-- MySQL dump 10.13  Distrib 8.4.9, for Linux (x86_64)
--
-- Host: localhost    Database: puutarhakanta2005
-- ------------------------------------------------------
-- Server version	8.4.9

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alkuperaa_koskevat_tiedot`
--

DROP TABLE IF EXISTS `alkuperaa_koskevat_tiedot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Origin-related information
CREATE TABLE `alkuperaa_koskevat_tiedot` (
  `alkupera_nro` int NOT NULL AUTO_INCREMENT,
  `alkuperatyyppi` varchar(255) DEFAULT NULL,
  `maa` varchar(255) DEFAULT NULL,
  `maan_ISOkoodi` varchar(255) DEFAULT NULL,
  `alue` varchar(255) DEFAULT NULL,
  `ala_alue` varchar(255) DEFAULT NULL,
  `kunta` varchar(255) DEFAULT NULL,
  `kyla` varchar(255) DEFAULT NULL,
  `latitude` varchar(255) DEFAULT NULL,
  `longitude` varchar(255) DEFAULT NULL,
  `grid_27_E` varchar(255) DEFAULT NULL,
  `kasvupaikka` varchar(255) DEFAULT NULL,
  `korkeus` varchar(255) DEFAULT NULL,
  `keraaja` varchar(255) DEFAULT NULL,
  `kerayspvm` varchar(255) DEFAULT NULL,
  `keraysnumero` varchar(255) DEFAULT NULL,
  `muita_keraystietoja` text,
  `keraysretki` varchar(255) DEFAULT NULL,
  `hankintaID` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`alkupera_nro`),
  KEY `IDX_Alkuperaa_koskevat_tiedot1` (`hankintaID`),
  CONSTRAINT `alkuperaa_koskevat_tiedot_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=21702 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alkuperainen_kasvupaikka`
--

DROP TABLE IF EXISTS `alkuperainen_kasvupaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Original growing site
CREATE TABLE `alkuperainen_kasvupaikka` (
  `alkuperaisen_kasvupaikan_nro` int NOT NULL AUTO_INCREMENT,
  `alkuperainen_kasvupaikka` varchar(255) DEFAULT NULL,
  `kasvupaikan_tarkenne` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`alkuperaisen_kasvupaikan_nro`),
  KEY `IDX_Alkuperainen_kasvupaikka1` (`taksonin_nro`),
  KEY `IDX_Alkuperainen_kasvupaikka2` (`viitenro`),
  CONSTRAINT `alkuperainen_kasvupaikka_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `alkuperainen_kasvupaikka_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eikaytossa_lista_kaytto`
--

DROP TABLE IF EXISTS `eikaytossa_lista_kaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Obsolete usage list
CREATE TABLE `eikaytossa_lista_kaytto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eikaytossalista_kasvupaikan_tyyppi`
--

DROP TABLE IF EXISTS `eikaytossalista_kasvupaikan_tyyppi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Obsolete growing site type list
CREATE TABLE `eikaytossalista_kasvupaikan_tyyppi` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eikaytossalista_kaytto`
--

DROP TABLE IF EXISTS `eikaytossalista_kaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Obsolete usage list (duplicate)
CREATE TABLE `eikaytossalista_kaytto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eikaytossalista_lahettaja`
--

DROP TABLE IF EXISTS `eikaytossalista_lahettaja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Obsolete sender/source list
CREATE TABLE `eikaytossalista_lahettaja` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eikaytossalista_viljelykasvit`
--

DROP TABLE IF EXISTS `eikaytossalista_viljelykasvit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Obsolete cultivated plants list
CREATE TABLE `eikaytossalista_viljelykasvit` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hankintanumero`
--

DROP TABLE IF EXISTS `hankintanumero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Acquisition number
CREATE TABLE `hankintanumero` (
  `uusin_hankintanumero` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`uusin_hankintanumero`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hankintatiedot`
--

