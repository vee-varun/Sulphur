-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 09, 2018 at 05:41 AM
-- Server version: 5.7.21-log
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sulphur`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add category', 7, 'add_category'),
(20, 'Can change category', 7, 'change_category'),
(21, 'Can delete category', 7, 'delete_category'),
(22, 'Can add post', 8, 'add_post'),
(23, 'Can change post', 8, 'change_post'),
(24, 'Can delete post', 8, 'delete_post'),
(25, 'Can add user', 9, 'add_user'),
(26, 'Can change user', 9, 'change_user'),
(27, 'Can delete user', 9, 'delete_user');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$XnWcaqrJxyWk$1XMqvvgJkArnFQ6deh1r9s2H5W7TtNAGquqR2t50oXg=', '2018-05-06 11:04:58.366561', 1, 'ajax', '', '', 'sirajalam049@gmail.com', 1, 1, '2018-05-06 11:04:47.213053');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `blog_category`
--

CREATE TABLE `blog_category` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `cover_pic` varchar(100) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `url` varchar(50) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  `in_nav` tinyint(1) NOT NULL,
  `in_footer` tinyint(1) NOT NULL,
  `unlisted` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `blog_category`
--

INSERT INTO `blog_category` (`id`, `name`, `cover_pic`, `date_created`, `url`, `keywords`, `description`, `in_nav`, `in_footer`, `unlisted`) VALUES
(2, 'Tourism', 'uploads/2018/05/07/11_world_tourism_day.jpg', '2018-05-06 19:12:57.743431', 'tourism', 'Tourism', 'All tourism related posts', 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `blog_post`
--

CREATE TABLE `blog_post` (
  `id` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `cover_pic` varchar(100) DEFAULT NULL,
  `content` longtext,
  `pub_date` datetime(6) NOT NULL,
  `view_count` int(10) UNSIGNED DEFAULT NULL,
  `url` varchar(600) DEFAULT NULL,
  `unlisted` tinyint(1) NOT NULL,
  `last_modified` datetime(6) NOT NULL,
  `is_page` tinyint(1) NOT NULL,
  `in_nav` tinyint(1) NOT NULL,
  `in_footer` tinyint(1) NOT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  `social` tinyint(1) NOT NULL,
  `author_id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `blog_post`
--

