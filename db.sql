USE `sql12676669`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: phongmachdb
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `examination_bill`
--

DROP TABLE IF EXISTS `examination_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examination_bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `examination_date` date DEFAULT NULL,
  `medicine_money` float DEFAULT NULL,
  `examination_money` float DEFAULT NULL,
  `medical_bill_id` int(11) NOT NULL,
  `patient_id` int(11) NOT NULL,
  `paid` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `medical_bill_id` (`medical_bill_id`),
  UNIQUE KEY `medical_bill_id_2` (`medical_bill_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `examination_bill_ibfk_1` FOREIGN KEY (`medical_bill_id`) REFERENCES `medical_bill` (`id`),
  CONSTRAINT `examination_bill_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examination_bill`
--

LOCK TABLES `examination_bill` WRITE;
/*!40000 ALTER TABLE `examination_bill` DISABLE KEYS */;
INSERT INTO `examination_bill` VALUES (1,'2023-12-13',3672,100000,1,3,1),(2,'2023-12-13',13000,100000,2,4,1),(3,'2023-12-13',70500,100000,3,5,1),(4,'2023-12-20',44700,100000,4,6,1),(5,'2023-12-20',6000,100000,5,7,1),(6,'2023-12-20',326800,100000,6,9,1),(7,'2024-01-04',82560,100000,7,4,1),(8,'2024-01-04',576000,100000,8,3,1),(9,'2024-01-04',18800,100000,9,8,1),(10,'2024-01-04',11500,100000,10,5,1),(11,'2023-11-13',90,100000,11,2,1),(12,'2023-11-13',9600,100000,12,11,1),(13,'2023-11-13',8400,100000,13,10,1),(14,'2023-11-13',8400,100000,14,8,1);
/*!40000 ALTER TABLE `examination_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_bill`
--

DROP TABLE IF EXISTS `medical_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `examination_date` date DEFAULT NULL,
  `symptom` text NOT NULL,
  `disease_prediction` text DEFAULT NULL,
  `patient_id` int(11) NOT NULL,
  `doctor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `medical_bill_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `user` (`id`),
  CONSTRAINT `medical_bill_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_bill`
--

LOCK TABLES `medical_bill` WRITE;
/*!40000 ALTER TABLE `medical_bill` DISABLE KEYS */;
INSERT INTO `medical_bill` VALUES (1,'2023-12-13','Ho','Cảm',3,16),(2,'2023-12-13','Ẻ','Đau bụng',4,16),(3,'2023-12-13','Đau mắt','Mắt đỏ',5,16),(4,'2023-12-20','Què','Què',6,16),(5,'2023-12-20','Đau','Mêht',7,16),(6,'2023-12-20','Đau','Đàu',9,16),(7,'2024-01-04','Đau','Đu',4,16),(8,'2024-01-04','Đau','Đau',3,16),(9,'2024-01-04','đau đầu','đau đầu',8,16),(10,'2024-01-04','Đau chân','trật khớp',5,16),(11,'2023-11-13','Đau','Đau',2,16),(12,'2023-11-13','Đau','Đau',11,16),(13,'2023-11-13','Đau','Đau',10,16),(14,'2023-11-13','Đau','Đau',8,16);
/*!40000 ALTER TABLE `medical_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_bill_detail`
--

DROP TABLE IF EXISTS `medical_bill_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_bill_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) DEFAULT NULL,
  `medicine_id` int(11) NOT NULL,
  `medical_bill_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `medicine_id` (`medicine_id`),
  KEY `medical_bill_id` (`medical_bill_id`),
  CONSTRAINT `medical_bill_detail_ibfk_1` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`id`),
  CONSTRAINT `medical_bill_detail_ibfk_2` FOREIGN KEY (`medical_bill_id`) REFERENCES `medical_bill` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_bill_detail`
--

LOCK TABLES `medical_bill_detail` WRITE;
/*!40000 ALTER TABLE `medical_bill_detail` DISABLE KEYS */;
INSERT INTO `medical_bill_detail` VALUES (1,4,10,1),(2,12,14,1),(3,12,17,1),(4,2,15,2),(5,10,17,2),(6,1,4,2),(7,3,11,3),(8,6,27,3),(9,3,15,4),(10,3,27,4),(11,3,28,4),(12,12,17,5),(13,6,29,5),(14,4,16,6),(15,4,27,6),(16,8,29,6),(17,6,21,7),(18,6,25,7),(19,8,15,8),(20,8,16,8),(21,5,25,9),(22,10,30,9),(23,5,1,10),(24,20,7,10),(25,1,10,11),(26,3,15,12),(27,3,17,12),(28,3,13,13),(29,12,8,13),(30,3,28,14),(31,12,29,14);
/*!40000 ALTER TABLE `medical_bill_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `name` varchar(255) NOT NULL,
  `price` float DEFAULT NULL,
  `description` text DEFAULT NULL,
  `direction` text DEFAULT NULL,
  `unit_in_stock` int(11) DEFAULT NULL,
  `unit_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `unit_id` (`unit_id`),
  CONSTRAINT `medicine_ibfk_1` FOREIGN KEY (`unit_id`) REFERENCES `unit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES ('A.T Alugela',1500,'Viêm thực quản, viêm dạ dày cấp và mạn tính, viêm loét dạ dày tá tràng, kích ứng dạ dày, ợ chua, rát bỏng','1-2 gói thuốc, từ 2-3 lần mỗi ngày, uống trước ăn 30 phút.',100,4,1),('A.T Bisoprolol 5',500,'điều trị tăng huyết áp, đau thắt ngực ổn định mạn tính, suy tim mạn tính','Uống thuốc với nhiều nước, nên dùng thuốc vào buổi sáng khi đói hoặc lúc điểm tâm. Không được nhai.',100,3,2),('A.T Furosemid inj',750,'điều trị phù, tăng huyết áp thể nhẹ và trung bình','uống ngay sau khi ăn bữa ăn chính.',100,1,3),('A.T Hydrocortisone',5000,'sử dụng điều trị chống viêm như viêm khớp, lupus, bệnh gout, viêm khớp vảy nến, viêm loét ruột.','Dùng thuốc đường tiêm khi người bệnh không thể tiếp nhận thuốc bằng đường khác.',100,1,4),('A.T Nitroglycerin inj',50000,'Suy tim, nhồi máu cơ tim cấp, phù phổi cấp do tim, đau thắt ngực trầm trọng.','i pha loãng trong dextrose 5% hoặc natri clorid 0,9% trước khi truyền tinh mach.',100,1,5),('A.T Sucralfate',1100,'điều trị viêm loét dạ dày tá tràng.','1g/lần, 4 lần/ngày (uống 1 giờ trước 3 bữa ăn và trước khi đi ngủ)',100,4,6),('Acecyst ',200,'Acecyst thuốc có tác dụng long đờm, được sử dụng để làm thông đường hô hấp','Sử dụng liều 1 viên/ lần, ngày 3 lần.',100,3,7),('Acefalgan',550,'giảm đau và hạ sốt, có tác dụng giảm đau từ nhẹ đến trung bình và hạ sốt.','Uống một viên mỗi 4 đến 6 giờ, nếu bạn cần. Không uống nhiều hơn 4 viên trong bất kỳ 24 giờ nào.',100,3,8),('Adrenalin',2500,'ác dụng kích thích hệ thần kinh giao cảm, kích thích cả thụ thể alpha và thụ thể beta của thần kinh giao cảm','Tiêm dưới da hoặc tiêm bắp từ 0,3-0,5 ml dung dịch tỷ lệ 1:1000, nhắc lại 5 phút một lần tùy theo huyết áp của bệnh nhân.',100,1,9),('Agifuros',90,'làm tăng thải trừ các ion kéo theo nước, tăng lưu lượng máu, tăng độ lọc ở cầu thận','Thuốc Agifuros 40mg được dùng đường uống. Nên uống trọn viên thuốc với một ly nước đầy.',100,2,10),('Bepracid 20',500,'có tác dụng ức chế tiết acid dạ dày trong điều kiện bình thường và trong cả tình trạng kích thích ','20 mg/ lần/ ngày trong 4 – 8 tuần.',100,2,11),('Bicebid 200',1000,'sử dụng trong việc điều trị các bệnh nhiễm khuẩn như: nhiễm khuẩn đường tiết niệu và nhiễm khuẩn đường hô hấp trên - dưới','dùng liều 300mg/ngày',100,2,12),('Bifucil',600,'Bifucil thuộc nhóm thuốc trị ký sinh trùng, chống nhiễm khuẩn, kháng virus và kháng nấm.','Uống 1 viên/ lần, 1 – 2 lần/ngày. Dùng trong 7 - 14 ngày.',100,2,13),('Captagim',76,'Captagim thuộc nhóm thuốc tim mạch, được bào chế dưới dạng viên nén','25mg x 2 - 3 lần/ ngày. Trường hợp bệnh nặng có thể tăng liều Captagim đến 50mg x 3 lần/ ngày;',100,3,14),('Cerecaps',3000,'thuốc điều trị thiếu máu não là một thuốc có nguồn gốc dược liệu, được điều chế ở dạng viên nang cứng','uống 2-3 viên mỗi lần, ngày dùng 2 lần.',100,2,15),('Ciloxan',69000,'Thuốc Ciloxan có dạng bào chế là dung dịch nhỏ mắt.','Trong 6 giờ đầu nhỏ 2 giọt sau mỗi 15 phút, 4 giờ sau thì 2 giọt sau mỗi 30 phút.',100,1,16),('Clanzen',200,'thuốc chống dị ứng',' 5mg/ngày, 2 ngày dùng 1 lần.',100,3,17),('Comegim',365,'thành phần chính là perindopril erbumin, là thuốc điều trị tăng huyết áp.','Thuốc thường được cho uống một lần/ngày vào buổi sáng, lúc đói (trước bữa ăn).',100,3,18),('Daflon',3258,'Thuốc có tác dụng làm giảm sức căng và tình trạng ứ trệ của tĩnh mạch, bảo vệ, làm tăng bền của các mạch máu nhỏ.','uống 1 viên x2 lần/ngày vào các bữa ăn.',100,3,19),('Desloratadin',160,'giúp người bệnh nâng cao hiệu quả điều trị và tránh được những tác dụng phụ không mong muốn.','liều khuyến cáo là 5 mg, 2 ngày uống 1 lần (uống cách ngày).',100,3,20),('Dextrose',13000,'bổ sung glucose cho những đối tượng dễ bị hạ đường huyết như suy dinh dưỡng','sử dụng từ 10- 25g, có thể lặp lại trong trường hợp nghiêm trọng;',100,1,21),('Dimedrol',650,'tác dụng kháng histamin, an thần, chống nôn và chống co thắt','Tiêm bắp hoặc tĩnh mạch, 10 – 50mg/lần.',100,1,22),('Entacron 25',1500,'thuốc được sử dụng trong các bệnh lý như bệnh thận, bệnh gan, bệnh tim gây ra phù, cổ chướng và cũng được dùng phối hợp trong bệnh tăng huyết áp.','Liều ban đầu uống 50- 100 mg/ngày, chia từ 2 đến 4 lần, dùng ít nhất 2 tuần',100,3,23),('Erolin',2500,'Thuốc được sử dụng trong điều trị dị ứng, mày đay,... ','Dùng liều 10mg/ngày, tương đương 1 viên thuốc Erolin 10mg/ngày;',100,2,24),('Expas 40',760,'một loại thuốc chống co thắt được sử dụng để thư giãn các cơ trơn như của đường tiêu hóa','Uống 1-2 viên một lần uống 3 lần/ngày.',100,2,25),('Fefasdin',10500,'thuốc chống dị ứng (thuộc nhóm thuốc kháng Histamin thế hệ 2) thường dùng trong các trường hợp quá mẫn cảm, dị ứng theo mùa, ...','Uống 60mg/lần, ngày chia 2 lần. Nếu dùng Fefasdin 120 hay 180 thì uống 1 viên trong ngày;',100,1,26),('Fenilham',11500,'thuốc giảm đau thuộc nhóm opioid, thường được chỉ định giảm đau trong ung thư, phẫu thuật gây mê và giảm đau sau phẫu thuật.',' 50 – 100 microgam/ lần. Tiêm tĩnh mạch tốc độ chậm.',100,1,27),('Galanmer',400,'huộc nhóm vitamin và khoáng chất, thuốc Galanmer có tác dụng điều trị và phòng ngừa thiếu vitamin B12','1 lần/ viên và uống 3 lần/ ngày.',100,2,28),('Gyoryg',600,'người tăng glucose máu (đặc biệt tăng glucose máu sau khi ăn) không kiểm soát được chỉ bằng chế độ ăn và tập luyện.','Uống acarbose vào đầu bữa ăn để giảm nồng độ glucose máu sau ăn',100,3,29),('Hapacol',1500,'Hapacol được sử dụng phổ biến trong điều trị các triệu chứng thường gặp như sốt cao, đau đầu, mệt mỏi,…','1 viên/lần, nếu người bệnh bị đau nhức nghiêm trọng có thể dùng 2 viên/lần hoặc sử dụng theo chỉ định của bác sĩ.',100,4,30);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine_tag`
--

DROP TABLE IF EXISTS `medicine_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine_tag` (
  `tag_id` int(11) NOT NULL,
  `medicine_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `tag_id` (`tag_id`),
  KEY `medicine_id` (`medicine_id`),
  CONSTRAINT `medicine_tag_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `medicine_tag_ibfk_2` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine_tag`
--

LOCK TABLES `medicine_tag` WRITE;
/*!40000 ALTER TABLE `medicine_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `medicine_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_form`
--

DROP TABLE IF EXISTS `registration_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration_form` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `examination_date` date NOT NULL,
  `accepted` tinyint(4) DEFAULT 0,
  `used` tinyint(4) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `registration_form_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_form`
--

LOCK TABLES `registration_form` WRITE;
/*!40000 ALTER TABLE `registration_form` DISABLE KEYS */;
INSERT INTO `registration_form` VALUES (1,3,'2023-12-13',1,1),(2,4,'2023-12-13',1,1),(3,5,'2023-12-13',1,1),(4,6,'2023-12-20',1,1),(5,7,'2023-12-20',1,1),(6,9,'2023-12-20',1,1),(7,3,'2024-01-04',1,1),(8,4,'2024-01-04',1,1),(9,8,'2024-01-04',1,1),(10,5,'2024-01-04',1,1),(11,2,'2023-11-13',1,1),(12,11,'2023-11-13',1,1),(13,10,'2023-11-13',1,1),(14,8,'2023-11-13',1,1),(15,13,'2024-01-13',1,0),(16,3,'2024-01-13',0,0);
/*!40000 ALTER TABLE `registration_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regulation`
--

DROP TABLE IF EXISTS `regulation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regulation` (
  `key` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `value` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `regulation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regulation`
--

LOCK TABLES `regulation` WRITE;
/*!40000 ALTER TABLE `regulation` DISABLE KEYS */;
INSERT INTO `regulation` VALUES ('user_in_1_day','Số bệnh nhân khám trong 1 ngày',40,1,1),('examination_price','Tiền khám 1 lần',100000,1,2);
/*!40000 ALTER TABLE `regulation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag` (
  `name` varchar(255) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit` (
  `name` varchar(50) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit`
--

LOCK TABLES `unit` WRITE;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` VALUES ('Chai',1),('Vĩ',2),('Viên',3),('Gói',4);
/*!40000 ALTER TABLE `unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `fullname` varchar(255) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `gender` enum('Male','Female') DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `role` enum('Admin','Customer','Nurse','Doctor') DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `username_2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Admin','admin','e10adc3949ba59abbe56e057f20f883e',NULL,'Male','2023-12-22',NULL,'0386904554',1,'2023-12-24 15:11:56','Admin',1),('NguoiKham 0','nguoikham0','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0387073500',1,'2023-12-24 15:11:56','Customer',2),('NguoiKham 1','nguoikham1','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0911111111',1,'2023-12-24 15:11:56','Customer',3),('NguoiKham 2','nguoikham2','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0922222222',1,'2023-12-24 15:11:56','Customer',4),('NguoiKham 3','nguoikham3','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0933333333',1,'2023-12-24 15:11:56','Customer',5),('NguoiKham 4','nguoikham4','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0944444444',1,'2023-12-24 15:11:56','Customer',6),('NguoiKham 5','nguoikham5','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0955555555',1,'2023-12-24 15:11:56','Customer',7),('NguoiKham 6','nguoikham6','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0966666666',1,'2023-12-24 15:11:56','Customer',8),('NguoiKham 7','nguoikham7','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0977777777',1,'2023-12-24 15:11:56','Customer',9),('NguoiKham 8','nguoikham8','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0988888888',1,'2023-12-24 15:11:56','Customer',10),('NguoiKham 9','nguoikham9','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2023-12-24',NULL,'0999999999',1,'2023-12-24 15:11:56','Customer',11),('A','0123456789','e10adc3949ba59abbe56e057f20f883e',NULL,'Male','2024-01-01','khoianh202@gmail.com','0123456789',1,'2024-01-03 20:46:15','Customer',13),('Admin 12345676','0987654321','e10adc3949ba59abbe56e057f20f883e',NULL,'Male','2024-01-01','khoianh202@gmail.com','0987654321',1,'2024-01-05 00:47:02','Customer',14),('Nurse','nurse','e10adc3949ba59abbe56e057f20f883e',NULL,'Female','2024-01-01',NULL,'0000000000',1,'2024-01-05 00:47:02','Nurse',15),('Doctor','doctor','e10adc3949ba59abbe56e057f20f883e',NULL,'Male','2024-01-01',NULL,'0000000001',1,'2024-01-05 00:47:02','Doctor',16);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-13 16:21:23
