<?php

$cmd = 'python /home/asyraf/Desktop/analyze.py';

$output = shell_exec($cmd);

while (@ ob_end_flush()); // end all output buffers if any

$proc = popen($cmd, 'r');
echo '<pre>';
while (!feof($proc))
{
    echo fread($proc, 4096);
    @ flush();
}
echo '</pre>';
?>
