f = open("city.txt", "w")

f.write("Dehradun 5.78 308.20\n")
f.write("Delhi 190 1484\n")
f.write("Mumbai 200 603\n")
f.write("Agra 15 188\n")
f.write("Shimla 2.5 35\n")

f.close()
f = open("city.txt", "r")

total_area = 0

for line in f:
    print("LINE:", line)   

    if line.strip() == "":
        continue

    data = line.split()
    print("DATA:", data)   

    city = data[0]
    population = float(data[1])
    area = float(data[2])

    print("AREA:", area)  

    total_area += area

print("Total Area:", total_area)

f.close()