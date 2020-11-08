```sql
-- 创建一个视图，保存重复3的号码
SELECT
	id,号码, count(号码) AS a 
FROM
	table_all_merge 
GROUP BY
	号码 
HAVING
	a > 2;
	-- 创建一个视图，保存重复2次的号码
CREATE VIEW view_phone_2 AS SELECT
号码,
COUNT( `号码` ) AS a 
FROM
	table_all_merge 
GROUP BY
	`号码` 
HAVING
	a > 1 and a<3;
	-- 查询标记为TV的重复号码
SELECT
	a.id,
	a.phone,a.mark
FROM
	table_all_merge as a
	INNER JOIN  xiaoyu.view_phone_3  ON a.phone=xiaoyu.view_phone_3.phone
where mark='TV';
-- 查询标记为TV或者短板的重复号码
SELECT
	a.id,
	a.phone,a.mark
FROM
	table_all_merge as a
	INNER JOIN  xiaoyu.view_phone_3  ON a.phone=xiaoyu.view_phone_3.phone
where mark='TV' or mark='短板';
```