-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `Member_Type` varchar(45) NOT NULL,
  `Registration_No` varchar(45) NOT NULL,
  `ID_No` varchar(45) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Address_Line_1` varchar(60) NOT NULL,
  `Address_Line_2` varchar(60) NOT NULL,
  `Phone_No` varchar(45) NOT NULL,
  `Mobile_No` varchar(45) NOT NULL,
  `Book_Id` varchar(45) NOT NULL,
  `Book_Title` varchar(60) NOT NULL,
  `Author_Name` varchar(45) NOT NULL,
  `Date_of_Borrow` varchar(45) NOT NULL,
  `Due_date` varchar(45) NOT NULL,
  `No_of_days` varchar(45) NOT NULL,
  `Late_fee` varchar(45) NOT NULL,
  `Over_due_Date` varchar(45) NOT NULL,
  `book_price` varchar(45) NOT NULL,
  PRIMARY KEY (`Registration_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `library`
--

LOCK TABLES `library` WRITE;
/*!40000 ALTER TABLE `library` DISABLE KEYS */;
INSERT INTO `library` VALUES ('Admin Staff','R_0001','I_0001','Divyansh','Nigam','Jhansi','Uttar Pradesh','284003','9559108881','B_ID0001','Clean Code','Robert Cecil Martin','16/12/1999','16/01/2000','30','Rs. 50','No','Rs. 1000'),('Student','R_0002','I_0002','Divyansh','Nigam','Jhansi','Uttar Pradesh','284003','9559108881','B_ID0001','Clean Code','Robert Cecil Martin','26/02/2023','28/03/2023','30','Rs. 50','No','Rs. 1000'),('Student','R_0004','I_0004','Divyansh','Nigam','Jhansi','Uttar Pradesh','284003','9559108881','B_ID0001','Clean Code','Robert Cecil Martin','26/02/2023','28/03/2023','30','Rs. 50','No','Rs. 1000');
/*!40000 ALTER TABLE `library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-01  0:06:13
