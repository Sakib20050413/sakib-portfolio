<?php
// db.php - Database Configuration & MySQLi Connection for Web Technology Lab CRUD Evaluation
// Student: Md Najmus Sakib Rahatul (ID: 1119003), Dept. of CSE, BAIUST

$host     = "localhost";
$username = "root";
$password = "";
$database = "portfolio_db";

// Connect to MySQL Server (Procedural mysqli)
$conn = @mysqli_connect($host, $username, $password);

if (!$conn) {
    die("<div style='color:red; font-family:sans-serif; padding:20px;'>
            <h3>[MySQL Connection Error]</h3>
            Unable to connect to MySQL database server at <code>$host</code>.<br>
            Error: " . mysqli_connect_error() . "<br>
            <em>Please ensure XAMPP / MySQL service is running.</em>
         </div>");
}

// Create database if not exists
$create_db_sql = "CREATE DATABASE IF NOT EXISTS `$database` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci";
mysqli_query($conn, $create_db_sql);

// Select the database
mysqli_select_db($conn, $database);

// Auto-create projects table
$projects_table = "CREATE TABLE IF NOT EXISTS `projects` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `code` VARCHAR(20) NOT NULL UNIQUE,
    `title` VARCHAR(255) NOT NULL,
    `category` VARCHAR(100) NOT NULL DEFAULT 'Full-Stack Web',
    `tech_stack` VARCHAR(350) NOT NULL,
    `summary` TEXT NOT NULL,
    `stars_count` INT DEFAULT 0,
    `github_url` VARCHAR(255) DEFAULT '',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
mysqli_query($conn, $projects_table);

// Auto-create messages table
$messages_table = "CREATE TABLE IF NOT EXISTS `messages` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `sender_name` VARCHAR(150) NOT NULL,
    `sender_email` VARCHAR(150) NOT NULL,
    `subject` VARCHAR(255) NOT NULL,
    `message` TEXT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";
mysqli_query($conn, $messages_table);

// Seed sample project if table is empty
$count_res = mysqli_query($conn, "SELECT COUNT(*) as total FROM `projects`");
$row = mysqli_fetch_assoc($count_res);
if ($row && $row['total'] == 0) {
    $seed_sql = "INSERT INTO `projects` (`code`, `title`, `category`, `tech_stack`, `summary`, `stars_count`, `github_url`) VALUES
    ('A001', 'BAIUST Campus Lost & Found System', 'Full-Stack Web', 'Django 5, Python, Bootstrap 5, PostgreSQL', 'Automated lost and found recovery platform across 14 BAIUST campus zones with smart matching.', 42, 'https://github.com/Sakib20050413/campus_lostfound'),
    ('A002', 'IoT Storm & Lightning Early Warning Box', 'IoT & TinyML', 'ESP32-S3, AS3935 RF Sensor, BMP280, GSM', '3-Stream AI/ML lightning distance warning system with Bangla voice siren.', 58, 'https://github.com/Sakib20050413/lightning-early-warning-iot'),
    ('A003', '512-Point FFT Mosquito Trap', 'IoT & TinyML', 'ESP32-S3, INMP441, 512-pt FFT, PWM Fan', 'Acoustic bio-trap classifying female vector mosquitoes in 32ms.', 51, 'https://github.com/Sakib20050413/mosquito-dsp-trap')";
    mysqli_query($conn, $seed_sql);
}
?>
