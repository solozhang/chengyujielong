成语接龙小游戏：
    输入第一个成语和最后一个成语
    将这两个成语通过接龙的方式连接起来
    例如，第一个成语：瞒天过海，最后一个成语：身败名裂
    接龙的结果是：
        瞒天过海
        海底捞月
        月下老人
        人百其身
        身败名裂
    

sql文件是成语数据库，倒入前的创建表结构命令：
CREATE TABLE `pre_org_chengyu` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `chengyu` varchar(255) DEFAULT NULL,
  `pinyin` varchar(255) DEFAULT NULL,
  `diangu` text,
  `chuchu` text,
  `lizi` text,
  `spinyin` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `chengyu` (`chengyu`)
) ENGINE=InnoDB AUTO_INCREMENT=13001 DEFAULT CHARSET=utf8
