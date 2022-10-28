-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 28, 2022 at 04:36 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pops`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `user_id` int(11) NOT NULL COMMENT '使用者ID ',
  `user_name` varchar(20) NOT NULL COMMENT '使用者名稱(註冊 + 登入 + 後端編輯)',
  `user_password` varchar(40) NOT NULL COMMENT '使用者密碼(註冊 + 登入 + 後端編輯)',
  `user_balance` int(16) NOT NULL COMMENT '使用者餘額(後端編輯)',
  `user_phone` varchar(30) NOT NULL COMMENT '使用者電話號碼(註冊 + 後端編輯)',
  `user_email` varchar(100) NOT NULL COMMENT '使用者電子信箱(註冊 + 後端編輯)',
  `user_register_date` datetime NOT NULL COMMENT '使用者註冊日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `interface`
--

CREATE TABLE `interface` (
  `event_article_id` int(11) NOT NULL COMMENT '事件表單ID',
  `event_title` varchar(60) NOT NULL COMMENT '事件表單主題',
  `event_content` text NOT NULL COMMENT '事件表單敘述',
  `event_edit_date` datetime NOT NULL COMMENT '事件編輯日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `interface`
--
ALTER TABLE `interface`
  ADD PRIMARY KEY (`event_article_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '使用者ID ';

--
-- AUTO_INCREMENT for table `interface`
--
ALTER TABLE `interface`
  MODIFY `event_article_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '事件表單ID';
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
