
wm_concat()  # 该函数进行行转列 oracle中mysql中有的函数
oracle中使用nvl函数来讲空值变成非空值
count(comm)   # 只会统计非空值，忽略空值
count(nvl(comm,0))  # 当comm为非空时，将为comm，为空时，为0

# 分组函数的嵌套
max(avg(sal))



select deptno,job,sum(sal)
from emp
group by deptno,job;  # 未包含在组函数中的值，全部写在group by中


alter table old_table_name rename new_table_name;    # 修改表的名字
use company;  #  选择company数据库
desc t_dept;  # 查看表t_dept的定义信息
alter table t_dept
add descri varchar(20);    # 向表t_dept中添加字段
add descri varchar(20) first;    # 通过使用first来指定添加的字段位于第一个
add descri varchar(20) after depyno;   # 通过使用after可在指定的字段后面添加字段
alter table t_dept
drop deptno;                          # 删除字段
alter table t_dept
modify deptno varchar(20);            # 修改某字段
alter table t_dept
change 旧属性名 新属性名 旧属性类型;   # 修改某字段名字




# 排序检索数据
select prod_name,prod_id,prod_price
from products
order by prod_price,prod_name        # 仅在多个行中具有相同的prod_price时，才对prod_name进行排序，此外，默认排序为升序
order by 2,3                         # 使用相对位置进行排序，与上面结果一样，指定prod_id prod_name进行排序
order by prod_price desc             # 使用desc来降序排序
order by prod_price desc,prod_name   # 多个排序列的使用

# 过滤数据
select prod_name,prod_price
from products
where prod_price=3.49                # 从products中检索两个列，但不返回所有的行，只返回prod_price值为3.49的行
where prod_price<10                  # 检索价格小于10的商品
where prod_price<=10
order by prod_name                   # order by 子句应位于 where 子句之后

select vend_id,prod_name             # 不匹配检索
from products
where vend_id<>'DLL01'；             # 列出所有不是供应商DLL01制造的产品 不匹配检索
where vend_id!='DLL01'；

select prod_name,prod_price          # 范围检索
from products
where prod_price between 5 and 10;   # 检索价格早5和10之间的所有商品 闭区间

select prod_name                     # 空值检索
from products
where prod_price is null;            # 返回空值的字符串

# 高级过滤器 not in
select prod_id,prod_price,prod_name              # 对不止一个列进行过滤
from products
where vend_id='DLL01' and prod_price<=4;         # 这里使用and

select prod_name,prod_price                      # 检索由任一个指定供应商制造的商品
from products
where ven_id='DLL01' OR ven_id='BRS01';          # 匹配任意一个条件，而不是同时匹配两个条件

select prod_name,prod_price                      # and 的优先级要高于 or
from products
where (ven_id='DLL01' or ven_id='BRS01') and prod_price>=10    

select prod_name,prod_price
from products
where ven_id in ('DLL01','BRS01')                # 其功能与or一样
order by prod_name;                              # prod_name desc

select prod_name
from products
where not ven_id='DLL01'                         # 否定跟在其后面的条件,使用 not
order by prod_name;

# 用通配符进行过滤
select prod_id,prod_name
from products
where prod_name like 'Fish%'                     # 找出所有以Fish起头的产品，access使用*

select prod_id,prod_name
from products
where prod_name like '%bean bag%'                # 表示匹配任何位置上包含文本bean bag的值

select prod_name
from products
where prod_name like 'F%y'                       # 找出以F开头，以y结尾的所有产品
where prod_name like 'F%y%'                      # 以匹配y后面的空格
where email like 'b%@forta.com';

select prod_id,prod_name
from products
where prod_name like '_ inch teddy bear'         # 总是刚好匹配一个字符串

select cust_contact
from customers
where cust_contact like '[JM]%'                  # 表示匹配括号中的任意一个字符
order by cust_contact;

select cust_contact
from customers
where cust_contact like '[^JM]%'                 # 匹配以J和M之外的任意字符起头的任意联系人 [!JM]
order by cust_contact;

select cust_contact
from customers
where not cust_contact like '[JM]%'              # 使用not 代替^
order by cust_contact;

#创建计算字段
select vend_name+' ('+vend_country+')'            # 使用加号将两个字段进行拼接
from vebdors
order by vend_name;

select concat(vend_name,' (',vend_country,')')
from vendors
order by vend_name;                                      # 返回列宽的文本值

select rtrim(vend_name)+' ('+rtrim(vend_country)+')'      # 使用rtrim将文本宽度的值空值去除
from vendors
order by vend_name;                                       # rtrim去掉值右边的所有空格

select rtrim(vend_name)+' ('+rtrim(vend_country)+')' as vend_title    # 将新的计算字段重新命名为新的名称
from vendors
order by vend_name;

select prod_id,quantity,item_price,quantity*item_price as expanded_price
from orderitems
where order_num=20008;

