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
  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn pymysql
  ```
  5. MySQL一系列操作
  ```
  mysql> create user 'zvms'@'127.0.0.1' identified by '123456';
  mysql> grant all on *.* to 'zvms'@'127.0.0.1';
  mysql> ^Z
  D:\MySQL\bin> mysql -h 127.0.0.1 -u zvms -p
  Enter password: ******
  mysql> create database zvms;
  ```
  6. 启动初始化程序
  ```
  python init.py
  ```
  7. 启动程序
  ```
  python bin\main.py
  ```