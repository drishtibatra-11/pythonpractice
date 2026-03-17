import os 
with open("example.txt", "w") as f:
    f.write("this is a sample file for testing os module functions.")
    f.write("\nsecond line of the file.")
with open("source.txt", "w") as f:
    f.write("this file will be copied")
with open("file_to_rename.txt", "w") as f:
    f.write("this file will be deleted")
with open("old_name.txt", "w") as f:
    f.write("this file will be renamed")