# 使用函数处理数据
select vend_name,upper(vend_name) as vend_name_upcase                # 使用upper转换成大写
from vendors
order by vend_name;

-- left,length,lower,ltrim,right,rtrim,soundex,upper

select order_num
from orderitems
where datepart(yy,order_date)=2012;                         # sql sever提取时间的方式
where year(order_date)=2012;                                # mysql 提取时间方式

# 汇总数据
select avg(prod_price) as avg_price                         # 求均值 忽略值列为null的行
from products
where ven_id='DLL01';

select count(*) as num_cust                                 # 对所有行计数，不管行中各列有什么值
from customers;

select count(cust_email) as num_cust                        # 此时对单个字段计数时，会忽略null值，只对有值进行计数
from customers;

select max(prod_price) as max_price                         # 返回列中最大的值忽略null min
from products;

select sum(quantity) as items_ordered                       # sum 忽略 null 值
from orderitems
where order_num=20005;

select avg(distinct prod_price) as avg_price
from products
where vend_id='DLL01';

select count(*) as num_items,
		min(prod_price) as price_min,
		max(prod_price) as price_max,
		avg(prod_price) as price_avg
from products;

# 分组数据
select vend_id,count(*) as num_prods
from products
where prod_price>=4
group by vend_id
having count(*)>=2;

select cust_id
from orders
where order_num in (select order_num
					from orderitems
					where prod_id='RGAN01')

select cust_name,cust_state,(select count(*) from orders where orders.cust_id=customers.cust_id) as orders
from customers
order by cust_name;

# 联接表
select vend_name,prod_name,prod_price                          # 指定要检索的列
from vendors,products                                          # 指定要联结的所有表
-- 完全限定名称，用一个句点分隔表名和列名
where vendors.vend_id=products.vend_id                           # 设置关联方式

select vend_name,prod_name,prod_price
from vendors inner join products                             # 使用 inner join 进行内连接
on vendors.vend_id=products.vend_id;

-- 连接多个表
select prod_name,vend_name,prod_price,quantity
from orderitems,products,vendors
where products.vend_id=vendors.vend_id                      # 这里使用 and
	and orderitems.prod_id=products.prod_id
	and order_num=20007;

# 创建高级连接
select cust_name,cust_contact
from customers as c,orders as o,orderitems as oi            # 定义表的别名
where c.cust_id=o.cust_id                                   # 这里使用表的别名
	and oi.order_num=o.order_num
	and prod_id='RGAN01';

select cust_id,cust_name,cust_contact
from customers
where cust_name=(select cust_name
					from customers
					where cust_contact='Jim Jones');

select customers.cust_id,orders.order_num
from customers left outer join orders                 #　从子句左边的表选择所有的行
on customers.cust_id=orders.order_num;

select customers.cust_id,orders.order_num
from customers right outer join orders                 #　从子句右边的表选择所有的行
on customers.cust_id=orders.order_num;

select customers.cust_id,orders.order_num
from customers full outer join orders                 #　完全连接 full outer join
on customers.cust_id=orders.order_num;

select customers.cust_id,count(orders.order_num) as num_ord
from customers inner join orders
	on customers.cust_id=orders.cust_id
group by customers.cust_id; 

select customers.cust_id,count(orders.order_num) as num_ord
from customers left outer join orders                         # 使用左连接来包含所有数据
	on customers.cust_id=orders.cust_id
group by customers.cust_id; 

# 组合查询 union
select cust_name,cust_contact,cust_email
from customers
where cust_state in ('IL','IN','MI')
union                                               # 这里使用union 对于两个sql语句查询的结果进行合并
-- 这里还可以使用 union all 匹配所有的行
select cust_name,cust_contact,cust_email
from customers
where cust_name='Fun4All'
order by cust_name,cust_contact desc;                    # 排序结果必须位于最后一条语句

-- 也可使用如下方法
select cust_name,cust_contact,cust_email
from customers
where cust_state in ('IL','IN','MI')
	or cust_name='Fun4All';

# 插入数据
insert into customers                       # 插入数据
	values('1000000006','toy land','123 any street','new york','ny','11111','usa',null,null);   #使用values

-- 这样编写不容易随着表结构的改变，插入的数据混乱
insert into customers(cust_id,cust_name,cust_address,cust_city,
						cust_state,cust_zip,cust_country,cust_contact,cust_email)
						values('1000000006','toy land','123 any street','new york','ny','11111','usa',null,null);
-- 当未给出列名时，默认插入的数值省略了这两列对应的值

-- 插入检索出的数据
insert into customers(cust_id,cust_name,cust_address,cust_city,
						cust_state,cust_zip,cust_country,cust_contact,cust_email)
select cust_id,cust_name,cust_address,cust_city,cust_state,cust_zip,cust_country,cust_contact,cust_email
from custnw;

