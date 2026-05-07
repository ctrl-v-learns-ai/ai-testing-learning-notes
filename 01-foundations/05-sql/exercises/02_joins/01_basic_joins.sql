-- SQL 基础练习2：表连接
-- 练习目标：掌握各种 JOIN 的使用
-- 前置知识：基本查询

-- 创建部门表
CREATE TABLE departments (
    id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location VARCHAR(50)
);

-- 创建员工表
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- 创建订单表
CREATE TABLE orders (
    id INT PRIMARY KEY,
    employee_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- 插入测试数据
INSERT INTO departments (id, department_name, location) VALUES
(1, '技术部', '北京'),
(2, '市场部', '上海'),
(3, '人事部', '广州'),
(4, '财务部', '深圳');

INSERT INTO employees (id, name, department_id, salary) VALUES
(1, '张三', 1, 8000.00),
(2, '李四', 2, 7000.00),
(3, '王五', 1, 9000.00),
(4, '赵六', 3, 7500.00),
(5, '钱七', NULL, 6500.00);

INSERT INTO orders (id, employee_id, order_date, amount) VALUES
(1, 1, '2024-01-15', 1500.00),
(2, 1, '2024-02-20', 2300.00),
(3, 2, '2024-01-10', 800.00),
(4, 3, '2024-03-05', 3200.00),
(5, 3, '2024-04-18', 1800.00);

-- 练习2.1：INNER JOIN
-- 查询员工及其部门信息
SELECT e.name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- 练习2.2：LEFT JOIN
-- 查询所有员工（包括没有部门的）
SELECT e.name, d.department_name, e.salary
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- 练习2.3：RIGHT JOIN
-- 查询所有部门（包括没有员工的）
SELECT e.name, d.department_name, e.salary
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;

-- 练习2.4：多表连接
-- 查询员工、部门和订单信息
SELECT e.name, d.department_name, o.order_date, o.amount
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN orders o ON e.id = o.employee_id;

-- 练习2.5：自连接
-- 查询员工及其上级（假设 id 小的是上级）
SELECT e.name AS 员工, m.name AS 上级
FROM employees e
LEFT JOIN employees m ON e.department_id = m.department_id AND e.id > m.id;

-- 练习2.6：使用 USING
-- 当列名相同时，可以使用 USING
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d USING (department_id);

-- 练习2.7：统计每个部门的订单数
SELECT d.department_name, COUNT(o.id) AS 订单数
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
LEFT JOIN orders o ON e.id = o.employee_id
GROUP BY d.department_name;

-- 练习2.8：统计每个部门的订单总额
SELECT d.department_name, COALESCE(SUM(o.amount), 0) AS 订单总额
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
LEFT JOIN orders o ON e.id = o.employee_id
GROUP BY d.department_name;

-- 练习2.9：查询没有订单的员工
SELECT e.name
FROM employees e
LEFT JOIN orders o ON e.id = o.employee_id
WHERE o.id IS NULL;

-- 练习2.10：查询订单金额大于平均订单金额的订单
SELECT o.*, e.name
FROM orders o
INNER JOIN employees e ON o.employee_id = e.id
WHERE o.amount > (SELECT AVG(amount) FROM orders);

/*
思考题：
1. INNER JOIN 和 LEFT JOIN 的区别？
2. 什么时候用 RIGHT JOIN？
3. 如何处理 JOIN 中的 NULL 值？
4. 自连接是什么？什么场景使用？
5. 如何优化 JOIN 查询性能？
*/
