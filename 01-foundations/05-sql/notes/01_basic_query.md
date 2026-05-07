# SQL 基础一：基本查询

## 什么是 SQL？

SQL（Structured Query Language）是用于管理和操作关系型数据库的标准语言。

类比理解：
- 数据库 = Excel 工作簿
- 表 = Excel 工作表
- 行 = Excel 行
- 列 = Excel 列

## 基本查询语法

### SELECT 和 FROM

```sql
-- 查询所有列
SELECT * FROM employees;

-- 查询特定列
SELECT name, age, salary FROM employees;

-- 别名
SELECT name AS 姓名, age AS 年龄 FROM employees;
```

### WHERE 条件

```sql
-- 等于
SELECT * FROM employees WHERE age = 25;

-- 不等于
SELECT * FROM employees WHERE age != 25;

-- 大于/小于
SELECT * FROM employees WHERE salary > 5000;
SELECT * FROM employees WHERE age < 30;

-- BETWEEN
SELECT * FROM employees WHERE age BETWEEN 20 AND 30;

-- IN
SELECT * FROM employees WHERE department IN ('技术部', '市场部');

-- LIKE（模糊匹配）
SELECT * FROM employees WHERE name LIKE '张%';  -- 以张开头
SELECT * FROM employees WHERE name LIKE '%三%';  -- 包含三

-- IS NULL
SELECT * FROM employees WHERE email IS NULL;
SELECT * FROM employees WHERE email IS NOT NULL;
```

### 逻辑运算符

```sql
-- AND
SELECT * FROM employees WHERE age > 25 AND salary > 5000;

-- OR
SELECT * FROM employees WHERE department = '技术部' OR department = '市场部';

-- NOT
SELECT * FROM employees WHERE NOT department = '技术部';
```

### ORDER BY 排序

```sql
-- 升序（默认）
SELECT * FROM employees ORDER BY age;

-- 降序
SELECT * FROM employees ORDER BY salary DESC;

-- 多列排序
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

### LIMIT 限制行数

```sql
-- 查询前 10 条
SELECT * FROM employees LIMIT 10;

-- 跳过前 5 条，查询 10 条
SELECT * FROM employees LIMIT 10 OFFSET 5;
```

## 常用函数

### 字符串函数

```sql
-- 长度
SELECT LENGTH(name) FROM employees;

-- 转换大小写
SELECT UPPER(name), LOWER(email) FROM employees;

-- 截取
SELECT SUBSTRING(name, 1, 1) FROM employees;  -- 取第一个字

-- 拼接
SELECT CONCAT(name, ' - ', department) FROM employees;

-- 替换
SELECT REPLACE(phone, '-', '') FROM employees;
```

### 数值函数

```sql
-- 四舍五入
SELECT ROUND(salary, 2) FROM employees;

-- 向上取整
SELECT CEIL(salary) FROM employees;

-- 向下取整
SELECT FLOOR(salary) FROM employees;

-- 绝对值
SELECT ABS(profit) FROM sales;
```

### 日期函数

```sql
-- 当前日期
SELECT CURRENT_DATE;

-- 当前时间
SELECT CURRENT_TIMESTAMP;

-- 提取年/月/日
SELECT YEAR(hire_date), MONTH(hire_date), DAY(hire_date) FROM employees;

-- 日期加减
SELECT hire_date + INTERVAL 30 DAY FROM employees;
SELECT hire_date - INTERVAL 1 YEAR FROM employees;

-- 日期差
SELECT DATEDIFF(end_date, start_date) FROM projects;
```

### 聚合函数

```sql
-- 计数
SELECT COUNT(*) FROM employees;
SELECT COUNT(DISTINCT department) FROM employees;

-- 求和
SELECT SUM(salary) FROM employees;

-- 平均值
SELECT AVG(salary) FROM employees;

-- 最大/最小
SELECT MAX(salary), MIN(salary) FROM employees;
```

## 子查询

```sql
-- 标量子查询
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- IN 子查询
SELECT * FROM employees WHERE department IN (SELECT name FROM departments WHERE location = '北京');

-- EXISTS 子查询
SELECT * FROM employees e WHERE EXISTS (SELECT 1 FROM orders o WHERE o.employee_id = e.id);
```

## CASE WHEN 条件表达式

```sql
-- 简单 CASE
SELECT name, 
       CASE department 
           WHEN '技术部' THEN '研发'
           WHEN '市场部' THEN '销售'
           ELSE '其他'
       END AS 部门分类
FROM employees;

-- 搜索 CASE
SELECT name,
       CASE 
           WHEN salary >= 10000 THEN '高薪'
           WHEN salary >= 5000 THEN '中等'
           ELSE '低薪'
       END AS 薪资等级
FROM employees;
```

## DISTINCT 去重

```sql
-- 去重查询
SELECT DISTINCT department FROM employees;

-- 多列去重
SELECT DISTINCT department, city FROM employees;
```

## 常见坑

### 坑1：NULL 的比较

```sql
-- 错误：NULL 不能用 = 比较
SELECT * FROM employees WHERE email = NULL;  -- 不会返回结果

-- 正确：使用 IS NULL
SELECT * FROM employees WHERE email IS NULL;
```

### 坑2：字符串比较

```sql
-- 字符串比较区分大小写（取决于数据库）
SELECT * FROM employees WHERE name = '张三';  -- 可能查不到 '张三 '

-- 使用 TRIM 去除空格
SELECT * FROM employees WHERE TRIM(name) = '张三';
```

### 坑3：日期格式

```sql
-- 不同数据库日期格式不同
-- MySQL: '2024-01-15'
-- SQL Server: '20240115' 或 '2024-01-15'

-- 使用标准格式 'YYYY-MM-DD'
SELECT * FROM employees WHERE hire_date = '2024-01-15';
```

## 速查表

| 操作 | 代码 |
|------|------|
| 查询所有列 | `SELECT * FROM table` |
| 条件查询 | `SELECT * FROM table WHERE condition` |
| 排序 | `SELECT * FROM table ORDER BY col` |
| 限制行数 | `SELECT * FROM table LIMIT n` |
| 去重 | `SELECT DISTINCT col FROM table` |
| 模糊匹配 | `SELECT * FROM table WHERE col LIKE '%pattern%'` |
| 聚合函数 | `SELECT COUNT(*), SUM(col), AVG(col) FROM table` |

## 小测验

1. WHERE 和 HAVING 的区别？
2. NULL 的比较应该用什么？
3. LIKE 中 % 和 _ 的区别？
4. ORDER BY 默认是升序还是降序？
5. 聚合函数有哪些？
