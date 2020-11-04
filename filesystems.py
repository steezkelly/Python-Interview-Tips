import os, glob

os.chdir("/Users/Steez/Pictures")
for file in glob.glob("*.jpg"):
  print(file)
