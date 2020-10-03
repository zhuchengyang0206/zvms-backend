# zvms
## user

这个表只储存可以登录的用户，预计每个班和每个老师分配一个账户，义管会、实践部另算

项名 |备注 | 类型 | 简述 | 举例 | 其他 
-|-|-|-|-|-
uid |user identity | INTEGER | 储存用户的id | 202001 | 不需要自动递增， 唯一， 理论上六位即可
unm |user name | CHAR(64) | 储存用户的名字 | 王彳亍 | 长度不知道要多少，凭感觉来:-D
cls |class | INTEGER | 储存用户拥有的班级id | 202001 | 理论长度其实也是六位就够
pms |permission | SMALLINT | 储存用户的身份权限 | 0 | 1:团支书 2: 教师 3: 义管会 4: 系统 权限等级待定
pwd |password | CHAR(255) | 储存密码 | aababababab | 记得加密，方式待定

## student

这个表存储每个学生的身份以及部分义工信息

项名 |备注 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-|-
sid |student identity | INTEGER | 储存学生的学号 | 20200101 | 不需要自动递增， 唯一， 理论上八位即可
snm |student name | CHAR(64) | 储存学生的名字 | 王彳亍 | 长度不知道要多少，凭感觉来:-D
vti |volunteering time inside | INTEGER | 储存学生的义工时间 | 0 | 避免浮点运算，在数据库中以分钟为单位
vto |volunteering time outside | INTEGER | 储存学生的义工时间 | 0 | 以分钟为单位
vtl |volunteering time large | INTEGER | 储存学生的义工时间 | 0 | 以分钟为单位

## volunteer

这个表存储每次义工活动

项名 |备注 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-|-
vid |volunteering identity | INTEGER | 义工活动的唯一确定编号 | 1 | 其实这个自动递增倒也无所谓
vnm |volunteering name | CHAR(256) | 义工活动的名称 | 喂孔子+拜锦鲤 | 长度不知道要多少，凭感觉来:-D
vtm |volunteering time | CHAR(256) | 义工活动的时间 | 2020.9.24 | 长度不知道要多少，凭感觉来:-D
smx |maximum students | INTEGER | 义工活动的人数上限 | 10 | 
dsc |description | CHAR(1024) | 义工活动的描述 | blablablabla | 长度不知道要多少，凭感觉来:-D
stt |status | SMALLINT | 义工活动的状态 | 0 | `0`表示已经结束，`1`表示还没开始，`2`表示正在进行
vti |volunteering time inside | INTEGER | 每个人预计将获得的义工时间 | 0 | 以分钟为单位
vto |volunteering time outside | INTEGER | 每个人预计将获得的义工时间 | 0 | 以分钟为单位
vtl |volunteering time large | INTEGER | 每个人预计将获得的义工时间 | 0 | 以分钟为单位

## stu_vol

这个表存储学生和义工之间的关系

项名 |备注 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-|-
vid |volunteering identity | INTEGER | 义工活动的编号 | 1 | 表示`sid`的学生参加了这个义工活动 
sid |student identity | INTEGER | 学生的学号 | 20200101 | 表示这个学生参加了`vid`的义工活动 
stt |status | SMALLINT | 审核状态 | 0 | `0`表示未通过，`1`表示通过，`2`表示审核中
vti |volunteering time inside | INTEGER | 实际获得的义工时间 | 0 | 以分钟为单位
vto |volunteering time outside | INTEGER | 实际获得的义工时间 | 0 | 以分钟为单位
vtl |volunteering time large | INTEGER | 实际获得的义工时间 | 0 | 以分钟为单位

## class_vol

这个表存储义工活动分配给哪些班级

项名 |备注 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-|-
vid |volunteering identity | INTEGER | 义工活动的编号 | 1 | 
cls |class | INTEGER | 班级的编号 | 202001 | 表示`vid`的义工活动，这个班级被允许参加 
