<?php
  $targetdir = 'uploads/';
      // name of the directory where the files should be stored
  $targetfile = $targetdir.$_FILES['file']['name'];

  if (move_uploaded_file($_FILES['file']['tmp_name'], $targetfile)) {
    echo "file uploaded succeeded";
  } else {
    echo "file upload failed";
  }
?>
<html>
<head>
<title>Uploading Complete</title>
</head>
<body>
<h2>Uploaded File Info:</h2>
<ul>
<li>Sent file: <?php echo $_FILES['file']['name'];  ?>
<li>File size: <?php echo $_FILES['file']['size'];  ?> bytes
<li>File type: <?php echo $_FILES['file']['type'];  ?>
</ul>
</body>
</html>
