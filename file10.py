import shutil
import os
shutil.copy('example.txt', 'copy.txt')
os.rename('copy.txt', 'renamed_copy.txt')