-- SQL 基础练习3：分组聚合
-- 练习目标：掌握 GROUP BY、HAVING、窗口函数
-- 前置知识：基本查询、表连接

-- 创建测试表
CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    region VARCHAR(50),
    salesperson VARCHAR(50),
    amount DECIMAL(10, 2),
    quantity INT,
    sale_date DATE
);

-- 插入测试数据
INSERT INTO sales (id, product_name, category, region, salesperson, amount, quantity, sale_date) VALUES
(1, '笔记本电脑', '电子产品', '华东', '张三', 5999.00, 2, '2024-01-15'),
(2, '手机', '电子产品', '华南', '李四', 3999.00, 5, '2024-01-20'),
(3, '平板电脑', '电子产品', '华东', '张三', 2999.00, 3, '2024-02-10'),
(4, '显示器', '电子产品', '华北', '王五', 1999.00, 4, '2024-02-15'),
(5, '键盘', '配件', '华东', '赵六', 499.00, 10, '2024-03-05'),
(6, '鼠标', '配件', '华南', '李四', 199.00, 20, '2024-03-10'),
(7, '笔记本电脑', '电子产品', '华北', '王五', 5999.00, 1, '2024-04-18'),
(8, '手机', '电子产品', '华东', '张三', 3999.00, 3, '2024-04-25'),
(9, '平板电脑', '电子产品', '华南', '李四', 2999.00, 2, '2024-05-12'),
(10, '显示器', '配件', '华北', '赵六', 1999.00, 5, '2024-05-20');

-- 练习3.1：基本分组
-- 统计每个类别的销售数量
SELECT category, COUNT(*) AS 销售次数
FROM sales
GROUP BY category;

-- 练习3.2：多列分组
-- 统计每个地区每个类别的销售数量
SELECT region, category, COUNT(*) AS 销售次数
FROM sales
GROUP BY region, category;

-- 练习3.3：聚合函数
-- 统计每个类别的总销售额、平均销售额、最大销售额
SELECT category,
       SUM(amount) AS 总销售额,
       AVG(amount) AS 平均销售额,
       MAX(amount) AS 最大销售额,
       MIN(amount) AS 最小销售额
FROM sales
GROUP BY category;

-- 练习3.4：HAVING 过滤
-- 查询总销售额大于10000的类别
SELECT category, SUM(amount) AS 总销售额
FROM sales
GROUP BY category
HAVING SUM(amount) > 10000;

-- 练习3.5：WHERE 和 HAVING 结合
-- 查询2024年Q1（1-3月）总销售额大于5000的类别
SELECT category, SUM(amount) AS 总销售额
FROM sales
WHERE sale_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY category
HAVING SUM(amount) > 5000;

-- 练习3.6：排序
-- 按总销售额降序排列
SELECT category, SUM(amount) AS 总销售额
FROM sales
GROUP BY category
ORDER BY 总销售额 DESC;

-- 练习3.7：GROUP_CONCAT（MySQL）
-- 统计每个地区的销售人员列表
SELECT region, GROUP_CONCAT(DISTINCT salesperson) AS 销售人员
FROM sales
GROUP BY region;

-- 练习3.8：窗口函数 - 行号
-- 按销售额排名
SELECT product_name, category, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS 排名
FROM sales;

-- 练习3.9：窗口函数 - 分区排名
-- 按类别分组，按销售额排名
SELECT product_name, category, amount,
       ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) AS 类别排名
FROM sales;

-- 练习3.10：窗口函数 - 累计求和
-- 按日期累计销售额
SELECT sale_date, amount,
       SUM(amount) OVER (ORDER BY sale_date) AS 累计销售额
FROM sales;

-- 练习3.11：窗口函数 - 移动平均
-- 计算3条记录的移动平均
SELECT sale_date, amount,
       AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS 移动平均
FROM sales;

-- 练习3.12：子查询和分组
-- 查询每个类别销售额最高的产品
SELECT * FROM sales s1
WHERE amount = (SELECT MAX(amount) FROM sales s2 WHERE s2.category = s1.category);

-- 练习3.13：使用窗口函数更高效
SELECT * FROM (
    SELECT *, 
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC) AS rn
    FROM sales
) t
WHERE rn = 1;

/*
思考题：
1. WHERE 和 HAVING 的区别？
2. GROUP BY 和 ORDER BY 的顺序？
3. 聚合函数有哪些？
4. 窗口函数和聚合函数的区别？
5. 如何取每个分组的第一条记录？
*/
