# zvms
## user

这个表只储存可以登录的用户，预计每个班和每个老师分配一个账户，义管会、实践部另算

项名 | 类型 | 简述 | 举例 | 其他 
-|-|-|-|-
userid | INTERGER | 储存用户的id | 202001 | 不需要自动递增， 唯一， 理论上六位即可
username | VARCHAR(64) | 储存用户的名字 | 王彳亍 | 长度不知道要多少，凭感觉来:-D
class | INTEGER | 储存用户拥有的班级id | 202001 | 理论长度其实也是六位就够
permission | SMALLINT | 储存用户的身份权限 | 0 | 0:团支书 1: 教师 2: 义管会 3: 实践部 4: 系统 权限等级待定
password | VARCHAR(255) | 储存密码 | aababababab | 记得加密，方式待定

## student

这个表存储每个学生的身份以及部分义工信息

项名 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-
stuId | INTERGER | 储存学生的学号 | 20200101 | 不需要自动递增， 唯一， 理论上八位即可
stuName | VARCHAR(64) | 储存学生的名字 | 王彳亍 | 长度不知道要多少，凭感觉来:-D
volTimeInside | INTERGER | 储存学生的义工时间 | 0 | 避免浮点运算，在数据库中以分钟为单位
volTimeOutside | INTERGER | 储存学生的义工时间 | 0 | 以分钟为单位
volTimeLarge | INTERGER | 储存学生的义工时间 | 0 | 以分钟为单位

## volunteer

这个表存储每次义工活动

项名 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-
volId | INTERGER | 义工活动的唯一确定编号 | 1 | 其实这个自动递增倒也无所谓
name | VARCHAR(256) | 义工活动的名称 | 喂孔子+拜锦鲤 | 长度不知道要多少，凭感觉来:-D
time | VARCHAR(256) | 义工活动的时间 | 2020.9.24 | 长度不知道要多少，凭感觉来:-D
volTimeInside | INTERGER | 每个人将获得的义工时间 | 0 | 以分钟为单位，如果后期要改成每个人分配不同的时间的话在下一个表中加一栏`volTime`就好
volTimeOutside | INTERGER | 每个人将获得的义工时间 | 0 | 以分钟为单位
volTimeLarge | INTERGER | 每个人将获得的义工时间 | 0 | 以分钟为单位

## stu_vol

这个表存储学生和义工之间的关系

项名 | 类型 | 简述 | 举例 | 其他
-|-|-|-|-
volId | INTERGER | 义工活动的编号 | 1 | 表示`stuID`的学生参加了这个义工活动
stuId | INTERGER | 学生的学号 | 20200101 | 表示这个学生参加了`volId`的义工活动