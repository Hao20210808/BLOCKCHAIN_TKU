<?php
  $host = 'localhost';
  $dbuser = 'root';
  $dbpw = 'm1V@81rQweM4*A/x';
  $dbname = 'POPs';

  $link = mysqli_connect($host, $dbuser, $dbpw, $dbname);
  if ($link) {
    //( value > 0 ) => connected successfully
    //codes => UTF-8
    
    mysql_query($link, "SET NAMES utf8")
    echo "connected success";
  } else {
    //fail, return 'error'
    //mysql_connect_error();
    echo 'connected fail :<br/>'mysqli_connect_error();
  }
?>
