<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $image = $data['image'];

    $image_parts = explode(";base64,", $image);
    $image_base64 = base64_decode($image_parts[1]);
    $file_path = 'snapshots/' . uniqid() . '.png';

    if (!file_exists('snapshots')) {
        mkdir('snapshots', 0777, true);
    }

    file_put_contents($file_path, $image_base64);
    echo 'Snapshot saved successfully: ' . $file_path;
}
?>
