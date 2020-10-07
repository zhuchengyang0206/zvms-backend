# INTERFACE

## 发生错误时的默认返回值

``` json
{
    "type": "ERROR",
    "message": "错误信息"
}
```

## /login

#### input 1

``` json
{
    "userid": 202001,
    "password": 123456
}
```

#### output 1_1

``` json
{
    "type": "SUCCESS",
    "message": "登陆成功",
    "username": "王彳亍",
    "class": 202001,
    "permission": 0
}
```

#### output 1_2

``` json
{
    "type": "ERROR",
    "message": "用户ID或密码错误！"
}
```

#### output 1_3

``` json
{
    "type": "ERROR",
    "message": "用户重复！请向管理员寻求帮助！"
}
```

## /logout

#### output

``` json
{
    "type": "SUCCESS",
    "message": "登出成功"
}
```

## /student

### /student/volbook/\<stuId>

#### output

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "rec": [
        {"volId": 1, "inside": 0.5, "outside": 0, "large": 0, "status": 1},
        {"volId": 3, "inside": 1.5, "outside": 0, "large": 0, "status": 1},
        {"volId": 5, "inside": 0, "outside": 0, "large": 2, "status": 1},
        {"volId": 6, "inside": 0, "outside": 2, "large": 0, "status": 1},
    ]
}
```

## /class

### /class/list 读取全部班级列表

#### output

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "class": [
        {"id": 202001, "name": "高一1班"},
        {"id": 202011, "name": "蛟一1班"},
        {"id": 202002, "name": "高一2班"},
        {"id": 201901, "name": "高二1班"},
        {"id": 201801, "name": "高三1班"}
        //name随年份自动计算
    ]
}
```

### /class/stulist/\<classid> 读取一个班级的全部学生

#### output

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "student": [
        {"id": 20200101, "name": "王可", "inside": 1.5, "outside": 2, "large": 8},
        {"id": 20200102, "name": "王不可", "inside": 2.5, "outside": 2, "large": 8},
        {"id": 20200103, "name": "王可以", "inside": 5, "outside": 8, "large": 0},
        {"id": 20200104, "name": "王不行", "inside": 1, "outside": 4, "large": 16},
        {"id": 20200105, "name": "王彳亍", "inside": 5, "outside": 0, "large": 8}
        // inside表示校内义工，outside表示校外义工，large表示大型活动义工
    ]
}
```

### /class/volunteer/\<classid> 获取一个班级的义工活动列表

#### output

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "volunteer": [
        {"id": 1, "name": "义工活动1", "time": "2020.10.1" , "description": "打扫新华书店", "status": 1, "stuMax": 20},
        {"id": 2, "name": "义工活动2", "time": "2020.10.2" , "description": "新华书店打扫", "status": 1, "stuMax": 2},
        {"id": 3, "name": "义工活动3", "time": "2020.10.3" , "description": "华新书店打扫", "status": 0, "stuMax": 5},
        {"id": 4, "name": "义工活动4", "time": "2020.10.4" , "description": "打扫华新书店", "status": 2, "stuMax": 10}
    ]
}
```

## /volunteer

### /volunteer/list 义工活动列表

#### output

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "volunteer": [
        {"id": 1, "name": "义工活动1", "description": "新华打扫书店", "time": "2020.10.1" , "status": 1, "stuMax": 20},
        {"id": 2, "name": "义工活动2", "description": "打扫新华书店", "time": "2020.10.2" , "status": 1, "stuMax": 2},
        {"id": 3, "name": "义工活动3", "description": "打新华打新华", "time": "2020.10.3" , "status": 0, "stuMax": 5},
        {"id": 4, "name": "义工活动4", "description": "扫书店扫书店", "time": "2020.10.4" , "status": 2, "stuMax": 10}
    ]
}
```

### /volunteer/\<volId> 一项义工的详细信息及报名入口

#### input 1

``` json
{
    "type": "FETCH"
}
```

#### output 1

``` json
{
    "type": "SUCCESS",
    "message": "获取成功",
    "name": "义工活动1",
    "time": "2020.10.1 13:00~16:00",
    "stuMax": 20,
    "nowStu": 18,
    "description": "新华书店打扫",
    "status": 1,
    "inside": 0,
    "outside": 3,
    "large": 0,
    "class": [
        {"id": 202001, "name": "高一1班"},
        {"id": 202011, "name": "蛟一1班"},
        {"id": 202002, "name": "高一2班"},
        {"id": 201901, "name": "高二1班"},
        {"id": 201801, "name": "高三1班"}
    ]
}
```

#### input 2

``` json
{
    "type": "SIGNUP",
    "stulst": [
        20200101,
        20200102,
        20200103
    ]
    // 注意 这里别忘记后台的session验证，要检验stulst中的人是否都是本班的
}
```

#### output 2_1

``` json
{
    "type": "SUCCESS",
    "message": "报名成功"
}
```

#### output 2_2

```` json
{
    "type": "ERROR",
    "message": "人数超限"
}
````