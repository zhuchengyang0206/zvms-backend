-- Adminer 4.7.6 MySQL dump

SET NAMES utf8;
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `class_vol`;
CREATE TABLE `class_vol` (
  `volId` int(11) DEFAULT NULL,
  `class` int(11) DEFAULT NULL,
  `stuMax` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `stuId` int(11) NOT NULL,
  `stuName` char(64) DEFAULT NULL,
  `volTimeInside` int(11) DEFAULT NULL,
  `volTimeOutside` int(11) DEFAULT NULL,
  `volTimeLarge` int(11) DEFAULT NULL,
  PRIMARY KEY (`stuId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `stu_vol`;
CREATE TABLE `stu_vol` (
  `volId` int(11) DEFAULT NULL,
  `stuId` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `volTimeInside` int(11) DEFAULT NULL,
  `volTimeOutside` int(11) DEFAULT NULL,
  `volTimeLarge` int(11) DEFAULT NULL,
  `thought` TEXT DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `userId` int(11) NOT NULL,
  `userName` char(255) DEFAULT NULL,
  `class` int(11) DEFAULT NULL,
  `permission` smallint(6) DEFAULT NULL,
  `password` char(255) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `volunteer`;
CREATE TABLE `volunteer` (
  `volId` int(11) NOT NULL,
  `volName` char(255) DEFAULT NULL,
  `volDate` date DEFAULT NULL,
  `volTime` time DEFAULT NULL,
  `stuMax` int(11) DEFAULT NULL,
  `nowStuCount` int(11) DEFAULT NULL,
  `description` text,
  `status` smallint(6) DEFAULT NULL,
  `volTimeInside` int(11) DEFAULT NULL,
  `volTimeOutside` int(11) DEFAULT NULL,
  `volTimeLarge` int(11) DEFAULT NULL,
  `holderId` int(11) DEFAULT NULL,
  PRIMARY KEY (`volId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
