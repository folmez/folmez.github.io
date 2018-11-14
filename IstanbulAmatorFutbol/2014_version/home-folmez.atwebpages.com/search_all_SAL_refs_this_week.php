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
    $tablename = "buhafta";

    $query_value = "";
    $query_takim_value = "";
    include "search_form.php";
        

    $sezon_tum = mysql_query("SELECT * FROM ".$tablename)
            or die(mysql_error());
            
    $hakemler_temp = array();
    $i = 0;
    while($row = mysql_fetch_array($sezon_tum))
    {
            $hakemler_temp[$i] = $row['Hakem1'];
            $hakemler_temp[$i+1] = $row['Hakem2'];
            $hakemler_temp[$i+2] = $row['Hakem3'];
            $i = $i+3;
    }

    $hakemler_temp = array_unique($hakemler_temp);
    $hakemler_temp2 = array_values($hakemler_temp);
        
    $hakemler = array();
    $j=0;
    $i=0;
    for ($i=0; $i<=count($hakemler_temp2)-1; $i++) 
    {   
            if($hakemler_temp2[$i]!="")
            {
                    $hakemler[$j] = $hakemler_temp2[$i];
                    $j=$j+1;
            }
    }
    
    $macsayilari = array();
    for ($i=0; $i<=count($hakemler)-1; $i++) 
    {   
        $query = $hakemler[$i];
        $macsayilari[$i] = array();
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
        
        $macsayilari[$i][0] = mysql_num_rows($raw_SAL_results_OrtaHakem);
        $macsayilari[$i][1] = mysql_num_rows($raw_1_AL_results_OrtaHakem);
        $macsayilari[$i][2] = mysql_num_rows($raw_SAL_results_YardHakem);
        $macsayilari[$i][3] = mysql_num_rows($raw_1_AL_results_YardHakem);
        $macsayilari[$i][4] = 1000000*$macsayilari[$i][0]+10000*$macsayilari[$i][1]+100*$macsayilari[$i][2]+1*$macsayilari[$i][3];
        $macsayilari[$i][5] = $query;
    }
    echo "</table>";
    
    function mySort($a,$b) 
    {return $b[4]-$a[4];}
    usort($macsayilari, 'mySort');

    echo "<br>";
    echo "<table align='center'>";
    echo "<tr>";
    echo "<td>";
    echo "<table border='1'>"; 
    echo "</tr>";
    echo "</td>";
    echo "<tr><td align='center'>Hakem</td><td>S.AL. Düdük </td><td>1.AL. Düdük</td><td>S.AL. Bayrak </td><td>1.AL. Bayrak </td></tr>";
    
    for ($i=0; $i<=count($hakemler)-1; $i++) 
    {   
        echo "<tr>";
        echo "<td align='center'>".$macsayilari[$i][5]."</td>";;
        echo "<td align='center'>".$macsayilari[$i][0]."</td>";
        echo "<td align='center'>".$macsayilari[$i][1]."</td>";
        echo "<td align='center'>".$macsayilari[$i][2]."</td>";
        echo "<td align='center'>".$macsayilari[$i][3]."</td>";
        echo "</tr>";
    }
    echo "</table>";
    


?>

</div>

</div>

</body>
</html>
