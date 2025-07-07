<?php 
header('Content-Type: application/json');
require_once 'db_config.php'; 
 
try {
    $data = json_decode(file_get_contents('php://input'), true);
    
    // 验证必填字段 
    if (empty($data['cn_name']) || empty($data['name']) || empty($data['username']) || empty($data['password'])) {
        throw new Exception('缺少必填字段');
    }
    
    $conn = getDBConnection();
    
    $sql = "INSERT INTO yo_all_password (cn_name, name, url, username, password, note) 
            VALUES (?, ?, ?, ?, ?, ?)";
    
    $stmt = $conn->prepare($sql);
    if (!$stmt) {
        throw new Exception($conn->error);
    }
    
    $stmt->bind_param("ssssss", 
        $data['cn_name'], 
        $data['name'], 
        $data['url'], 
        $data['username'], 
        $data['password'], 
        $data['note']
    );
    
    if ($stmt->execute()) {
        echo json_encode(['success' => true, 'id' => $conn->insert_id]);
    } else {
        throw new Exception($stmt->error);
    }
    
    $stmt->close();
    $conn->close();
    
} catch (Exception $e) {
    error_log("Error: " . $e->getMessage());
    echo json_encode(['success' => false, 'message' => '添加失败: ' . $e->getMessage()]);
}
?>