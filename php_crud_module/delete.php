<?php
// delete.php - Delete Record from MySQL Database
// Web Technology Lab & Theory Assignment Module
// Student: Md Najmus Sakib Rahatul (ID: 1119003), Dept. of CSE, BAIUST

require_once 'db.php';

$id   = isset($_GET['id']) ? (int)$_GET['id'] : 0;
$type = isset($_GET['type']) ? trim($_GET['type']) : 'project';

if ($id > 0) {
    if ($type === 'message') {
        $stmt = mysqli_prepare($conn, "DELETE FROM `messages` WHERE `id` = ?");
        mysqli_stmt_bind_param($stmt, "i", $id);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
        header("Location: index.php?msg=" . urlencode("Message deleted successfully."));
        exit;
    } else {
        $stmt = mysqli_prepare($conn, "DELETE FROM `projects` WHERE `id` = ?");
        mysqli_stmt_bind_param($stmt, "i", $id);
        mysqli_stmt_execute($stmt);
        mysqli_stmt_close($stmt);
        header("Location: index.php?msg=" . urlencode("Project record #$id deleted successfully."));
        exit;
    }
}

header("Location: index.php");
exit;
?>