DROP TABLE IF EXISTS `hankintatiedot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Acquisition data
CREATE TABLE `hankintatiedot` (
  `hankintaID` int NOT NULL AUTO_INCREMENT,
  `hankintanumero` varchar(255) DEFAULT NULL,
  `saapumispvm` varchar(255) DEFAULT NULL,
  `hankintanimi` varchar(255) DEFAULT NULL,
  `millaisena_saatu` varchar(255) DEFAULT NULL,
  `erikoiskokoelma_oma_puutarha` varchar(255) DEFAULT NULL,
  `materiaalin_arvo` varchar(255) DEFAULT NULL,
  `lisatiedot` varchar(255) DEFAULT NULL,
  `jarjestysnro` varchar(255) DEFAULT NULL,
  `vuosi` varchar(255) DEFAULT NULL,
  `lisaysPVM` varchar(255) DEFAULT NULL,
  `lisayshistoria` text,
  `kasvin_huomautuksia` text,
  `hankintahistoria` text,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `lahettajanro` int NOT NULL DEFAULT '0',
  `put` tinyint(1) DEFAULT NULL,
  `puttia` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `vuosiluku` int DEFAULT NULL,
  `heimo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`hankintaID`),
  UNIQUE KEY `hankintanumero` (`hankintanumero`),
  KEY `IDX_Hankintatiedot1` (`taksonin_nro`),
  KEY `IDX_Hankintatiedot2` (`lahettajanro`),
  CONSTRAINT `hankintatiedot_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `hankintatiedot_ibfk_2` FOREIGN KEY (`lahettajanro`) REFERENCES `lahettaja` (`lahettajanro`)
) ENGINE=InnoDB AUTO_INCREMENT=57887 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `heimo`
--

DROP TABLE IF EXISTS `heimo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Taxonomic family
CREATE TABLE `heimo` (
  `jarjestysnumero` int NOT NULL DEFAULT '0',
  `nimi` varchar(255) DEFAULT NULL,
  `synonyymi` varchar(255) DEFAULT NULL,
  `numero` varchar(255) DEFAULT NULL,
  `lahko` varchar(255) DEFAULT NULL,
  `lahkonnumero` varchar(255) DEFAULT NULL,
  `alaluokka` varchar(255) DEFAULT NULL,
  `alaluokannumero` varchar(255) DEFAULT NULL,
  `luokka` varchar(255) DEFAULT NULL,
  `luokannumero` varchar(255) DEFAULT NULL,
  `paaryhma` varchar(255) DEFAULT NULL,
  `paaryhmannumero` varchar(255) DEFAULT NULL,
  `suom_nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`jarjestysnumero`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `huomioita`
--

DROP TABLE IF EXISTS `huomioita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Notes/Remarks
CREATE TABLE `huomioita` (
  `paneeli` varchar(255) NOT NULL DEFAULT '',
  `huom` text,
  PRIMARY KEY (`paneeli`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `huomoita`
--

DROP TABLE IF EXISTS `huomoita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Notes (typo variant)
CREATE TABLE `huomoita` (
  `paneeli` varchar(255) NOT NULL DEFAULT '',
  `huom` text,
  PRIMARY KEY (`paneeli`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hyotykaytto`
--

DROP TABLE IF EXISTS `hyotykaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Utility use (obsolete)
CREATE TABLE `hyotykaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `kansainvaliset_sopimukset`
--

DROP TABLE IF EXISTS `kansainvaliset_sopimukset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- International agreements
CREATE TABLE `kansainvaliset_sopimukset` (
  `sopimus_id` int NOT NULL AUTO_INCREMENT,
  `Sopimuksen_nimi` varchar(255) DEFAULT NULL,
  `selite` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`sopimus_id`),
  KEY `IDX_Kansainvaliset_Sopimukset1` (`taksonin_nro`),
  KEY `IDX_Kansainvaliset_Sopimukset2` (`viitenro`),
  CONSTRAINT `kansainvaliset_sopimukset_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `kansainvaliset_sopimukset_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `kasvatustietoja`
--

DROP TABLE IF EXISTS `kasvatustietoja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Cultivation records
CREATE TABLE `kasvatustietoja` (
  `lisatietojen_nro_kasvatus` int NOT NULL AUTO_INCREMENT,
  `siemenpankki` varchar(255) DEFAULT NULL,
  `siemenia_jaljella` varchar(255) DEFAULT NULL,
  `siementen_varastoimistapa` varchar(255) DEFAULT NULL,
  `tutkimus` varchar(255) DEFAULT NULL,
  `huomautuksia` text,
  `hankintaID` int NOT NULL DEFAULT '0',
  `pvm` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`lisatietojen_nro_kasvatus`),
  KEY `IDX_Kasvatustietoja1` (`hankintaID`),
  CONSTRAINT `kasvatustietoja_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=57591 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `kasvin_kayttotarkoitus`
--

DROP TABLE IF EXISTS `kasvin_kayttotarkoitus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Plant usage purpose
CREATE TABLE `kasvin_kayttotarkoitus` (
  `kayttonro` int NOT NULL AUTO_INCREMENT,
  `kayton_tunnus` varchar(255) DEFAULT NULL,
  `kaytto` varchar(255) DEFAULT NULL,
  `selite` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`kayttonro`),
  KEY `IDX_Kasvin_kayttotarkoitus1` (`taksonin_nro`),
  KEY `IDX_Kasvin_kayttotarkoitus2` (`viitenro`),
  CONSTRAINT `kasvin_kayttotarkoitus_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `kasvin_kayttotarkoitus_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=2211 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `kayttajatiedot`
--

DROP TABLE IF EXISTS `kayttajatiedot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- User data
CREATE TABLE `kayttajatiedot` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kayttajan_tunnus` varchar(100) DEFAULT NULL,
  `kayttajan_nimi` varchar(255) DEFAULT NULL,
  `kayttajan_taso` int DEFAULT NULL,
  `lisatietoja` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `kayttajan_tunnus` (`kayttajan_tunnus`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `kayttotarkoitus`
--

DROP TABLE IF EXISTS `kayttotarkoitus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Usage purpose (obsolete)
CREATE TABLE `kayttotarkoitus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `koe`
--

DROP TABLE IF EXISTS `koe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Experimental/test table
CREATE TABLE `koe` (
  `id` int NOT NULL AUTO_INCREMENT,
  `i` int DEFAULT NULL,
  `t` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `koristekaytto`
--

DROP TABLE IF EXISTS `koristekaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Ornamental use (obsolete)
CREATE TABLE `koristekaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `laakekaytto`
--

DROP TABLE IF EXISTS `laakekaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Medicinal use (obsolete)
CREATE TABLE `laakekaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lahettaja`
--

DROP TABLE IF EXISTS `lahettaja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Sender/source
CREATE TABLE `lahettaja` (
  `lahettajanro` int NOT NULL AUTO_INCREMENT,
  `lahettajatyyppi` varchar(255) DEFAULT NULL,
  `lahettajan_tunnus_puutarha` varchar(255) DEFAULT NULL,
  `lahettajan_tunnus_kansainvalinen` varchar(255) DEFAULT NULL,
  `lahettajan_nimi` varchar(255) DEFAULT NULL,
  `lahiosoite` varchar(255) DEFAULT NULL,
  `postilokero` varchar(255) DEFAULT NULL,
  `postinumero` varchar(255) DEFAULT NULL,
  `postitoimipaikka` varchar(255) DEFAULT NULL,
  `kaupunki` varchar(255) DEFAULT NULL,
  `osavaltio` varchar(255) DEFAULT NULL,
  `maa` varchar(255) DEFAULT NULL,
  `kontaktihenkilo` varchar(255) DEFAULT NULL,
  `e_mail` varchar(255) DEFAULT NULL,
  `web_sivut` varchar(255) DEFAULT NULL,
  `osoitteen_kirjauspvm` varchar(255) DEFAULT NULL,
  `Rion_sopimus` varchar(255) DEFAULT NULL,
  `lahettajan_lisatiedot` varchar(255) DEFAULT NULL,
  `hakunimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`lahettajanro`)
) ENGINE=InnoDB AUTO_INCREMENT=745 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_alkuperainen_kasvupaikka`
--

DROP TABLE IF EXISTS `lista_alkuperainen_kasvupaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Original growing site list
CREATE TABLE `lista_alkuperainen_kasvupaikka` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_alkuperainen_levinneisyys`
--

DROP TABLE IF EXISTS `lista_alkuperainen_levinneisyys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Original distribution list
CREATE TABLE `lista_alkuperainen_levinneisyys` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `LYHENNE` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_alkuperainen_vai_tulokas`
--

DROP TABLE IF EXISTS `lista_alkuperainen_vai_tulokas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Native or introduced plant list
CREATE TABLE `lista_alkuperainen_vai_tulokas` (
  `nimi` varchar(100) DEFAULT NULL,
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_alkuperatyyppi`
--

DROP TABLE IF EXISTS `lista_alkuperatyyppi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Origin type list
CREATE TABLE `lista_alkuperatyyppi` (
  `nimi` varchar(255) NOT NULL DEFAULT '',
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_ei_kesta_seuraavia_torjunta_aineita`
--

DROP TABLE IF EXISTS `lista_ei_kesta_seuraavia_torjunta_aineita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Cannot tolerate following pesticides list
CREATE TABLE `lista_ei_kesta_seuraavia_torjunta_aineita` (
  `id` int NOT NULL AUTO_INCREMENT,
  `koodi` varchar(100) DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_haku`
--

DROP TABLE IF EXISTS `lista_haku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Search list
CREATE TABLE `lista_haku` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_hyotykaytto`
--

DROP TABLE IF EXISTS `lista_hyotykaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Utility use list
CREATE TABLE `lista_hyotykaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_ilmastonkestavyys`
--

DROP TABLE IF EXISTS `lista_ilmastonkestavyys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Climate hardiness list
CREATE TABLE `lista_ilmastonkestavyys` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_isokoodi`
--

DROP TABLE IF EXISTS `lista_isokoodi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- ISO code list
CREATE TABLE `lista_isokoodi` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kasvinsaapuminen`
--

DROP TABLE IF EXISTS `lista_kasvinsaapuminen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Plant arrival list
CREATE TABLE `lista_kasvinsaapuminen` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kasvumuoto`
--

DROP TABLE IF EXISTS `lista_kasvumuoto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Growth form list
CREATE TABLE `lista_kasvumuoto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kasvupaikka_suomessa`
--

DROP TABLE IF EXISTS `lista_kasvupaikka_suomessa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Growing site in Finland list
CREATE TABLE `lista_kasvupaikka_suomessa` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kayttotarkoitus`
--

DROP TABLE IF EXISTS `lista_kayttotarkoitus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Usage purpose list
CREATE TABLE `lista_kayttotarkoitus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kestaa_seuraavia_torjunta_aineita`
--

DROP TABLE IF EXISTS `lista_kestaa_seuraavia_torjunta_aineita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Tolerates following pesticides list
CREATE TABLE `lista_kestaa_seuraavia_torjunta_aineita` (
  `id` int NOT NULL AUTO_INCREMENT,
  `koodi` varchar(100) DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_kieli`
--

DROP TABLE IF EXISTS `lista_kieli`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Language list
CREATE TABLE `lista_kieli` (
  `nimi` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_koristekaytto`
--

DROP TABLE IF EXISTS `lista_koristekaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Ornamental use list
CREATE TABLE `lista_koristekaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_laakekaytto`
--

DROP TABLE IF EXISTS `lista_laakekaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Medicinal use list
CREATE TABLE `lista_laakekaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_lahettajantyyppi`
--

DROP TABLE IF EXISTS `lista_lahettajantyyppi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Sender/source type list
CREATE TABLE `lista_lahettajantyyppi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_levinneisyysalue_maailmalla`
--

DROP TABLE IF EXISTS `lista_levinneisyysalue_maailmalla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- World distribution area list
CREATE TABLE `lista_levinneisyysalue_maailmalla` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `LYHENNE` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_lisaystapa`
--

DROP TABLE IF EXISTS `lista_lisaystapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Addition method list
CREATE TABLE `lista_lisaystapa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `koodi` varchar(100) DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_luonnonsuojeluarvo_muualla`
--

DROP TABLE IF EXISTS `lista_luonnonsuojeluarvo_muualla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Nature conservation value elsewhere list
CREATE TABLE `lista_luonnonsuojeluarvo_muualla` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_luonnonsuojeluarvo_suomessa`
--

DROP TABLE IF EXISTS `lista_luonnonsuojeluarvo_suomessa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Nature conservation value in Finland list
CREATE TABLE `lista_luonnonsuojeluarvo_suomessa` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_luonnonvarainen_levinneisyys`
--

DROP TABLE IF EXISTS `lista_luonnonvarainen_levinneisyys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Wild distribution list
CREATE TABLE `lista_luonnonvarainen_levinneisyys` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `LYHENNE` varchar(100) DEFAULT NULL,
  `NUMEROKOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_maarittaja`
--

DROP TABLE IF EXISTS `lista_maarittaja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Determiner/identifier list
CREATE TABLE `lista_maarittaja` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_maaritysmerkinta`
--

DROP TABLE IF EXISTS `lista_maaritysmerkinta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Identification mark list
CREATE TABLE `lista_maaritysmerkinta` (
  `nimi` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_millaisenasaatu`
--

DROP TABLE IF EXISTS `lista_millaisenasaatu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Acquisition method list
CREATE TABLE `lista_millaisenasaatu` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_naytteensijainti`
--

DROP TABLE IF EXISTS `lista_naytteensijainti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Specimen location list
CREATE TABLE `lista_naytteensijainti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `koodi` varchar(255) DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_naytteentyyppi`
--

DROP TABLE IF EXISTS `lista_naytteentyyppi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Specimen type list
CREATE TABLE `lista_naytteentyyppi` (
  `nimi` varchar(255) DEFAULT NULL,
  `koodi` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_neuvoisuus_kotisuus`
--

DROP TABLE IF EXISTS `lista_neuvoisuus_kotisuus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Advice/housekeeping list
CREATE TABLE `lista_neuvoisuus_kotisuus` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_osasto`
--

DROP TABLE IF EXISTS `lista_osasto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Section/department list
CREATE TABLE `lista_osasto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=312 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_polytystapa`
--

DROP TABLE IF EXISTS `lista_polytystapa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Shading method list
CREATE TABLE `lista_polytystapa` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_puutarhanerikoiskokoelma`
--

DROP TABLE IF EXISTS `lista_puutarhanerikoiskokoelma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Botanical garden special collection list
CREATE TABLE `lista_puutarhanerikoiskokoelma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_puutarhanomakokoelma`
--

DROP TABLE IF EXISTS `lista_puutarhanomakokoelma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Botanical garden collection list
CREATE TABLE `lista_puutarhanomakokoelma` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_rauhoitukset`
--

DROP TABLE IF EXISTS `lista_rauhoitukset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Protected status list
CREATE TABLE `lista_rauhoitukset` (
  `nimi` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_siemenia_jaljella`
--

DROP TABLE IF EXISTS `lista_siemenia_jaljella`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Seeds remaining list
CREATE TABLE `lista_siemenia_jaljella` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_sopimukset`
--

DROP TABLE IF EXISTS `lista_sopimukset`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Agreements list
CREATE TABLE `lista_sopimukset` (
  `nimi` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_status`
--

DROP TABLE IF EXISTS `lista_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Status list
CREATE TABLE `lista_status` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_tarkastaja`
--

DROP TABLE IF EXISTS `lista_tarkastaja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Inspector list
CREATE TABLE `lista_tarkastaja` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_tarkastajanimi`
--

DROP TABLE IF EXISTS `lista_tarkastajanimi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Inspector name list
CREATE TABLE `lista_tarkastajanimi` (
  `id` int DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_tuulenkestavyys`
--

DROP TABLE IF EXISTS `lista_tuulenkestavyys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Wind hardiness list
CREATE TABLE `lista_tuulenkestavyys` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_varsi`
--

DROP TABLE IF EXISTS `lista_varsi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Stem/trunk list
CREATE TABLE `lista_varsi` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_viherrakentamiskaytto`
--

DROP TABLE IF EXISTS `lista_viherrakentamiskaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Green space/landscaping use list
CREATE TABLE `lista_viherrakentamiskaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_viljelyn_tarkoitus`
--

DROP TABLE IF EXISTS `lista_viljelyn_tarkoitus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Cultivation purpose list
CREATE TABLE `lista_viljelyn_tarkoitus` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista_ymparistoindikaattoriluonne`
--

DROP TABLE IF EXISTS `lista_ymparistoindikaattoriluonne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Environmental indicator characteristic list
CREATE TABLE `lista_ymparistoindikaattoriluonne` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `NUMERO` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lukitut_taulut`
--

DROP TABLE IF EXISTS `lukitut_taulut`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Locked tables
CREATE TABLE `lukitut_taulut` (
  `kayttajan_tunnus` varchar(100) NOT NULL DEFAULT '',
  `taulun_nimi` varchar(100) DEFAULT NULL,
  `avainkentta` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`kayttajan_tunnus`),
  UNIQUE KEY `avainkentta` (`avainkentta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `maailman_levinneisyysalue`
--

DROP TABLE IF EXISTS `maailman_levinneisyysalue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- World distribution area
CREATE TABLE `maailman_levinneisyysalue` (
  `levinneisyysalueen_nro` int NOT NULL AUTO_INCREMENT,
  `levinneisyysalue` varchar(255) DEFAULT NULL,
  `levinneisyysalueen_tarkenne` varchar(255) DEFAULT NULL,
  `alkuperainen_vai_tulokas` varchar(255) DEFAULT NULL,
  `viitenro` int DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `lisatietoja` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`levinneisyysalueen_nro`),
  KEY `IDX_Maailman_Levinneisyysalue1` (`taksonin_nro`),
  CONSTRAINT `maailman_levinneisyysalue_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`)
) ENGINE=InnoDB AUTO_INCREMENT=4531 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `maaritysmerkinta`
--

DROP TABLE IF EXISTS `maaritysmerkinta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Identification mark
CREATE TABLE `maaritysmerkinta` (
  `maaritysnro` int NOT NULL AUTO_INCREMENT,
  `maarityspvm` varchar(255) DEFAULT NULL,
  `maarittaja` varchar(255) DEFAULT NULL,
  `maaritystaso` varchar(255) DEFAULT NULL,
  `huomautus` varchar(255) DEFAULT NULL,
  `hankintaID` int DEFAULT NULL,
  `osasto` varchar(255) DEFAULT NULL,
  `paikka` varchar(255) DEFAULT NULL,
  `vanhataksoni` varchar(255) DEFAULT NULL,
  `uusitaksoni` varchar(255) DEFAULT NULL,
  `uus_maarityspvm` date DEFAULT NULL,
  PRIMARY KEY (`maaritysnro`),
  KEY `IDX_Maaritysmerkinta1` (`hankintaID`),
  CONSTRAINT `maaritysmerkinta_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=238 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `muunkielinen_nimi`
--

DROP TABLE IF EXISTS `muunkielinen_nimi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Foreign-language name
CREATE TABLE `muunkielinen_nimi` (
  `nimen_nro` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  `kieli` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  `viite_2` int DEFAULT NULL,
  PRIMARY KEY (`nimen_nro`),
  KEY `IDX_Muunkielinen_nimi1` (`taksonin_nro`),
  KEY `IDX_Muunkielinen_nimi2` (`viitenro`),
  CONSTRAINT `muunkielinen_nimi_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `muunkielinen_nimi_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=7327 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `naytetieto`
--

DROP TABLE IF EXISTS `naytetieto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Specimen data
CREATE TABLE `naytetieto` (
  `naytteen_nro` int NOT NULL AUTO_INCREMENT,
  `tyyppi` varchar(255) DEFAULT NULL,
  `sijainti` varchar(255) DEFAULT NULL,
  `tiedot` text,
  `keraaja` varchar(255) DEFAULT NULL,
  `paivays` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  `sijainnin_selite` varchar(255) DEFAULT NULL,
  `viitteen_selite` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`naytteen_nro`),
  KEY `IDX_Naytetieto1` (`taksonin_nro`),
  KEY `IDX_Naytetieto2` (`viitenro`),
  CONSTRAINT `naytetieto_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `naytetieto_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `naytetietoja`
--

DROP TABLE IF EXISTS `naytetietoja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Specimen information
CREATE TABLE `naytetietoja` (
  `naytteen_nro` int NOT NULL AUTO_INCREMENT,
  `naytteen_tyyppi` varchar(255) DEFAULT NULL,
  `naytteen_sijainti` varchar(255) DEFAULT NULL,
  `naytteen_tiedot` text,
  `naytteen_keraaja` varchar(255) DEFAULT NULL,
  `naytteen_paivays` varchar(255) DEFAULT NULL,
  `hankintaID` int DEFAULT NULL,
  `sijainnin_selite` varchar(255) DEFAULT NULL,
  `viitenro` int DEFAULT NULL,
  `viitteen_selite` varchar(255) DEFAULT NULL,
  `uus_naytteen_paivays` date DEFAULT NULL,
  PRIMARY KEY (`naytteen_nro`),
  KEY `IDX_Naytetietoja1` (`hankintaID`),
  CONSTRAINT `naytetietoja_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=132 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `osastopaikka`
--

DROP TABLE IF EXISTS `osastopaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Section location
CREATE TABLE `osastopaikka` (
  `osaston_numero` int NOT NULL AUTO_INCREMENT,
  `osaston_koodi` varchar(255) DEFAULT NULL,
  `osaston_nimi` varchar(255) DEFAULT NULL,
  `kasvin_status` varchar(255) DEFAULT NULL,
  `kasvin_huomautuksia` text,
  `hankintaID` int DEFAULT NULL,
  PRIMARY KEY (`osaston_numero`),
  KEY `IDX_Osastopaikka1` (`hankintaID`),
  CONSTRAINT `osastopaikka_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=90778 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `puutarhassa_viljelyn_tarkoitus`
--

DROP TABLE IF EXISTS `puutarhassa_viljelyn_tarkoitus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Garden cultivation purpose
CREATE TABLE `puutarhassa_viljelyn_tarkoitus` (
  `viljely_nro` int NOT NULL AUTO_INCREMENT,
  `puutarhassa_viljelyn_tarkoitus` varchar(255) DEFAULT NULL,
  `puutarhassa_viljelyn_tarkenne` varchar(255) DEFAULT NULL,
  `hankintaID` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`viljely_nro`),
  KEY `IDX_Puutarhassa_viljelyn_tarkoitus1` (`hankintaID`),
  CONSTRAINT `puutarhassa_viljelyn_tarkoitus_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=667 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sijoituspaikka`
--

DROP TABLE IF EXISTS `sijoituspaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Placement location
CREATE TABLE `sijoituspaikka` (
  `sijoituspaikan_nro` int NOT NULL AUTO_INCREMENT,
  `sijoituspvm` varchar(255) DEFAULT NULL,
  `ruutu` varchar(255) DEFAULT NULL,
  `sijoituspaikan_nimi` varchar(255) DEFAULT NULL,
  `kasvin_status` varchar(255) DEFAULT NULL,
  `sijoituspaikan_koordinaatit` varchar(255) DEFAULT NULL,
  `sijoituspaikka_vanhat_tiedot` varchar(255) DEFAULT NULL,
  `kasvin_huomautuksia` text,
  `osaston_numero` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`sijoituspaikan_nro`),
  KEY `IDX_Sijoituspaikka1` (`osaston_numero`),
  CONSTRAINT `sijoituspaikka_ibfk_1` FOREIGN KEY (`osaston_numero`) REFERENCES `osastopaikka` (`osaston_numero`)
) ENGINE=InnoDB AUTO_INCREMENT=141919 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `suomalainen_kasvupaikka`
--

DROP TABLE IF EXISTS `suomalainen_kasvupaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Growing site in Finland
CREATE TABLE `suomalainen_kasvupaikka` (
  `suomalaisen_kasvupaikan_nro` int NOT NULL AUTO_INCREMENT,
  `kasvupaikka` varchar(255) DEFAULT NULL,
  `kasvupaikan_tyyppi` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`suomalaisen_kasvupaikan_nro`),
  KEY `IDX_Suomalainen_kasvupaikka1` (`taksonin_nro`),
  KEY `IDX_Suomalainen_kasvupaikka2` (`viitenro`),
  CONSTRAINT `suomalainen_kasvupaikka_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `suomalainen_kasvupaikka_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `suomalainen_levinneisyysalue`
--

DROP TABLE IF EXISTS `suomalainen_levinneisyysalue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Distribution area in Finland
CREATE TABLE `suomalainen_levinneisyysalue` (
  `levinneisyysalueen_nro` int NOT NULL AUTO_INCREMENT,
  `levinneisyysalue` varchar(255) DEFAULT NULL,
  `levinneisyysalueen_tarkenne` varchar(255) DEFAULT NULL,
  `alkuperainen_vai_tulokas` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`levinneisyysalueen_nro`),
  KEY `IDX_Suomalainen_Levinneisyysalue1` (`taksonin_nro`),
  KEY `IDX_Suomalainen_Levinneisyysalue2` (`viitenro`),
  CONSTRAINT `suomalainen_levinneisyysalue_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `suomalainen_levinneisyysalue_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=14462 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `suunniteltu_kasvupaikka`
--

DROP TABLE IF EXISTS `suunniteltu_kasvupaikka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Planned growing site
CREATE TABLE `suunniteltu_kasvupaikka` (
  `kasvupaikan_nro` int NOT NULL AUTO_INCREMENT,
  `osasto` varchar(255) DEFAULT NULL,
  `sijoituspaikka` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`kasvupaikan_nro`),
  KEY `IDX_Suunniteltu_kasvupaikka1` (`taksonin_nro`),
  CONSTRAINT `suunniteltu_kasvupaikka_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `synonyymi`
--

DROP TABLE IF EXISTS `synonyymi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Synonym
CREATE TABLE `synonyymi` (
  `synonyymin_nro` int NOT NULL AUTO_INCREMENT,
  `nimi` varchar(255) DEFAULT NULL,
  `auktori` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  `viite_2` int DEFAULT NULL,
  PRIMARY KEY (`synonyymin_nro`),
  KEY `IDX_Synonyymi1` (`taksonin_nro`),
  KEY `IDX_Synonyymi2` (`viitenro`),
  CONSTRAINT `synonyymi_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `synonyymi_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=1779 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `taksoni`
--

DROP TABLE IF EXISTS `taksoni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Taxon (plant species/variety)
CREATE TABLE `taksoni` (
  `taksonin_nro` int NOT NULL AUTO_INCREMENT,
  `tieteellinen_nimi` varchar(255) NOT NULL DEFAULT '',
  `suku` varchar(255) DEFAULT NULL,
  `suvun_auktori` varchar(255) DEFAULT NULL,
  `laji` varchar(255) DEFAULT NULL,
  `lajin_auktori` varchar(255) DEFAULT NULL,
  `alataso_1` varchar(255) DEFAULT NULL,
  `alatason_1_viite` int DEFAULT NULL,
  `alataso_2` varchar(255) DEFAULT NULL,
  `alatason_2_auktori` varchar(255) DEFAULT NULL,
  `alatason_1_auktori` varchar(255) DEFAULT NULL,
  `alatason_2_viite` int DEFAULT NULL,
  `alataso_3` varchar(255) DEFAULT NULL,
  `alatason_3_auktori` varchar(255) DEFAULT NULL,
  `alatason_3_viite` int DEFAULT NULL,
  `alataso_4` varchar(255) DEFAULT NULL,
  `alatason_4_auktori` varchar(255) DEFAULT NULL,
  `alatason_4_viite` int DEFAULT NULL,
  `alataso_5` varchar(255) DEFAULT NULL,
  `alatason_5_auktori` varchar(255) DEFAULT NULL,
  `alatason_5_viite` int DEFAULT NULL,
  `risteymatiedot` varchar(255) DEFAULT NULL,
  `risteymatietojen_auktori` varchar(255) DEFAULT NULL,
  `viimeinen_paivityspvm` varchar(255) DEFAULT NULL,
  `muita_tietoja` text,
  `jarjestysnumero` int DEFAULT NULL,
  `viitenro` int DEFAULT NULL,
  `lajin_viite` varchar(255) DEFAULT NULL,
  `lajin_viite2` varchar(255) DEFAULT NULL,
  `yleis_viite` varchar(255) DEFAULT NULL,
  `vap_yleis_viite` varchar(255) DEFAULT NULL,
  `put` tinyint(1) DEFAULT NULL,
  `puttia` varchar(255) DEFAULT NULL,
  `risteymaviite` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`taksonin_nro`),
  KEY `IDX_Taksoni1` (`jarjestysnumero`),
  KEY `IDX_Taksoni2` (`viitenro`),
  CONSTRAINT `taksoni_ibfk_1` FOREIGN KEY (`jarjestysnumero`) REFERENCES `heimo` (`jarjestysnumero`),
  CONSTRAINT `taksoni_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=11781 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `taksonin_lappu`
--

DROP TABLE IF EXISTS `taksonin_lappu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Taxon label/tag
CREATE TABLE `taksonin_lappu` (
  `Lappu_nro` int NOT NULL AUTO_INCREMENT,
  `Lappu_teksti` text,
  `taksonin_nro` int DEFAULT NULL,
  PRIMARY KEY (`Lappu_nro`),
  KEY `IDX_Taksonin_lappu1` (`taksonin_nro`),
  CONSTRAINT `taksonin_lappu_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`)
) ENGINE=InnoDB AUTO_INCREMENT=7324 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `taksonin_viljelytiedot`
--

DROP TABLE IF EXISTS `taksonin_viljelytiedot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Taxon cultivation data
CREATE TABLE `taksonin_viljelytiedot` (
  `lisatietojen_nro_viljely` int NOT NULL AUTO_INCREMENT,
  `kasvitaudit_ja_tuholaiset` varchar(255) DEFAULT NULL,
  `kestaa_seuraavia_torjuntaaineita` varchar(255) DEFAULT NULL,
  `ei_kesta_seuraavia_torjunta_aineita` varchar(255) DEFAULT NULL,
  `erityisia_kasvualustavaatimuksia` varchar(255) DEFAULT NULL,
  `erityisia_valovaatimuksia` varchar(255) DEFAULT NULL,
  `erityisia_lampotila_tai_talvehtimisvaatimuksia` varchar(255) DEFAULT NULL,
  `lisaystapa` varchar(255) DEFAULT NULL,
  `siementen_keruu` varchar(255) DEFAULT NULL,
  `siementen_sailytys` varchar(255) DEFAULT NULL,
  `tuulenkestavyys` varchar(255) DEFAULT NULL,
  `ilmastollinen_kestavyys` varchar(255) DEFAULT NULL,
  `viljelykasvien_ilmastollinen_kestavyys` varchar(255) DEFAULT NULL,
  `varsi` varchar(255) DEFAULT NULL,
  `kasvumuoto` varchar(255) DEFAULT NULL,
  `kasvutapa` varchar(255) DEFAULT NULL,
  `korkeus` varchar(255) DEFAULT NULL,
  `polytystapa` varchar(255) DEFAULT NULL,
  `neuvoisuus_ja_kotisuus` varchar(255) DEFAULT NULL,
  `muita_viljelytietoja` text,
  `rauhoitus` varchar(255) DEFAULT NULL,
  `uhanalaisuusluokka_suomessa` varchar(255) DEFAULT NULL,
  `uhanalaisuusluokka_maailmalla` varchar(255) DEFAULT NULL,
  `muita_ominaisuuksia` text,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `haitallisuus` varchar(255) DEFAULT NULL,
  `myrkyllisyys` varchar(255) DEFAULT NULL,
  `sopimukset` varchar(255) DEFAULT NULL,
  `vapaa_viite` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`lisatietojen_nro_viljely`),
  KEY `IDX_Taksonin_viljelytiedot1` (`taksonin_nro`),
  CONSTRAINT `taksonin_viljelytiedot_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`)
) ENGINE=InnoDB AUTO_INCREMENT=11419 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tarkastajanimi_lista`
--

DROP TABLE IF EXISTS `tarkastajanimi_lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Inspector name list
CREATE TABLE `tarkastajanimi_lista` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lyhenne` varchar(10) DEFAULT NULL,
  `nimi` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tarkastusmerkinta`
--

DROP TABLE IF EXISTS `tarkastusmerkinta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Inspection mark/record
CREATE TABLE `tarkastusmerkinta` (
  `tarkastusnro` int NOT NULL AUTO_INCREMENT,
  `tarkastuspvm` varchar(255) DEFAULT NULL,
  `elavia_yksiloita` varchar(255) DEFAULT NULL,
  `menestymista_koskevat_havainnot` varchar(255) DEFAULT NULL,
  `tarkastaja` varchar(255) DEFAULT NULL,
  `kasvin_huomautuksia` text,
  `sijoituspaikan_nro` int DEFAULT NULL,
  `uus_tarkastuspvm` date DEFAULT NULL,
  PRIMARY KEY (`tarkastusnro`),
  KEY `IDX_Tarkastusmerkinta1` (`sijoituspaikan_nro`),
  CONSTRAINT `tarkastusmerkinta_ibfk_1` FOREIGN KEY (`sijoituspaikan_nro`) REFERENCES `sijoituspaikka` (`sijoituspaikan_nro`)
) ENGINE=InnoDB AUTO_INCREMENT=133017 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `testi`
--

DROP TABLE IF EXISTS `testi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Test table
CREATE TABLE `testi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pvm` varchar(255) DEFAULT NULL,
  `uuspvm` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `toimenpide`
--

DROP TABLE IF EXISTS `toimenpide`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Action/operation
CREATE TABLE `toimenpide` (
  `toimenpide_nro` int NOT NULL AUTO_INCREMENT,
  `pvm` varchar(255) DEFAULT NULL,
  `toimenpide` varchar(255) DEFAULT NULL,
  `hankintaID` int DEFAULT NULL,
  `uus_pvm` date DEFAULT NULL,
  PRIMARY KEY (`toimenpide_nro`),
  KEY `IDX_Toimenpide1` (`hankintaID`),
  CONSTRAINT `toimenpide_ibfk_1` FOREIGN KEY (`hankintaID`) REFERENCES `hankintatiedot` (`hankintaID`)
) ENGINE=InnoDB AUTO_INCREMENT=35232 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `viherrakentamiskaytto`
--

DROP TABLE IF EXISTS `viherrakentamiskaytto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Green space/landscaping use (obsolete)
CREATE TABLE `viherrakentamiskaytto` (
  `NIMI` varchar(255) DEFAULT NULL,
  `KOODI` varchar(100) DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `viite`
--

DROP TABLE IF EXISTS `viite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Reference/bibliographic citation
CREATE TABLE `viite` (
  `viitenro` int NOT NULL AUTO_INCREMENT,
  `viitteen_lyhenne` varchar(255) DEFAULT NULL,
  `tekija` varchar(255) DEFAULT NULL,
  `kirjan_nimi` varchar(255) DEFAULT NULL,
  `kirja_selite` varchar(255) DEFAULT NULL,
  `kustantaja` varchar(255) DEFAULT NULL,
  `painos` varchar(255) DEFAULT NULL,
  `vuosi` varchar(255) DEFAULT NULL,
  `ISBN` varchar(255) DEFAULT NULL,
  `sijainti` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=292 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ymparistoindikaattoriluonne`
--

DROP TABLE IF EXISTS `ymparistoindikaattoriluonne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
-- Environmental indicator characteristic
CREATE TABLE `ymparistoindikaattoriluonne` (
  `indikaattorin_nro` int NOT NULL AUTO_INCREMENT,
  `ymparistoindikaattoriluonne` varchar(255) DEFAULT NULL,
  `ymparistoindikaattorin_selite` varchar(255) DEFAULT NULL,
  `taksonin_nro` int NOT NULL DEFAULT '0',
  `viitenro` int DEFAULT NULL,
  PRIMARY KEY (`indikaattorin_nro`),
  KEY `IDX_Ymparistoindikaattoriluonne1` (`taksonin_nro`),
  KEY `IDX_Ymparistoindikaattoriluonne2` (`viitenro`),
  CONSTRAINT `ymparistoindikaattoriluonne_ibfk_1` FOREIGN KEY (`taksonin_nro`) REFERENCES `taksoni` (`taksonin_nro`),
  CONSTRAINT `ymparistoindikaattoriluonne_ibfk_2` FOREIGN KEY (`viitenro`) REFERENCES `viite` (`viitenro`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-21 18:39:27
