<?php
  session_start();
?>

<style>
  div.result {
    text-align: center;
  }
</style>

<div class="backend">
  <?php
    if(isset($_SESSION['is_login']) && $_SESSION['is_login'] == TRUE):
  ?>

  <div class="result">
    <h2>登入成功!</h2>
    <p><a href="User/logout.php">登出</a></p>
  </div>

  <?php
    else:
      header('Location: MainPage.php?page=login');
    endif;
  ?>
</div>
