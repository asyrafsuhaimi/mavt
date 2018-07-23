# Open a file
import os, sys
path = "/var/www/html/mlwr/uploads"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print file
