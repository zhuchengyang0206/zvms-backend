# zvms-backend

### 介绍：镇海中学义工管理系统后端

* 使用方法：

-----

  1. 启用virtualenv开发环境(Windows)
  ```
  py -3 -m venv venv
  venv\Scripts\activate
  ```
  2. 安装Flask
  ```
  pip install flask
  ```
  Postscript: 如果上一条指令不能使用，请使用下面这一条
  ```
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn flask
  ```
  3. 安装MySQL
  4. 安装MySQLdb
  ```
  pip install MySQLdb
  ```
  5. MySQL中注册用户
  ```
  mysql> CREATE USER zvms BY 123456;
  ```
  6. MySQL中注册数据库
  ```
  mysql> CREATE TABLE zvms;
  ```
  7. 启动初始化程序
  ```
  python init.py
  ```
  8. 启动程序
  ```
  python main.py
  ```