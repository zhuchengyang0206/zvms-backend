create user 'zvms'@'127.0.0.1' identified by '123456';
grant SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
	on *.* to 'zvms'@'127.0.0.1' with grant option;
flush privileges;
create database zvms;
use zvms;

create table user (
	userId int AUTO_INCREMENT,
	userName char(64),
	class int,
	permission smallint,
	password char(255),
	primary key (userId)
)charset=utf8;

insert into user (userName,class,permission,password)
          values ("高一1班",202001,0,"e10adc3949ba59abbe56e057f20f883e");
insert into user (userName,class,permission,password)
          values ("高一2班",202002,0,"e10adc3949ba59abbe56e057f20f883e");
insert into user (userName,class,permission,password)
          values ("Admin",202001,3,"e10adc3949ba59abbe56e057f20f883e");

create table student (
	stuId int,
	stuName char(64),
	volTimeInside int,
	volTimeOutside int,
	volTimeLarge int,
	primary key (stuId)
)charset=utf8;

insert into student (stuId,stuName,volTimeInside,volTimeOutside,volTimeLarge)
             values (20200101,"张三",0,0,0);
insert into student (stuId,stuName,volTimeInside,volTimeOutside,volTimeLarge)
             values (20200102,"张",10,0,0);
insert into student (stuId,stuName,volTimeInside,volTimeOutside,volTimeLarge)
             values (20200201,"三",100,0,0);
insert into student (stuId,stuName,volTimeInside,volTimeOutside,volTimeLarge)
             values (20200202,"三张",20,36,4);

create table volunteer (
	volId int AUTO_INCREMENT,
	volName char(255),
	volDate char(64),
	volTime char(64),
	stuMax int,
	nowStuCount int,
	description text,
	status smallint,
	volTimeInside int,
	volTimeOutside int,
	volTimeLarge int,
	holderId int,
	primary key (volId)
)charset=utf8;

create table stu_vol (
	volId int,
	stuId int,
	status smallint,
	volTimeInside int,
	volTimeOutside int,
	volTimeLarge int,
	thought text
)charset=utf8;

create table class_vol (
	volId int,
	class int,
	stuMax int,
	nowStuCount int
)charset=utf8;