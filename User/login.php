<?php
  session_start();
?>
<style>
  form{
    border: #aaa solid 1px;
    margin:20px auto;
    padding:50px;
    width: 400px
  }

  .error{
    color:red;
  }

  button:hover {
    background-color: red;
  }

  a:hover {
    background-color: red;
  }
</style>
<div class="login">
  <?php
    if(isset($_SESSION['is_login']) && $_SESSION['is_login'] == TRUE):
      header('Location: User/backend.php');
    else:
  ?>
  <form method="POST" action="User/checkUser.php">
    <?php
      if (isset($_GET['msg'])) {
        echo "<p class='error'>{$_GET['msg']}</p>";
      }
    ?>
    <div>User Name: <input type="text" name="username" placeholder="User ID" style="width:200px;"/></div>
    <br>
    <div>User Passwords: <input type="password" name="userpassword" placeholder="User password" style="width:200px;"/></div>
    <br>
    <p><button type="submit">Login</button></p>
    <p>If you forget your account password, please contact<a href="MainPage.php?page=contact" style="color: blue">System Administrator</a></p>
    <p>Don't have an administrator account? Click<a href="MainPage.php?page=register" style="color: blue">Register</a></p>
  </form>
  <?php endif; ?>
</div>
