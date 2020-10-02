# INTERFACE

## 发生错误时的返回值

``` json
{
    "type": "ERROR",
    "message": "错误信息"
}
```

## /login

#### input

``` json
{
    "userid": 202001,
    "password": 123456
}
```

#### output

``` json
{
    "type": "SUCCESS",
    "message": "登陆成功",
    "username": "王彳亍",
    "class": 202001,
    "permission": 0
}
```

## /logout

#### output

``` json
{
    "type": "SUCCESS",
    "message": "登出成功！"
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
    "student":[
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
    "volunteer":[
        {"id": 1, "name": "义工活动1", "status": 1, "stuMax": 20},
        {"id": 2, "name": "义工活动2", "status": 1, "stuMax": 2},
        {"id": 3, "name": "义工活动3", "status": 0, "stuMax": 5},
        {"id": 4, "name": "义工活动4", "status": 2, "stuMax": 10}
    ]
}
```

## /volunteer

### /volunteer/\<volId> 一项义工的详细信息

#### output

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
    "class":[
        {"id": 202001, "name": "高一1班"},
        {"id": 202011, "name": "蛟一1班"},
        {"id": 202002, "name": "高一2班"},
        {"id": 201901, "name": "高二1班"},
        {"id": 201801, "name": "高三1班"}
    ]
}
```



