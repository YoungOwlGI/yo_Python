<?php
// db_config.php
$servername = "localhost";
$username = "root";
$password = "xiaomty";
$dbname = "youngowl";

function getDBConnection() {
    global $servername, $username, $password, $dbname;

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        error_log("数据库连接失败: " . $conn->connect_error);
        header('HTTP/1.1 500 Internal Server Error');
        die(json_encode(['success' => false, 'message' => '数据库连接失败']));
    }

    $conn->set_charset("utf8mb4");
    return $conn;
}
?>