import database as DB

sql = "SELECT * FROM user WHERE username=%s AND password=%s"
name = '2001'
passwd = 'e10adc3949ba59abbe56e057f20f883e'
DB.execute(sql, (name, passwd))
print(DB.fetchall())