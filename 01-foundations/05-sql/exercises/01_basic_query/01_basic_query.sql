-- SQL 基础练习1：基本查询
-- 练习目标：掌握 SELECT、WHERE、ORDER BY、LIMIT
-- 前置知识：无

-- 创建测试表
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    city VARCHAR(50),
    hire_date DATE,
    email VARCHAR(100)
);

-- 插入测试数据
INSERT INTO employees (id, name, age, department, salary, city, hire_date, email) VALUES
(1, '张三', 25, '技术部', 8000.00, '北京', '2023-01-15', 'zhangsan@example.com'),
(2, '李四', 30, '市场部', 7000.00, '上海', '2022-06-20', 'lisi@example.com'),
(3, '王五', 28, '技术部', 9000.00, '北京', '2023-03-10', 'wangwu@example.com'),
(4, '赵六', 35, '人事部', 7500.00, '广州', '2021-11-05', 'zhaoliu@example.com'),
(5, '钱七', 22, '技术部', 6500.00, '深圳', '2024-01-20', 'qianqi@example.com'),
(6, '孙八', 29, '市场部', 7200.00, '上海', '2022-09-15', 'sunba@example.com'),
(7, '周九', 32, '技术部', 9500.00, '北京', '2021-05-10', 'zhoujiu@example.com'),
(8, '吴十', 27, '人事部', 6800.00, '广州', '2023-07-25', 'wushi@example.com'),
(9, '郑十一', 24, '技术部', 7200.00, '深圳', '2024-02-14', 'zheng11@example.com'),
(10, '王十二', 31, '市场部', 8500.00, '上海', '2022-04-18', 'wang12@example.com');

-- 练习1.1：查询所有数据
SELECT * FROM employees;

-- 练习1.2：查询特定列
SELECT name, age, salary FROM employees;

-- 练习1.3：条件查询
-- 查询年龄大于25的员工
SELECT * FROM employees WHERE age > 25;

-- 练习1.4：多条件查询
-- 查询技术部且薪资大于8000的员工
SELECT * FROM employees WHERE department = '技术部' AND salary > 8000;

-- 练习1.5：IN 查询
-- 查询技术部和市场部的员工
SELECT * FROM employees WHERE department IN ('技术部', '市场部');

-- 练习1.6：LIKE 模糊查询
-- 查询姓张的员工
SELECT * FROM employees WHERE name LIKE '张%';

-- 练习1.7：BETWEEN 查询
-- 查询年龄在25到30之间的员工
SELECT * FROM employees WHERE age BETWEEN 25 AND 30;

-- 练习1.8：NULL 查询
-- 查询邮箱不为空的员工
SELECT * FROM employees WHERE email IS NOT NULL;

-- 练习1.9：排序
-- 按薪资降序排列
SELECT * FROM employees ORDER BY salary DESC;

-- 练习1.10：多列排序
-- 先按部门升序，再按薪资降序
SELECT * FROM employees ORDER BY department ASC, salary DESC;

-- 练习1.11：限制行数
-- 查询薪资最高的3名员工
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

-- 练习1.12：去重查询
-- 查询所有部门
SELECT DISTINCT department FROM employees;

-- 练习1.13：别名
-- 使用别名查询
SELECT name AS 姓名, age AS 年龄, salary AS 薪资 FROM employees;

-- 练习1.14：CASE WHEN
-- 根据薪资等级分类
SELECT name, salary,
       CASE 
           WHEN salary >= 9000 THEN '高薪'
           WHEN salary >= 7000 THEN '中等'
           ELSE '低薪'
       END AS 薪资等级
FROM employees;

/*
思考题：
1. WHERE 和 HAVING 的区别？
2. LIKE 中 % 和 _ 的区别？
3. ORDER BY 默认是升序还是降序？
4. 如何查询 NULL 值？
5. DISTINCT 的作用是什么？
*/
