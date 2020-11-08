INSERT INTO user(userId, userName, class, permission, password) VALUES (202001, "admin", 202001, 2, "e10adc3949ba59abbe56e057f20f883e");
INSERT INTO student(stuId, stuName, volTimeInside, volTimeOutside, volTimeLarge) VALUES (20200101, "王彳亍", 0, 0, 0);
INSERT INTO volunteer(volId, volName, volDate, volTime, stuMax, nowStuCount, description, status, volTimeInside, volTimeOutside, volTimeLarge, holderId) VALUES (1, "喂孔子+拜锦鲤", "2020.9.24", "13:00", 10, 0, "blablablabla", 0, 1, 0, 0, 202001);
INSERT INTO stu_vol(volId, stuId, status, volTimeInside, volTimeOutside, volTimeLarge) VALUES (1, 20200101, 0, 0, 0, 0);
INSERT INTO class_vol(volId, class, stuMax) VALUES (1, 202001, 10);