INSERT INTO `blog_post` (`id`, `title`, `cover_pic`, `content`, `pub_date`, `view_count`, `url`, `unlisted`, `last_modified`, `is_page`, `in_nav`, `in_footer`, `keywords`, `description`, `social`, `author_id`, `category_id`) VALUES
(4, 'Lotus Temple | Baha\'i House Of Worship', 'uploads/2018/05/07/lotus_temple.jpg', '<h2><img alt=\"\" src=\"/uploads/2018/05/07/lotus_temple.jpg\" style=\"height:401px; width:600px\" /></h2>\r\n\r\n<h2>The Marvellous Lotus Temple</h2>\r\n\r\n<p>Lotus temple is the place of worship of people of Baha&#39;i religion. Mr. Fariborz Sahba was selected as the architect by the world governing the body of Baha&#39;i faith in the year 1974. The Baha&#39;i temple (Lotus Temple) is probably one of the most distinctive and most special buildings to be built in the world today. The completed structure remains both Engineering and in Architectural point of view, as a MARVEL!</p>\r\n\r\n<h2>Attractions of Lotus Temple</h2>\r\n\r\n<ul>\r\n	<li>\r\n	<h3>Model of Lotus Temple</h3>\r\n\r\n	<p>Lotus Temple consisting of basement, 3 groups of nine shells springing from the podium, nine arches, and nine ponds walkways and double layered interior dome makes it look likes symmetric half opened Lotus flower surrounded by its leaves lie at the water surface.</p>\r\n	</li>\r\n	<li>\r\n	<h3>Prayer Hall</h3>\r\n\r\n	<p>Inner leaves of the lotus temple housing the main prayer hall, outer leaves covering the inner hall entrance leaves. The entry gates in the main hall are in human scale with almost 4m of height. Once you enter the main prayer hall, the sense of monumentality continues with the hall almost 40m High. The hall can seat almost 1200 people at a time.</p>\r\n	</li>\r\n</ul>\r\n\r\n<h2>Worship in Lotus Temple</h2>\r\n\r\n<p>Like other Baha&#39;i Houses of Worship, the Lotus Temple is open to all, regardless of any religion, as emphasized in Baha&#39;i texts. The Baha&#39;i laws also emphasize that not only the holy scriptures of the Baha&#39;i Faith but also those people of other religions can be read inside the Lotus Temple regardless of their language. Prayers and readings can be set to music by choirs, no any musical instruments can be played inside the Lotus Temple. Furthermore, no sermons can be delivered there, and no ritualistic ceremonies can be practiced in Lotus Temple</p>', '2018-05-06 19:14:14.104346', 0, 'lotus-temple-bahai-house-of-worship', 0, '2018-05-06 22:43:28.093446', 0, 0, 0, 'Lotus Temple, kamal mandir, baha\'i, nehru place, religion, h', 'Lotus temple is the place of worship of people of Baha\'i religion. Like other Baha\'i Houses of Worship, the Lotus Temple is open to all, regardless of any religion, as emphasized in Baha\'i texts.', 0, 2, 2),
(5, 'Home Page', 'uploads/2018/05/07/laptop_books_work_wallpaper_by_shabbygirlblog-d8g2p5y.jpg', '<p>A sulphur based website.</p>', '2018-05-06 19:47:00.537466', 0, 'home-page', 0, '2018-05-07 06:11:07.418392', 1, 0, 0, '', '', 0, 2, NULL),
(6, 'About', 'uploads/2018/05/07/laptop_books_work_wallpaper_by_shabbygirlblog-d8g2p5y_5fL1UF2.jpg', '<h1>About delhians</h1>\r\n\r\n<p>Being a delhian means you are not only from Delhi but also you love Delhi, live Delhi and even breath Delhi. Delhi as a capital of India perfectly serves its purpose with its unique and attractive tourism places.</p>\r\n\r\n<p>You can contribute to delhians.com to make it better by sharing your ideas, experience, and other stuff with us. Soon we will be adding more features into this by which you can register yourself as a delhian and you can also share your story in Delhi.</p>\r\n\r\n<p><strong>Let&#39;s come to Delhi and make and share some memories with us and others.</strong></p>\r\n\r\n<h3>Updated Informations</h3>\r\n\r\n<p>The information we provide about every place is totally updated with time. We keep eyes on timings and tariff plans of places and make a quick update on any change of any information of places. But we are also humans and have no superpowers, so there may be some chances that we may miss something, if you find any, please let us know. We welcome your suggestions heartily and will correct it for you asap.</p>\r\n\r\n<h3>We are from You</h3>\r\n\r\n<p>We work as a team and everybody is part of this team. We have worked on every aspect which is required for any tourist but you can share any idea of yours as a participant of this team if you feel its suitable. We are always adding places. If we missed something, please let us know, we will add it in our database.</p>', '2018-05-06 22:49:18.869350', 0, 'about', 0, '2018-05-06 22:49:18.869350', 1, 0, 0, 'about page', 'about page', 0, 2, NULL),
(7, 'Sample', 'uploads/2018/05/07/laptop_books_work_wallpaper_by_shabbygirlblog-d8g2p5y_O63LpPN.jpg', '<p>Sample postsample</p>', '2018-05-07 06:08:44.235560', 0, 'sample', 0, '2018-05-07 06:08:44.255611', 0, 0, 0, 'Sample postsample', 'Sample postsample', 0, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'blog', 'category'),
(8, 'blog', 'post'),
(5, 'contenttypes', 'contenttype'),
(9, 'sadmin', 'user'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-05-06 11:00:39.130984'),
(2, 'auth', '0001_initial', '2018-05-06 11:00:58.577003'),
(3, 'admin', '0001_initial', '2018-05-06 11:01:11.769197'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-05-06 11:01:11.869490'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-05-06 11:01:14.867709'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-05-06 11:01:18.397490'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-05-06 11:01:21.287450'),
(8, 'auth', '0004_alter_user_username_opts', '2018-05-06 11:01:21.371781'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-05-06 11:01:23.234446'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-05-06 11:01:23.336165'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-05-06 11:01:23.564559'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-05-06 11:01:29.118729'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-05-06 11:01:31.810734'),
(14, 'sessions', '0001_initial', '2018-05-06 11:01:33.269935'),
(15, 'sadmin', '0001_initial', '2018-05-06 11:09:21.733747'),
(16, 'blog', '0001_initial', '2018-05-06 11:09:26.034278'),
(17, 'blog', '0002_auto_20180506_1711', '2018-05-06 11:41:54.957922');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('8a5d05izm8ebq392yjfnrrbqw9fmq67h', 'YTI4YjFiNGI3ZTVjNDQzMDA4MmFiZjM1MzM5YzA2ZjkzYjY5N2U1OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMDQ5ZDU3NjZkMDk0MDYzZWExNjNlZTAzYjdlMDZkNzc2NThlMzZkIiwidXNlcm5hbWUiOiJyb290IiwiZnVsbF9uYW1lIjoiU2lyYWogQWxhbSIsImdlbmRlciI6dHJ1ZSwiZW1haWwiOiJzaXJhamFsYW0wNDlAZ21haWwuY29tIiwicmVnX2RhdGVfeWVhciI6MjAxOCwicmVnX2RhdGVfbW9udGgiOjUsInJlZ19kYXRlX2RheSI6NiwicmVnX2RhdGVfaG91ciI6MTYsInJlZ19kYXRlX21pbnV0ZSI6NDIsInJlZ19kYXRlX3NlY29uZCI6MTksImRpc3BsYXlfbmFtZSI6IlNpcmFqIiwibGFzdF9tb2RpZmllZF95ZWFyIjoyMDE4LCJsYXN0X21vZGlmaWVkX21vbnRoIjo1LCJsYXN0X21vZGlmaWVkX2RheSI6NiwibGFzdF9tb2RpZmllZF9ob3VyIjoxNiwibGFzdF9tb2RpZmllZF9taW51dGUiOjQyLCJsYXN0X21vZGlmaWVkX3NlY29uZCI6MTksInVzZXJfcGljIjoiZGVmYXVsdC5qcGciLCJpZCI6MiwiYWN0aXZlIjp0cnVlfQ==', '2018-05-21 06:10:22.693574');

-- --------------------------------------------------------

--
-- Table structure for table `sadmin_user`
--

CREATE TABLE `sadmin_user` (
  `id` int(11) NOT NULL,
  `login` varchar(60) NOT NULL,
  `password` varchar(250) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `reg_date` datetime(6) NOT NULL,
  `display_name` varchar(30) NOT NULL,
  `last_modified` datetime(6) NOT NULL,
  `user_pic` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sadmin_user`
--

INSERT INTO `sadmin_user` (`id`, `login`, `password`, `full_name`, `gender`, `email`, `reg_date`, `display_name`, `last_modified`, `user_pic`) VALUES
(2, 'root', 'ce5ca673d13b36118d54a7cf13aeb0ca012383bf771e713421b4d1fd841f539a', 'Siraj Alam', 1, 'sirajalam049@gmail.com', '2018-05-06 16:42:19.347196', 'Siraj', '2018-05-06 16:42:19.347196', 'default.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `blog_category`
--
ALTER TABLE `blog_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_category_url_a23f4a52` (`url`);

--
-- Indexes for table `blog_post`
--
ALTER TABLE `blog_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blog_post_author_id_dd7a8485_fk_sadmin_user_id` (`author_id`),
  ADD KEY `blog_post_category_id_c326dbf8_fk_blog_category_id` (`category_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `sadmin_user`
--
ALTER TABLE `sadmin_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blog_category`
--
ALTER TABLE `blog_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `blog_post`
--
ALTER TABLE `blog_post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `sadmin_user`
--
ALTER TABLE `sadmin_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blog_post`
--
ALTER TABLE `blog_post`
  ADD CONSTRAINT `blog_post_author_id_dd7a8485_fk_sadmin_user_id` FOREIGN KEY (`author_id`) REFERENCES `sadmin_user` (`id`),
  ADD CONSTRAINT `blog_post_category_id_c326dbf8_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
