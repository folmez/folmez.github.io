<?php
        
$username = "1711463_maclar";
$password = "***";
$hostname = "fdb6.awardspace.net";
     
//Connection to the database
$dbhandle = mysql_connect($hostname, $username, $password) 
        or die("Unable to connect to MySQL");

mysql_query("SET character_set_results=utf8", $dbhandle);
mysql_query("SET NAMES UTF8");
    
//Select a database to work with
$selected = mysql_select_db("1711463_maclar",$dbhandle) 
        or die("Could not select examples");
?>
 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Search results</title>
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
    $SAL_1AL_mac_sayisi_gorunsun = 0;

    $query = $_GET['query'];
    $query_takim = $_GET['query_takim'];
    $buhafta = $_GET['buhafta'];
    $sezon = $_GET['sezon'];
    
    $query_value = $query;
    $query_takim_value = $query_takim;
    $buhafta_value = $buhafta;
    $sezon_value = $sezon;
    include "search_form.php";


    if($buhafta==1)
    {$tablename = "buhafta";}
    else
    {
        if($sezon=='1213')
        {$tablename = "maclar_1213";}
        if($sezon=='1314')
        {$tablename = "maclar_1314";}
        if($sezon=='1415')        
        {$tablename = "maclar_1415";}
        if($sezon=='1516')        
        {$tablename = "maclar_1516";}
    }
    
    // SAVE SEARCHED QUERIES 
    date_default_timezone_set('Europe/Istanbul');
    $now = date("Y-m-d H:i:s");
    $now_monthyear = date("M_Y");
    $searched_query = "[".$now."],[".$query."],[".$query_takim."],[".$buhafta."],[".$sezon."]"."\n";
    $filename = "../Private/searched_queries_".$now_monthyear.".txt";
    $searched_query .= file_get_contents($filename);
    file_put_contents($filename, $searched_query);
    
    // UPPERCASE SMALL TURKISH CHARACTERS 
    $query = str_replace('i', 'İ', $query);  $query_takim = str_replace('i', 'İ', $query_takim);
    $query = str_replace('ş', 'Ş', $query);  $query_takim = str_replace('ş', 'Ş', $query_takim);
    $query = str_replace('ç', 'Ç', $query);  $query_takim = str_replace('ç', 'Ç', $query_takim);
    $query = str_replace('ğ', 'Ğ', $query);  $query_takim = str_replace('ğ', 'Ğ', $query_takim);
    $query = str_replace('ü', 'Ü', $query);  $query_takim = str_replace('ü', 'Ü', $query_takim);
    $query = str_replace('ö', 'Ö', $query);  $query_takim = str_replace('ö', 'Ö', $query_takim);
    
    // UPPERCASE ALL CHARACTERS 
    $query = mb_convert_case($query, MB_CASE_UPPER, "UTF-8"); 
    $query_takim = mb_convert_case($query_takim, MB_CASE_UPPER, "UTF-8");
    
       
