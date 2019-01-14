def getNumFiles(path):
  import os
  count = 0
  dirs = os.listdir(path)
  for file in dirs:

    count++
  return count
