<?php
  $targetdir = 'uploads/';// name of the directory where the files should be stored
  $targetfile = $targetdir.$_FILES['file']['name'];

  if (move_uploaded_file($_FILES['file']['tmp_name'], $targetfile)) {
    echo "<script>alert('File Successfuly Uploaded');</script>";
  } else {
    echo "<script>alert('File Cannot Be Uploaded'); window.location.href = 'index.php';</script>";
  }

$cmd = 'python /home/asyraf/Desktop/analyze.py';

$output = shell_exec($cmd);

while (@ ob_end_flush()); // end all output buffers if any

$proc = popen($cmd, 'r');
?>

<!DOCTYPE html>
<html>
<title>Result</title>
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
  .wrapper{
    margin: 10px 0 0 20px;
  }
  .wrapper2{

    margin: auto;
    border-style: solid;
    border-color: coral;
    border-width: 1px;
    padding-top: 5px;
    padding-right: 5px;
    padding-bottom: 5px;
    padding-left: 20px;
    width: 510px;
    height: 200px;
    overflow: scroll;
  }
  .scenario{
    margin: auto;
    width: 800px;
    height: 500px;
    background-color: #F8F8FF;
    border-style: solid;
    border-color: coral;
    border-width: 1px;

  }
</style>
<body>
  <div class="topnav">
    <a href="index.php">Home</a>
  </div>
  <h2 style="text-align:center;">Result of the Analysis</h2>
  <div class="wrapper">
    <h2>Uploaded File Info:</h2>
    <ul>
    <li>Sent file: <?php echo $_FILES['file']['name'];  ?>
    <li>File size: <?php echo $_FILES['file']['size'];  ?> bytes
    <li>File type: <?php echo $_FILES['file']['type'];  ?> 
    </ul>
  </div>
<h2 style="text-align:center;">Scenario of the Malware Attack</h2>
<div class="scenario">
</div>
<h2 style="text-align:center;">Summary of Attack Sequence</h2>
<div class="wrapper2">
<p><?php 
echo '<pre>';
while (!feof($proc))
{
    echo fread($proc, 4096);
    @ flush();
}
echo '</pre>';?>
</p>
</div>
</body>
</html>

