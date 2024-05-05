-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Quiz
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Frontend_quiz`
--

DROP TABLE IF EXISTS `Frontend_quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Frontend_quiz` (
  `QuestionId` int(11) NOT NULL,
  `Question` varchar(500) NOT NULL,
  `Option1` longtext NOT NULL,
  `Option2` longtext NOT NULL,
  `Option3` longtext NOT NULL,
  `CorrectAnswer` longtext NOT NULL,
  `createdAt` datetime(6) NOT NULL,
  `updatedAt` datetime(6) NOT NULL,
  `Answered` tinyint(1) NOT NULL,
  `Option4` longtext NOT NULL,
  PRIMARY KEY (`QuestionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Frontend_quiz`
--

LOCK TABLES `Frontend_quiz` WRITE;
/*!40000 ALTER TABLE `Frontend_quiz` DISABLE KEYS */;
INSERT INTO `Frontend_quiz` VALUES
(1,'What is a common method used by attackers to gain unauthorized access to a system','Shoulder surfing ','Encryption','Firewall','Phishing','2024-04-29 23:35:17.122961','2024-04-30 03:18:03.349548',0,'Phishing'),
(2,'Which of the following is a strong authentication factor?','Something you know','Something you are','Something you want','Something you are','2024-04-29 23:36:11.843401','2024-04-30 03:18:07.768938',0,'Something you see'),
(3,'What type of malware encrypts files on a victims system and demands payment for decryption?','Trojan horse','Spyware','Ransomware','Ransomware','2024-04-29 23:37:36.305798','2024-04-30 03:18:13.019388',0,'Adware'),
(4,'Which security measure ensures that data is transmitted in such a way that only authorized recipients can access it?','VPN (Virtual Private Network)','DNS (Domain Name System)',' HTTP (Hypertext Transfer Protocol)','VPN (Virtual Private Network)','2024-04-29 23:38:55.558909','2024-04-30 03:18:16.545135',0,'FTP (File Transfer Protocol)'),
(5,'What is the primary purpose of a firewall in a network security infrastructure?','To detect and remove viruses','To filter incoming and outgoing network traffic','To encrypt sensitive data','To filter incoming and outgoing network traffic','2024-04-30 00:12:34.554723','2024-04-30 03:18:21.417911',0,'To monitor system logs'),
(6,'Which of the following best describes a brute force attack?','A type of social engineering attack','An attack that exploits vulnerabilities in software','An attempt to guess passwords or encryption keys through trial and error','An attempt to guess passwords or encryption keys through trial and error','2024-04-30 00:16:55.448270','2024-04-30 03:18:39.234947',0,'A form of malware designed to steal sensitive information'),
(7,'What is the purpose of multi-factor authentication (MFA)?','To simplify the login process','To provide additional layers of security by requiring multiple forms of verification','To encrypt data in transit','To provide additional layers of security by requiring multiple forms of verification','2024-04-30 00:20:48.655998','2024-04-30 03:18:47.152871',0,'To prevent denial of service attacks'),
(8,'Which type of attack involves intercepting communication between two parties and altering the data transmitted?','Man-in-the-middle (MitM) attack','Denial of Service (DoS) attack','Cross-site scripting (XSS) attack','Man-in-the-middle (MitM) attack','2024-04-30 00:21:37.069343','2024-04-30 03:18:50.761030',0,'SQL injection attack'),
(9,'What security measure is designed to protect against unauthorized access to a wireless network?','MAC address filtering','IP address masking','Packet sniffing','MAC address filtering','2024-04-30 00:22:24.105629','2024-04-30 03:18:54.394732',0,'Port scanning'),
(10,'Which of the following is a common method for protecting sensitive information stored on a computer or device?','Encryption','Defragmentation','Overclocking','Encryption','2024-04-30 00:23:04.771201','2024-04-30 03:19:04.050677',0,'Cache clearing');
/*!40000 ALTER TABLE `Frontend_quiz` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-05 10:58:41
