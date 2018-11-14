<?php
  $email = $_REQUEST['email'] ;
  $message = $_REQUEST['message'] ;

  mail("folmez@gmail.com", "İstanbul Amatör Futbol Veri Tabanı", $message, "From: $email");
  header( "Location: tesekkurler.html" );
?>