<?php
if(isset($_POST['username']) && isset($_POST['Password']) && isset($_POST['role'])) {
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    
    $username = test_input($_POST['username']);
    $password = test_input($_POST['Password']); // Corrected variable name to $password
    $role = test_input($_POST['role']);
    
    if(empty($username)) {
        header("location: ../index.php?error=username is required");
    } else if(empty($password)) { // Corrected variable name to $password
        header("location: ../index.php?error=Password is required");
    } else {
        echo "cool!";
    }
} else {
    header("location: ../index.php");
}
?>


