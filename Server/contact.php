<?php
//載入 db.php 檔案，讓我們可以透過它連接資料庫
//require_once 'php/db.php';
?>
<!DOCTYPE html>
<html lang="zh-TW">
  <head>
    <title>contact</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="css/style.css"/>
    <link rel="shortcut icon" href="images/favicon.ico">
  </head>

  <body>
		<?php include_once 'menu.php'; ?>
    <div class="content">
      <div class="container">
        <div class="row">
          <div class="col-xs-12">
            <div class="row">
              <div class="col-md-6">
                <h1>Contact</h1>
              </div>
              <div class="col-md-6">
                <h1>TamKang University Computer Science Internet Engineering</h1>
                <p>
                  Address：No.151, Yingzhuan Rd., Tamsui Dist., New Taipei City 251301, Taiwan (R.O.C.)
                  <br>
                  Phone Number：+886-2-2621-5656
                  <br>
                  Email：<a href="mailto:service@sweea.com">service@sweea.com</a>
                  <br>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <?php include_once 'footer.php'; ?>
  </body>
</html>
