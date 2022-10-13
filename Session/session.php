<?php
 require_once '/Mysql_DB/MysqlConnect.php';

 session_start();
 $_SESSION['UserName'] = '$user_name';
 echo '$_SESSION["UserName"]' . $_SESSION['UserName'];
?>
