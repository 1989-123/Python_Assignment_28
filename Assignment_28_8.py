"""
Create Courses table (cid, cname) where cid is a primary key and Student table
(rollno, name, cid) where rollno is a primary key and cid is a foreign key.
"""

create table courses(c_id int,c_name text,primary key(c_id));

postgres=# create table student(
postgres(# roll_no int,
postgres(# s_name text,
postgres(# c_id int,
postgres(# primary key(roll_no),
postgres(# constraint fk_dept foreign key(c_id) references courses(c_id)
postgres(# );