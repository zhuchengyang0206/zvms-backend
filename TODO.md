# TODO LIST

## /class

### /class/list 读取全部班级列表

#### input

``` json
nothing
```

#### output

##### SUCCESS

``` json
{
    "type":"SUCCESS",
    "message":"获取成功",
    "total":4,
    "class":[
        {"id":202001, "name":"高一1班"},
        {"id":202011, "name":"蛟一1班"},
        {"id":202002, "name":"高一2班"},
        {"id":201901, "name":"高二1班"},
        {"id":201801, "name":"高三1班"}
        //name随年份自动计算
    ]
}
```

##### ERROR

``` json
{
    "type":"ERROR",
    "message":"错误信息"
}
```

### /class/stulist/\<classid> 读取一个班级的全部学生

#### input 

```
/class/stulist/202001
```

#### output

##### SUCCESS
``` json
{
    "type":"SUCCESS",
    "message":"获取成功",
    "total":4,
    "student":[
        {"id":20200101, "name":"王可", "inside":1.5, "outside":2, "large":8},
        {"id":20200102, "name":"王不可", "inside":2.5, "outside":2, "large":8},
        {"id":20200103, "name":"王可以", "inside":5, "outside":8, "large":0},
        {"id":20200104, "name":"王不行", "inside":1, "outside":4, "large":16},
        {"id":20200105, "name":"王彳亍", "inside":5, "outside":0, "large":8}
        // inside表示校内义工，outside表示校外义工，large表示大型活动义工
    ]
}
```
##### ERROR

``` json
{
    "type":"ERROR",
    "message":"错误信息"
}
```