select *
into custcopy          # 将数据复制到一个新表，并命名为custcopy
from customers;

# 更新和删除数据
update customers
set cust_email='kim@thetoystore.com'     # 使用set 来选择要更新的信息
where cust_id='1000000005';              # 必须使用where 不然将会对整个表进行更新

update customers
set cust_contact='sam roberts',          # 使用逗号,进行分割
	cust_email='kim@thetoystore'
where cust_id='1000000005';              # 必须使用where 不然将会对整个表进行更新

update customers
set cust_email=null                      # 删除某列的值，可将其设置为 null 值
where cust_id='1000000005';              

delete from customers
where cust_id='1000000005';              # 删除指定的行

# 创建和操作表
create table products                    # 创建的表名
	（
		prod_id     char(10)      not null,    # 列名 数据类型
		vend_id     char(10)      not null,
		prod_name   char(254)     not null,
		prod_price  decimal(8,2)  not null,
		prod_desc   varchar(1000) null
	);

create table orderitems
	(
		order_num   integer   not null,              # 不允许空值，必须存在值
		quantity    integer   not null    default 1  # 当未给出值时，默认将其填充为1
	)

-- 更新表
alter table vendors
add vend_phone char(20);    # 向表中增加列

alter table vendors
drop column vend_phone;     # 删除某列

drop table custcopy;        # 删除某个表

# 使用视图
create view productcustomers  as        #  创建视图命令
select cust_name,cust_contact,prod_id
from customers,orders,orderitems
where customers.cust_id=orders.cust_id
	and orderitems.order_num=orders.order_num;
select cust_name,cust_contact         # 从所创建的视图中检索出想要的信息
from productcustomers
where prod_id='RGAN01';

create view vendorlocations as
select rtrim(vend_name)+'('+rtrim(vend_country)+')'
	as vend_title
from vendors;
select *                         # 检索出所有数据
from vendorlocations;

create view customeremaillist as
select cust_id,cust_name,cust_email
from customers
where cust_email is not null;           # 利用视图过滤没有电子邮件的顾客
select *
from customeremaillist;

create view orderitemsexpanded as
select order_num,prod_id,quantity,item_price,
		quantity*item_price as expanded_price
from orderitems;
select *
from orderitemsexpanded
where order_num=20008;

# 使用存储过程
excute addnewproduct ('jts01','stuffed eifel tower',6.49,...)  # 执行存储过程

# case when使用
select *
备注=case
when grade>=90 then '成绩优秀'
when grade<90  and grade>=80 then '成绩良好'
when grade<80 and grade>=70 then '成绩及格'
else '不及格'
end
from tb_grade
######## case when 还可以使用其他字段计算数据
select *,age=(case when stusex='男' then stuage*2 else stuage end)
from tblStudent

use MRKJ;
with a as(
select *,age=(case when stusex='男' then stuage+10 else stuage end)
from tblStudent)
select stusex as 性别,avg(age) as 平均年龄
from a
group by stusex

# 将结果保存在一个新表中，在同一个数据库中select *,备注=case 
select *,
	备注=case 
	when sage<=18 then '未成年'
	when sage>18 and sage<=25 then '青年'
	else  '壮年'
	end
into Student2
from student

# 使用with将指定临时命名的结果集
use db_2008;                      # 必须加上;
with agereps(age,agecount) as     # 命名临时表的名称、字段名称
( 
	select age,count(*)
	from Employee
	where age is not NULL
	group by age
)
select age,agecount              # 从临时表中选取数据
from agereps


# 必须得从一个表中from 不能from（查询语句）
use db_2008;
select age,count(*) as agecount
into student3
from Employee
where age is not NULL
group by age
select *
from student3


#  嵌套使用临时表格
use db_2008;
with 
a as 
(
select *
from Student
where Sname like '王%'
),                         # 这里使用,进行分割
b as
(
select *
from Student
where Sage>=21
)
select * from a,b

# CTE后面也可以跟其他的CTE，但只能使用一个with，多个CTE中间用逗号（,）分隔，如下面的SQL语句所示：
with
cte1 as
(
    select * from table1 where name like 'abc%'
),
cte2 as
(
    select * from table2 where id > 20
),
cte3 as
(
    select * from table3 where price < 100
)
select a.* from cte1 a, cte2 b, cte3 c where a.id = b.id and a.id = c.id

use db_2008;
with a as
(
select *
from Student
where Sname like '王%'
),
b as
(
select *
from Student
where sage>=21
)
select a.sno,a.sname,a.sex,a.sage        # 将两个表进行连接在一起
from a inner join b
on a.sname=b.Sname

#  union 中order by 子句
#  在合并数据中使用union操作，只能有一个order by子句
#  这个子句必须在语句的末尾
use db_2008
select sname,sage
from student
union all
select cname,credit
from course
order by sage asc      # 该语句表示对于合并后的数据进行排序
