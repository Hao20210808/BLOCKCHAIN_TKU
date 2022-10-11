<?php
  session_start();
  session_destroy();
  header('Location: MainPage.php?page=login');
?>
