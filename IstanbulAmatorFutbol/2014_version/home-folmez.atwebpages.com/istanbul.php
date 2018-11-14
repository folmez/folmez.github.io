<html>
  <head>
    <title>İstanbul Amatör Futbol Veri Tabanı</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>

<body>
    
<div id="container">
  <div id="header">
      <h1>İstanbul Amatör Futbol Veri Tabanı</h1>
  </div>
  

  <?php include "navbar.php"; ?>  
  
  <div id="content">    
    <br>  
    <?php 
        $query_value = "";
        $query_takim_value = "";
        $buhafta = 0;
        include "search_form.php"; 
    ?>    
    
    <br>
    <h2>Hoşgeldiniz... Site halen test aşamasındadır.</h2>
    
     <h2>
       <ul> 
         <li>2015-2016 sezonundan ilk 17 Hafta eklendi</li>
         <br>
         <li>Veri tabanında hakem veya takım adı ile arama yapabilirsiniz.</li>
       </ul>
     </h2>
    
    <br>
 
 </div>  
 <?php include_once "statcounter.php"; ?>       
 </div>
 
</body>
</html>