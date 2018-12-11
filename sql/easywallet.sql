-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2018 at 02:27 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

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
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `userid` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `regno` int(10) NOT NULL,
  `walletid` int(2) NOT NULL,
  `activated` int(2) NOT NULL,
  `pin` varchar(255) NOT NULL,
  `disabled` int(2) NOT NULL,
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`userid`, `username`, `password`, `regno`, `walletid`, `activated`, `pin`, `disabled`, `dateCreated`) VALUES
(1, 'adeojo.emmanuel', 'magnitude', 1300890, 0, 0, '1111', 1, '2018-12-01 16:35:02'),
(2, 'adegoke.david', 'magnitude', 1500205, 0, 0, '1111', 0, '2018-12-01 16:35:52'),
(3, 'ogbuji.bright', 'magnitude', 1502336, 0, 0, '1111', 0, '2018-12-01 16:35:52');

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

--
-- Dumping data for table `deposit`
--

INSERT INTO `deposit` (`depositId`, `userid`, `amount`, `depositLocation`, `status`, `depositType`, `depositorName`, `dateDeposited`, `ifManipulated`) VALUES
(1, 1300890, 500, 'cafe', 1, 'cashpoint', 'Adeojo Emmanuel', '2018-12-02 14:51:01', '0000-00-00 00:00:00'),
(2, 1300890, 200, 'ocb', 1, 'cashpoint', 'Adeojo Emmanuel', '2018-12-02 14:58:09', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `settinghistory`
--

CREATE TABLE `settinghistory` (
  `id` int(255) NOT NULL,
  `userid` int(255) NOT NULL,
  `action` int(2) NOT NULL,
  `status` int(2) NOT NULL,
  `userip` varchar(20) NOT NULL,
  `dateAdded` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
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
-- Table structure for table `theftcomplain`
--

CREATE TABLE `theftcomplain` (
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
-- Table structure for table `tracelogin`
--

CREATE TABLE `tracelogin` (
  `id` int(255) NOT NULL,
  `userid` int(10) NOT NULL,
  `routerIp` varchar(30) NOT NULL,
  `userIp` varchar(30) NOT NULL,
  `loginStatus` int(2) NOT NULL,
  `ldate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tracelogin`
--

INSERT INTO `tracelogin` (`id`, `userid`, `routerIp`, `userIp`, `loginStatus`, `ldate`) VALUES
(3, 0, '196.223.125.1', '196.223.125.1', 1, '2018-12-03 23:30:26'),
(4, 0, '196.223.125.1', '196.223.125.1', 1, '2018-12-03 23:30:41'),
(5, 1, '196.223.125.1', '196.223.125.1', 1, '2018-12-03 23:32:32'),
(9, 0, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 13:22:12'),
(10, 0, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 14:29:54'),
(11, 1, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 14:37:33'),
(12, 1300890, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 14:47:34'),
(13, 1300890, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 14:47:47'),
(14, 1300890, '196.223.120.1', '192.168.7.1', 1, '2018-12-10 14:54:44'),
(15, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 14:54:51'),
(16, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 14:55:16'),
(17, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 14:56:21'),
(18, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:00:16'),
(19, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:05:07'),
(20, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:05:29'),
(21, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:06:23'),
(22, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:06:30'),
(23, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:08:38'),
(24, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:10'),
(25, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:21'),
(26, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:32'),
(27, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:34'),
(28, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:38'),
(29, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:45'),
(30, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:09:59'),
(31, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:10:16'),
(32, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:10:32'),
(33, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:12:30'),
(34, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:12:42'),
(35, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:13:02'),
(36, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:13:41'),
(37, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:13:52'),
(38, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:14:38'),
(39, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:15:04'),
(40, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:19:50'),
(41, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:20:28'),
(42, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:20:36'),
(43, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:20:50'),
(44, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:20:58'),
(45, 1300890, '196.223.120.1', '192.168.7.1', 0, '2018-12-10 15:21:04');

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
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `deposit`
--
ALTER TABLE `deposit`
  ADD PRIMARY KEY (`depositId`);

--
-- Indexes for table `settinghistory`
--
ALTER TABLE `settinghistory`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `theftcomplain`
--
ALTER TABLE `theftcomplain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tracelogin`
--
ALTER TABLE `tracelogin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `userid` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `deposit`
--
ALTER TABLE `deposit`
  MODIFY `depositId` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `settinghistory`
--
ALTER TABLE `settinghistory`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `theftcomplain`
--
ALTER TABLE `theftcomplain`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tracelogin`
--
ALTER TABLE `tracelogin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
