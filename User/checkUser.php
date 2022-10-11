<?php
  session_start();

  //$db_user = "test";
  //$db_password = "test";

  if(isset($_POST['username']) && isset($_POST['userpassword'])){
    if($_POST['username'] == $db_user && $_POST['userpassword'] == $db_password){
      $_SESSION['is_login'] = TRUE;
      header('Location: User/backend.php');
    } else {
      $_SESSION['is_login'] = FALSE;
      header('Location: MainPage.php?page=login?msg=Login failed, please confirm your user ID or passwords again');
    }
  } else {
    header('Location: MainPage.php?page=login?msg=Please insert data correctly');
  } endif;
?>
