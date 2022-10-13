<?php
 require_once 'MysqlConnect.php';

 session_start();
 $_SESSION['UserName'] = '$user_name';
 echo '$_SESSION["UserName"]' . $_SESSION['UserName'];
?>
