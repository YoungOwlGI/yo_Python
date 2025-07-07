<?php
header('Content-Type: application/json');
require_once 'db_config.php';

try {
    $conn = getDBConnection();

    $sql = "SELECT id, cn_name, name, url, username, password, note FROM yo_all_password";
    $stmt = $conn->prepare($sql);

    if (!$stmt) {
        throw new Exception($conn->error);
    }

    $stmt->execute();
    $result = $stmt->get_result();

    $passwords = [];
    while ($row = $result->fetch_assoc()) {
        $passwords[] = $row;
    }

    echo json_encode($passwords);

    $stmt->close();
    $conn->close();

} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo json_encode(['success' => false, 'message' => '获取数据失败']);
}
?>