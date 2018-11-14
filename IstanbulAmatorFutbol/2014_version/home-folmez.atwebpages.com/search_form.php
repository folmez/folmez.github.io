  <form action="search.php" method="GET" align="center">
    <select name="sezon">
      <option value="1516" <?php if($sezon=='1516'){echo "selected";} ?> >2015-2016</option>
      <option value="1415" <?php if($sezon=='1415'){echo "selected";} ?> >2014-2015</option>
      <option value="1314" <?php if($sezon=='1314'){echo "selected";} ?> >2013-2014</option>
      <option value="1213" <?php if($sezon=='1213'){echo "selected";} ?> >2012-2013</option>
    </select>
    <br>
    <br>
    <label for="text">Hakem:</label>
    <input type="text" name="query" value="<?php echo $query_value ?>"/>
    <br>
    <label for="text">Takım:</label>
    <input type="text" name="query_takim" value="<?php echo $query_takim_value ?>"/>
    <br>
    <input type="radio" name="buhafta" value=0 <?php if($buhafta==0){echo "checked";} ?> >
    Tüm sezonu göster
    <br>
<!--        
    <input type="radio" name="buhafta" value=1 <?php if($buhafta==1){echo "checked";} ?> >
    Sadece bu haftanın maçlarını göster -->
    <br>
    <input type="submit" value="Maçları bul!" />
  </form>
  
  <br>
  
  <form action="search_all_SAL_refs_this_week.php" method="GET" align="center">
    <input type="submit" value="Bu haftaki SAL ve 1AL maç sayılarını görüntüle!" />
  </form>
  
    <br>

  <form action="search_all_SAL_refs.php" method="GET" align="center">
    <input type="submit" value="Tüm SAL ve 1AL maç sayılarını görüntüle!" />
  </form>
  