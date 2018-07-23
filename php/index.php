<?php
$files = glob('/var/www/html/mlwr/uploads/*'); // get all file names
foreach($files as $file){ // iterate files
    unlink($file); // delete file
}
?>
<html>
<title>MAVT</title>
 <style>
   body {
     margin: 0;
     font-family: Arial, Helvetica, sans-serif;
   }

   .topnav {
     overflow: hidden;
     background-color: #333;
   }

   .topnav a {
     float: left;
     color: #f2f2f2;
     text-align: center;
     padding: 14px 16px;
     text-decoration: none;
     font-size: 17px;
   }

   .topnav a:hover {
     background-color: #ddd;
     color: black;
   }

   .topnav a.active {
     background-color: #48D1CC;
     color: white;
   }
   .container{
     width: 400px;
     margin: 100px auto;
   }
   input[type=file] {
     width: 100%;
     padding: 12px 20px;
     margin: 8px 0;
     box-sizing: border-box;
     border: 2px solid #A9A9A9;
     border-radius: 4px;
   }
   .button {
     display: inline-block;
     border-radius: 4px;
     background-color: #f4511e;
     border: none;
     color: #FFFFFF;
     text-align: center;
     font-size: 20px;
     padding: 10px;
     width: 80px;
     transition: all 0.5s;
     cursor: pointer;
     margin: 5px 0px 0px 150px;
   }

   .button span {
     cursor: pointer;
     display: inline-block;
     position: relative;
     transition: 0.5s;
   }

   .button span:after {
     content: '\00bb';
     position: absolute;
     opacity: 0;
     top: 0;
     right: -20px;
     transition: 0.5s;
   }

   .button:hover span {
     padding-right: 25px;
   }

   .button:hover span:after {
     opacity: 1;
     right: 0;
   }

 </style>
   <body>
     <div class="topnav">
       <a href="#home">Home</a>
     </div>
     <div class="container">
       <img src="logo.png" width="110%" height="15%" style="margin: 0px 0px 20px 0px">
      <form action="result.php" method="post" enctype="multipart/form-data">
         <input type="file" name="file"/>
         <input type="submit" class="button"/>
      </form>
    </div>

   </body>
</html>
