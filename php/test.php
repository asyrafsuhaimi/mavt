<?php
$files = glob('/var/www/html/mlwr/uploads/*'); // get all file names
foreach($files as $file){ // iterate files
 echo $file; // delete file
}
