-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 01, 2018 at 09:06 PM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 5.6.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `easywallet`
--

-- --------------------------------------------------------

--
-- Table structure for table `custormers`
--

CREATE TABLE `custormers` (
  `userid` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `regno` int(10) NOT NULL,
  `walletid` int(2) NOT NULL,
  `activated` int(2) NOT NULL,
  `pin` varchar(255) NOT NULL,
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `custormers`
--

INSERT INTO `custormers` (`userid`, `username`, `password`, `regno`, `walletid`, `activated`, `pin`, `dateCreated`) VALUES
(1, 'adeojo.emmanuel', 'magnitude', 1300890, 0, 0, '1111', '2018-12-01 16:35:02'),
(2, 'adegoke.david', 'magnitude', 1500205, 0, 0, '1111', '2018-12-01 16:35:52'),
(3, 'ogbuji.bright', 'magnitude', 1500928, 0, 0, '1111', '2018-12-01 16:35:52');

-- --------------------------------------------------------

--
-- Table structure for table `deposit`
--

CREATE TABLE `deposit` (
  `depositId` int(255) NOT NULL,
  `userid` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  `depositLocation` varchar(255) NOT NULL,
  `status` int(2) NOT NULL,
  `depositType` varchar(30) NOT NULL,
  `depositorName` varchar(100) NOT NULL,
  `dateDeposited` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ifManipulated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int(255) NOT NULL,
  `userid` int(10) NOT NULL,
  `locationDectect` int(2) NOT NULL,
  `emailNotification` int(2) NOT NULL,
  `2fa` int(2) NOT NULL,
  `dashboardStyle` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `spending`
--

CREATE TABLE `spending` (
  `spendingId` int(255) NOT NULL,
  `locationId` int(10) NOT NULL,
  `amount` int(10) NOT NULL,
  `userId` int(10) NOT NULL,
  `merchantiD` int(10) NOT NULL,
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dateManipulated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `theftComplain`
--

CREATE TABLE `theftComplain` (
  `id` int(255) NOT NULL,
  `userid` int(10) NOT NULL,
  `tansactionid` int(255) NOT NULL,
  `transactionType` varchar(20) NOT NULL,
  `status` int(2) NOT NULL,
  `dateComplained` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dateUpdated` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transfers`
--

CREATE TABLE `transfers` (
  `transferId` int(11) NOT NULL,
  `userid` int(255) NOT NULL,
  `amount` int(10) NOT NULL,
  `fromWho` int(10) NOT NULL,
  `toWho` int(10) NOT NULL,
  `isCrime` int(2) NOT NULL,
  `approved` int(2) NOT NULL,
  `dateTransferd` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `custormers`
--
ALTER TABLE `custormers`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `deposit`
--
ALTER TABLE `deposit`
  ADD PRIMARY KEY (`depositId`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spending`
--
ALTER TABLE `spending`
  ADD PRIMARY KEY (`spendingId`);

--
-- Indexes for table `theftComplain`
--
ALTER TABLE `theftComplain`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `custormers`
--
ALTER TABLE `custormers`
  MODIFY `userid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `deposit`
--
ALTER TABLE `deposit`
  MODIFY `depositId` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `spending`
--
ALTER TABLE `spending`
  MODIFY `spendingId` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `theftComplain`
--
ALTER TABLE `theftComplain`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
