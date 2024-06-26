<?php

$AUTH_USER = 'username';
$AUTH_PASS = 'password';

header('Cache-Control: no-cache, must-revalidate, max-age=0');

$has_supplied_credentials = !(empty($_SERVER['PHP_AUTH_USER']) && empty($_SERVER['PHP_AUTH_PW']));
$is_authenticated = 
    $has_supplied_credentials && 
    $_SERVER['PHP_AUTH_USER'] == $AUTH_USER && 
    $_SERVER['PHP_AUTH_PW'] == $AUTH_PASS;

if (!$is_authenticated) {
    header('HTTP/1.1 401 Authorization Required');
    header('WWW-Authenticate: Basic realm="Access denied"');
    error_log('Unauthorized access attempt');
    exit('Unauthorized');
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    error_log('POST request received');
    $data = json_decode(file_get_contents('php://input'), true);
    if (!isset($data['image']) || empty($data['image'])) {
        error_log('Invalid input: image not set or empty');
        exit('Invalid input');
    }
    $image = $data['image'];
    $image_parts = explode(";base64,", $image);
    if (count($image_parts) !== 2) {
        error_log('Invalid input: incorrect base64 format');
        exit('Invalid input');
    }

    $image_base64 = base64_decode($image_parts[1]);
    if ($image_base64 === false) {
        error_log('Invalid base64 input');
        exit('Invalid base64 input');
    }

    $file_path = 'snapshots/' . uniqid() . '.png';

    if (!file_exists('snapshots')) {
        mkdir('snapshots', 0777, true);
    }

    if (file_put_contents($file_path, $image_base64) === false) {
        error_log('Failed to save image');
        exit('Failed to save image');
    }

    echo 'Snapshot saved successfully: ' . $file_path;
    error_log('Snapshot saved successfully: ' . $file_path);
} else {
    error_log('Invalid request method: ' . $_SERVER['REQUEST_METHOD']);
    exit('Invalid request method');
}
?>
