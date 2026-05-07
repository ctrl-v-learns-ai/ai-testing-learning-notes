# SQL 基础二：表连接（JOIN）

## 什么是 JOIN？

JOIN 用于根据两个或多个表中的相关列来合并数据。

类比理解：
- JOIN = 合并两个 Excel 表（根据共同列）

## JOIN 类型

### INNER JOIN（内连接）

```sql
-- 只返回两个表中匹配的行
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- 等价写法
SELECT e.name, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.id;
```

### LEFT JOIN（左连接）

```sql
-- 返回左表所有行，右表匹配的行
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- 没有匹配的行，右表列显示 NULL
```

### RIGHT JOIN（右连接）

```sql
-- 返回右表所有行，左表匹配的行
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

### FULL OUTER JOIN（全外连接）

```sql
-- 返回两个表的所有行
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;

-- MySQL 不支持 FULL OUTER JOIN，使用 UNION
SELECT e.name, d.department_name
FROM employees e LEFT JOIN departments d ON e.department_id = d.id
UNION
SELECT e.name, d.department_name
FROM employees e RIGHT JOIN departments d ON e.department_id = d.id;
```

### CROSS JOIN（交叉连接）

```sql
-- 返回两个表的笛卡尔积
SELECT e.name, p.product_name
FROM employees e
CROSS JOIN products p;

-- 等价于
SELECT e.name, p.product_name
FROM employees e, products p;
```

## 多表连接

```sql
-- 连接三个表
SELECT e.name, d.department_name, c.city_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN cities c ON e.city_id = c.id;

-- 连接顺序影响性能
-- 小表驱动大表
```

## 自连接

```sql
-- 员工和上级
SELECT e.name AS 员工, m.name AS 上级
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

## USING 和 NATURAL JOIN

```sql
-- USING（当列名相同时）
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d USING (department_id);

-- NATURAL JOIN（自动匹配同名列）
SELECT e.name, d.department_name
FROM employees e
NATURAL JOIN departments d;
```

## 连接性能优化

```sql
-- 1. 使用索引
CREATE INDEX idx_department_id ON employees(department_id);

-- 2. 小表驱动大表
SELECT * FROM small_table s
INNER JOIN big_table b ON s.id = b.small_id;

-- 3. 避免 SELECT *
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- 4. 使用 WHERE 过滤后再连接
SELECT e.name, d.department_name
FROM (SELECT * FROM employees WHERE age > 25) e
INNER JOIN departments d ON e.department_id = d.id;
```

## 常见坑

### 坑1：JOIN 条件错误

```sql
-- 错误：忘记加 JOIN 条件
SELECT e.name, d.department_name
FROM employees e, departments d;
-- 返回笛卡尔积

-- 正确：加 JOIN 条件
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

### 坑2：NULL 的处理

```sql
-- LEFT JOIN 时，右表没有匹配的行会显示 NULL
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- 如果 department_id 为 NULL，不会匹配任何部门
-- 需要特殊处理
SELECT e.name, COALESCE(d.department_name, '未分配') AS department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

### 坑3：重复行

```sql
-- 一对多关系会导致重复行
SELECT e.name, o.order_id
FROM employees e
INNER JOIN orders o ON e.id = o.employee_id;

-- 如果员工有多个订单，员工名会重复
-- 使用 DISTINCT 去重
SELECT DISTINCT e.name
FROM employees e
INNER JOIN orders o ON e.id = o.employee_id;
```

## 速查表

| JOIN 类型 | 说明 | 代码 |
|-----------|------|------|
| INNER JOIN | 只返回匹配的行 | `SELECT * FROM a INNER JOIN b ON a.id = b.a_id` |
| LEFT JOIN | 返回左表所有行 | `SELECT * FROM a LEFT JOIN b ON a.id = b.a_id` |
| RIGHT JOIN | 返回右表所有行 | `SELECT * FROM a RIGHT JOIN b ON a.id = b.a_id` |
| FULL OUTER JOIN | 返回两个表所有行 | `SELECT * FROM a FULL OUTER JOIN b ON a.id = b.a_id` |
| CROSS JOIN | 返回笛卡尔积 | `SELECT * FROM a CROSS JOIN b` |

## 小测验

1. INNER JOIN 和 LEFT JOIN 的区别？
2. 什么时候用 RIGHT JOIN？
3. 如何处理 JOIN 中的 NULL 值？
4. 自连接是什么？什么场景使用？
5. 如何优化 JOIN 查询性能？
