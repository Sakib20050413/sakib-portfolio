<?php
$conn = mysqli_connect("localhost", "root", "", "sakib_portfolio_db");
if (isset($_POST['save_project'])) {
    $title = mysqli_real_escape_string($conn, $_POST['title']);
    $stack = mysqli_real_escape_string($conn, $_POST['stack']);
    mysqli_query($conn, "INSERT INTO projects (title, stack) VALUES ('$title', '$stack')");
}
?>
