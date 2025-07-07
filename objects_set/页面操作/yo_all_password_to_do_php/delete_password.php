<?php
header('Content-Type: application/json');
require_once 'db_config.php';

try {
    $data = json_decode(file_get_contents('php://input'), true);

    if (empty($data['id'])) {
        throw new Exception('缺少ID参数');
    }

    $conn = getDBConnection();

    $sql = "DELETE FROM yo_all_password WHERE id=?";

    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        throw new Exception($conn->error);
    }

    $stmt->bind_param("i", $data['id']);

    if ($stmt->execute()) {
        echo json_encode(['success' => true, 'affected_rows' => $stmt->affected_rows]);
    } else {
        throw new Exception($stmt->error);
    }

    $stmt->close();
    $conn->close();

} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo json_encode(['success' => false, 'message' => '删除失败: ' . $e->getMessage()]);
}
?>