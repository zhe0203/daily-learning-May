# 查询001课程比002课程成绩高的所有学生的学号
select stuid
from tblstudent as s1
where (
	select score from tblscore as t1 where t1.stuid=s1.stuid and t1.courseld='001'
) > (
	select score from tblscore as t2 where t2.stuid=s1.stuid and t2.courseld='002'
)

# 查询平均成绩大于60分的同学的学号和平均成绩
select stuid,avg(score)
from tblscore
group by stuid
having avg(score)>60

# 查询所有同学的学号、姓名、选课数、总成绩
select stuid,stuname,
	selcourses=(select count(courseld) from tblscore as t1 where t1.stuid=s1.stuid)
	sumscore=(select sum(score) from tblscore as t2 where t2.stuid=s1.stuid)
from tblstudent as s1

select a.sno,a.sname,selcourses=(select count(cname) from dbo.Course as t1 where t1.cno=a.sno)
from (select right(sno,4) as sno,sname from dbo.student) as a

use mrkj；
select courseid,geshu=(select count(*) from tblscore as s1 where c1.courseid=s1.courseid and score>30)
from tblCourse as c1

select stuid,stuname,jige=(select count(score) from tblscore as t1 where t1.stuid=t2.stuid and score>=40)
from tblstudent as t2
where (select count(score) from tblscore as t1 where t1.stuid=t2.stuid and score>=40)>0

# 查询李老师的个数
select count(*) from tblteacher where teaname like '李%'

# 查询没有学过'叶平'老师课的同学的学号、姓名
select stuid,stuname
from tblstudent
where stuid not in (
	select stuid from tblscore as score
	inner join tblscore as cu on sc.Courseld=cu.courseld
	inner join tblteacher as tc on cu.teald=tc.teald
	where tc.teaname='叶平'
)

# 对于某字段要求乘以某一个数据，可以使用update对其进行数据更新，再使用查询操作
use db_2008;
update Student
set sage=sage*2
where sname='李羽凡'

# 在表连接中 and 用法的区别
select *
from tblscore as s1 left join tblstudent as c1
on s1.courseid=s1.courseid and score>60              # 连接中使用and表示选择score>60的数据进行连接操作，小于60的将显示NULL

select *
from tblscore as s1 left join tblstudent as c1
on s1.courseid=s1.courseid 
where score>60                                       # 使用where表示对结果进行筛选

# 选择与TableName1匹配的数据TableName
select *
from tablename t
where exists (
	select 1 from tablename1 t1 where t.id=t1.id
)

# update加上inner join的用法
update employees
set phonenumber = c.phonenumber
from employees as e
inner join customers as c
on e.fname = c.fname and e.lname=c.lname
where phonenumber is null

update employees
set phonenumber = (
	select c.phonenumber
	from customers as c
	where c.fname=employees.fname
		and c.lname=employees.lname
		and employees.phonenumber is null
)

# 子查询
select id,fname,lname,
	(select count(*) from cars where cars.customerid=customer.id) as numberofcars
from customers

select w.* (select c.state from cities as c where c.name=w.city) as state
from weather as w

select customers,
	sum(case when payment_type='credit' then amount else 0 end) as credit,
	sum(case when payment_type='debit' then amount else 0 end ) as debit
from payments
group by customer

# 数据类型的转换
select cast('abc' as char(10)) -- 'abc       '
select cast('abc' as varchar(10))  -- 'abc'
select cast('ABCDEFGHIJKLMNOPQRSTUVWXYZ' as char(10))  -- 'ABCDEFGHIJ' (truncated to 10 characters)
# 给数据增加小数点的位数
select cast(123 as decimal(5,2))  -- 123.00
select cast(12345.12 as numeric(10,5))  -- 12345.12000
select cast(pi() as float)
select cast(pi() as real)

with a as (
	select *
	from employees
	where id=4
	union all
	select employees.*
	from employees join managersofjonathon on
		employees.id=managersofjonathon.managerid
)

with all_sales as(
	SELECT product.price, category.id as category_id, category.description as category_description
	from sale
	left join product on sale.product_id=product.id
	left join category on product.category_id=category.id
),
sales_by_category as(
	SELECT category_description, sum(price) as total_sales
	from all_sales    -- 这里可以使用上面的临时表
	group by category_id,category_description
)
selct * from sales_by_category where total_sales>20