// gets value sent over search form
     
    $min_length = 3;
    // you can set minimum length of the query if you want
     
    if((strlen($query) >= $min_length) or (strlen($query_takim) >= $min_length))
    { // if query length is more or equal minimum length then
         
        $query = htmlspecialchars($query); 
        // changes characters used in html to their equivalents, for example: < to &gt;
         
        $query = mysql_real_escape_string($query);
        // makes sure nobody uses SQL injection
         
        $raw_results = mysql_query("SELECT * FROM ".$tablename."
            WHERE ((`Hakem1` LIKE '%".$query."%')
            OR (`Hakem2` LIKE '%".$query."%')
            OR (`Hakem3` LIKE '%".$query."%'))
            AND (`Takimlar` LIKE '%".$query_takim."%')")
            or die(mysql_error());
        
        
        // * means that it selects all fields, you can also write: `id`, `title`, `text`
        // articles is the name of our table
         
        // '%$query%' is what we're looking for, % means anything, for example if $query is Hello
        // it will match "hello", "Hello man", "gogohello", if you want exact match use `title`='$query'
        // or if you want to match just full word so "gogohello" is out use '% $query %' ...OR ... '$query %' ... OR ... '% $query'
         
        // if one or more rows are returned do following 
        
            
       
        echo "<br>";
        if(mysql_num_rows($raw_results) > 0)
        { 
            $sonuc_varmi = 1; 
            echo "<table align='center'>";
            
            echo "<tr>";
            echo "<td align='center'>";
            echo "Aranan sözcükler: ";
            echo "[".$query."],";
            echo "[".$query_takim."],";
            if($buhafta==1)
            {echo "[Sadece bu hafta]";}
            else
            {echo "[Tüm sezon]";}
            echo "</td>";
 
            echo "</tr>";
            
            echo "<tr>";
            echo "<td>";
            echo "<table border='1'>";
            echo "</td>";
            echo "</tr>";
            
            echo "<tr>";
            echo "<td align='center'>MAÇ GÜNÜ</td>";
            echo "<td align='center'>SAAT</td>";
            echo "<td align='center'>STAD</td>";
            echo "<td align='center'>TAKIMLAR</td>";
            echo "<td align='center'>LİG</td>";
            echo "<td align='center'>GRUP</td>";
            echo "<td align='center'>HAKEM</td>";
            echo "<td align='center'>1. YARDIMCI</td>";
            echo "<td align='center'>2. YARDIMCI</td>";
            echo "</tr>";
             
            while($row = mysql_fetch_array($raw_results))
            {
                    /* $results = mysql_fetch_array($raw_results) puts data from database into array, 
                    while it's valid it does the loop */
             
             echo "<tr>";
             echo "<td>".$row{'MacGunu'}."</td>";
             echo "<td align='center'>".$row{'MacSaati'}."</td>";
             echo "<td>".$row{'Stadyum'}."</td>";
             
                    // Find the searched team's name and write it in bold!
             if(empty($query_takim))
             {echo "<td>".$row{'Takimlar'}."</td>";}
             else
             {
                 echo "<td>";
                 $middle = strpos($row{'Takimlar'}, " - ");
                 $evsahibi = substr($row{'Takimlar'}, 0, $middle);
                 $deplasman = substr($row{'Takimlar'}, $middle+3, strlen($row{'Takimlar'}));
                 if ((mb_stripos($evsahibi, $query_takim) !== false))
                 {echo "<b>".$evsahibi."</b>";}
                 else 
                 {echo $evsahibi;}
                 echo " - ";
                 if ((mb_stripos($deplasman, $query_takim) !== false))
                 {echo "<b>".$deplasman."</b>";}
                 else 
                 {echo $deplasman;}
                 echo "</td>";
             }
             
             echo "<td>".$row{'Lig'}."</td>";
             echo "<td>".$row{'Grup'}."</td>";
             
             if (empty($query))
             {
               echo "<td>".$row{'Hakem1'}."</td>";
               echo "<td>".$row{'Hakem2'}."</td>";
               echo "<td>".$row{'Hakem3'}."</td>";
             }
             else
             {
               if ((mb_stripos($row{'Hakem1'}, $query) !== false))
               {echo "<td><b>".$row{'Hakem1'}."</b></td>";}
               else 
               {echo "<td>".$row{'Hakem1'}."</td>";}
               if (mb_stripos($row{'Hakem2'}, $query) !== false)
               {echo "<td><b>".$row{'Hakem2'}."</b></td>";}
               else
               {echo "<td>".$row{'Hakem2'}."</td>";}
               if (mb_stripos($row{'Hakem3'}, $query) !== false)
               {echo "<td><b>".$row{'Hakem3'}."</b></td>";}
               else
               {echo "<td>".$row{'Hakem3'}."</td>";}
              }
             echo "</tr>";
            }
         
            echo "</table>";
            echo "<br><center> -- bu kadar -- </center><br>";         
        }
        else
        {
          $sonuc_varmi = 0;
          echo "<center>Sonuç yok.</center>";
          echo "<br>";
          echo "<center>";
          echo "Aranan sözcükler: ";
          echo "[".$query."],";
          echo "[".$query_takim."],";
          if($buhafta==1)
          {echo "[Sadece bu hafta]";}
          else
          {echo "[Tüm sezon]";}
          echo "</center>";
        }
        
        // HAKEM CIKMIS OLDUGU SUPER AMATOR VE 1. AMATOR MACLARININ SAYISINI TABLO HALINDE VER
        $raw_SAL_results_OrtaHakem = mysql_query("SELECT * FROM ".$tablename."
            WHERE (`Hakem1` LIKE '%".$query."%') AND (`Lig` LIKE 'S.AL.')")
            or die(mysql_error());

        $raw_1_AL_results_OrtaHakem = mysql_query("SELECT * FROM ".$tablename."
            WHERE (`Hakem1` LIKE '%".$query."%') AND (`Lig` LIKE '1.AL.')")
            or die(mysql_error());
        
        $raw_SAL_results_YardHakem = mysql_query("SELECT * FROM ".$tablename."
            WHERE ((`Hakem2` LIKE '%".$query."%') OR (`Hakem3` LIKE '%".$query."%')) AND (`Lig` LIKE 'S.AL.')")
            or die(mysql_error());

        $raw_1_AL_results_YardHakem = mysql_query("SELECT * FROM ".$tablename."
            WHERE ((`Hakem2` LIKE '%".$query."%') OR (`Hakem3` LIKE '%".$query."%')) AND (`Lig` LIKE '1.AL.')")
            or die(mysql_error());
        
        if($SAL_1AL_mac_sayisi_gorunsun==1)
        {
        // Sonuclarda birden fazla farkli hakem cikip cikmadigini kontrol et.
        $num_refs = 0;
        $refs = array();
        while($row = mysql_fetch_array($raw_SAL_results_OrtaHakem))
        {
                $refs[$num_refs] = $row{'Hakem1'};
                        //echo $row{'Hakem1'};
                $num_refs = $num_refs + 1;
        }
        while($row = mysql_fetch_array($raw_1_AL_results_OrtaHakem))
        {
                $refs[$num_refs] = $row{'Hakem1'};
                        //echo $row{'Hakem1'};
                $num_refs = $num_refs + 1;
        }
        while($row = mysql_fetch_array($raw_SAL_results_YardHakem))
        {
                if (stripos($row{'Hakem2'}, $query) !== false) 
                {$refs[$num_refs] = $row{'Hakem2'};}//echo $row{'Hakem2'};}
                else
                {$refs[$num_refs] = $row{'Hakem3'};}//echo $row{'Hakem3'};}                
                $num_refs = $num_refs + 1;
        }
        while($row = mysql_fetch_array($raw_1_AL_results_YardHakem))
        {
                if (stripos($row{'Hakem2'}, $query) !== false) 
                {$refs[$num_refs] = $row{'Hakem2'};}//echo $row{'Hakem2'};}
                else
                {$refs[$num_refs] = $row{'Hakem3'};}//echo $row{'Hakem3'};}                
                $num_refs = $num_refs + 1;
        }
        
        $unique_refs = array_unique($refs);    
        $unique_num_refs = count($unique_refs);
        if($unique_num_refs==1)
        {
                echo "<br>";
                
                echo "<table align='center'>";
                
                echo "<tr>";
                echo "<td align='center'>Hakem: ".$refs[0]."</td>";
                echo "</tr>";
                
                echo "<tr>";
                echo "<td>";
                echo "<table border='1'>"; 
                echo "</tr>";
                echo "</td>";
                
                echo "<tr><td></td><td>S.AL.</td><td>1.AL.</td></tr>";
                
                echo "<tr>";
                    echo "<td align='center'>Düdük</td>";
                    echo "<td align='center'>".mysql_num_rows($raw_SAL_results_OrtaHakem)."</td>";
                    echo "<td align='center'>".mysql_num_rows($raw_1_AL_results_OrtaHakem)."</td>";
                echo "</tr>";
                
                echo "<tr>";
                    echo "<td align='center'>Bayrak</td>";
                    echo "<td align='center'>".mysql_num_rows($raw_SAL_results_YardHakem)."</td>";
                    echo "<td align='center'>".mysql_num_rows($raw_1_AL_results_YardHakem)."</td>";
                echo "</tr>";
                
                echo "</table>";
        }
        else
        {
                if($sonuc_varmi == 1) 
                {
                  echo "<br>";
                  echo "<center>Tek bi hoca ismi ararsan burada S.AL. ve 1.AL. sayıları olur (eğer varsa)</center>";
                }
        }
        }
    }
    else
    { // if query length is less than minimum
            echo "Şundan fazla karakter girmen lazım: ".$min_length;
    }
?>

</div>

</div>

</body>
</html>
