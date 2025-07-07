<?php 
header('Content-Type: application/json');
require_once 'db_config.php'; 
 
try {
    $data = json_decode(file_get_contents('php://input'), true);
    
    // 验证必填字段 
    if (empty($data['id']) || empty($data['cn_name']) || empty($data['name']) || empty($data['username']) || empty($data['password'])) {
        throw new Exception('缺少必填字段');
    }
    
    $conn = getDBConnection();
    
    $sql = "UPDATE yo_all_password 
            SET cn_name=?, name=?, url=?, username=?, password=?, note=?
            WHERE id=?";
    
    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        throw new Exception($conn->error);
    }
    
    $stmt->bind_param("ssssssi", 
        $data['cn_name'], 
        $data['name'], 
        $data['url'], 
        $data['username'], 
        $data['password'], 
        $data['note'],
        $data['id']
    );
    
    if ($stmt->execute()) {
        echo json_encode(['success' => true, 'affected_rows' => $stmt->affected_rows]);
    } else {
        throw new Exception($stmt->error);
    }
    
    $stmt->close();
    $conn->close();
    
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo json_encode(['success' => false, 'message' => '更新失败: ' . $e->getMessage()]);
}
?>