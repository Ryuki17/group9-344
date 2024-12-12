PHP Secure Page Code:
<?php
// Allowed files for inclusion
$allowed_files = ['home', 'about', 'contact'];

// Check if 'file' parameter is set, sanitize it, and ensure it's valid
if (isset($_GET['file']) && in_array(basename($_GET['file']), $allowed_files)) {
    include('/var/www/html/' . basename($_GET['file']) . '.php');
} else {
    echo "Invalid file request.";
}
?>
