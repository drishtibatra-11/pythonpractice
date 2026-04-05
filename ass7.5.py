try:
    f = open("data.txt", "r")
    content = f.read()
    print(content)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("No permission to access file")

except Exception as e:
    print("Some error occurred:", e)

finally:
    print("Program ended")