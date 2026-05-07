# SQL 基础三：分组聚合（GROUP BY）

## 什么是 GROUP BY？

GROUP BY 用于将数据按指定列分组，然后对每个组进行聚合计算。

类比理解：
- GROUP BY = Excel 的数据透视表（按某列分组，计算汇总）

## 基本语法

```sql
-- 基本分组
SELECT department, COUNT(*) AS 人数
FROM employees
GROUP BY department;

-- 多列分组
SELECT department, city, COUNT(*) AS 人数
FROM employees
GROUP BY department, city;
```

## 聚合函数

```sql
-- 计数
SELECT department, COUNT(*) AS 人数
FROM employees
GROUP BY department;

-- 求和
SELECT department, SUM(salary) AS 总薪资
FROM employees
GROUP BY department;

-- 平均值
SELECT department, AVG(salary) AS 平均薪资
FROM employees
GROUP BY department;

-- 最大/最小
SELECT department, MAX(salary) AS 最高薪资, MIN(salary) AS 最低薪资
FROM employees
GROUP BY department;

-- 多个聚合函数
SELECT department, 
       COUNT(*) AS 人数,
       SUM(salary) AS 总薪资,
       AVG(salary) AS 平均薪资,
       MAX(salary) AS 最高薪资,
       MIN(salary) AS 最低薪资
FROM employees
GROUP BY department;
```

## HAVING 过滤分组

```sql
-- WHERE 过滤行，HAVING 过滤分组
SELECT department, AVG(salary) AS 平均薪资
FROM employees
GROUP BY department
HAVING AVG(salary) > 5000;

-- 结合 WHERE 和 HAVING
SELECT department, AVG(salary) AS 平均薪资
FROM employees
WHERE age > 25
GROUP BY department
HAVING AVG(salary) > 5000;
```

## ORDER BY 和 GROUP BY

```sql
-- 分组后排序
SELECT department, COUNT(*) AS 人数
FROM employees
GROUP BY department
ORDER BY 人数 DESC;

-- 按聚合值排序
SELECT department, AVG(salary) AS 平均薪资
FROM employees
GROUP BY department
ORDER BY 平均薪资 DESC;
```

## 常用分组技巧

### GROUP_CONCAT / STRING_AGG

```sql
-- MySQL: GROUP_CONCAT
SELECT department, GROUP_CONCAT(name) AS 员工列表
FROM employees
GROUP BY department;

-- SQL Server: STRING_AGG
SELECT department, STRING_AGG(name, ',') AS 员工列表
FROM employees
GROUP BY department;
```

### DISTINCT 在聚合函数中

```sql
-- 计算不重复值
SELECT department, COUNT(DISTINCT city) AS 城市数
FROM employees
GROUP BY department;
```

### ROLLUP 和 CUBE

```sql
-- ROLLUP：生成小计和总计
SELECT department, city, SUM(salary)
FROM employees
GROUP BY ROLLUP(department, city);

-- CUBE：生成所有可能的组合
SELECT department, city, SUM(salary)
FROM employees
GROUP BY CUBE(department, city);
```

## 窗口函数（高级）

```sql
-- ROW_NUMBER：行号
SELECT name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS 排名
FROM employees;

-- RANK：排名（有并列）
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 排名
FROM employees;

-- DENSE_RANK：排名（无间隔）
SELECT name, department, salary,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS 排名
FROM employees;

-- SUM 窗口函数
SELECT name, department, salary,
       SUM(salary) OVER (PARTITION BY department) AS 部门总薪资
FROM employees;

-- AVG 窗口函数
SELECT name, department, salary,
       AVG(salary) OVER (PARTITION BY department) AS 部门平均薪资
FROM employees;
```

## 子查询和 GROUP BY

```sql
-- 分组后取最大值
SELECT * FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 分组后取每个部门薪资最高的人
SELECT * FROM employees e
WHERE salary = (SELECT MAX(salary) FROM employees WHERE department = e.department);

-- 使用窗口函数更高效
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
    FROM employees
) t
WHERE rn = 1;
```

## 性能优化

```sql
-- 1. 使用索引
CREATE INDEX idx_department ON employees(department);

-- 2. 先过滤再分组
SELECT department, COUNT(*)
FROM (SELECT * FROM employees WHERE age > 25) t
GROUP BY department;

-- 3. 避免 SELECT *
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

## 常见坑

### 坑1：SELECT 列必须在 GROUP BY 中

```sql
-- 错误：name 不在 GROUP BY 中
SELECT name, department, COUNT(*)
FROM employees
GROUP BY department;

-- 正确：name 必须在 GROUP BY 中或使用聚合函数
SELECT department, COUNT(*)
FROM employees
GROUP BY department;

-- 或者
SELECT department, MAX(name), COUNT(*)
FROM employees
GROUP BY department;
```

### 坑2：WHERE 和 HAVING 的区别

```sql
-- WHERE 在分组前过滤行
-- HAVING 在分组后过滤分组

-- 错误：WHERE 不能用聚合函数
SELECT department, AVG(salary)
FROM employees
WHERE AVG(salary) > 5000
GROUP BY department;

-- 正确：使用 HAVING
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 5000;
```

### 坑3：NULL 的分组

```sql
-- NULL 值会被分为一组
SELECT city, COUNT(*)
FROM employees
GROUP BY city;

-- 如果 city 有 NULL，会显示一行 NULL
```

## 速查表

| 操作 | 代码 |
|------|------|
| 基本分组 | `SELECT col, COUNT(*) FROM table GROUP BY col` |
| 多列分组 | `SELECT col1, col2, COUNT(*) FROM table GROUP BY col1, col2` |
| 过滤分组 | `SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 5` |
| 排序 | `SELECT col, COUNT(*) FROM table GROUP BY col ORDER BY COUNT(*) DESC` |
| 行号 | `SELECT *, ROW_NUMBER() OVER (PARTITION BY col ORDER BY col2) FROM table` |

## 小测验

1. WHERE 和 HAVING 的区别？
2. GROUP BY 和 ORDER BY 的顺序？
3. 聚合函数有哪些？
4. 窗口函数和聚合函数的区别？
5. 如何取每个分组的第一条记录？
