n = int(input("Enter number of movies: "))
movies = {}

# Input movie details
for i in range(n):
    print("\nEnter details for movie", i+1)
    name = input("Movie name: ")
    year = int(input("Release year: "))
    director = input("Director name: ")
    cost = float(input("Production cost: "))
    collection = float(input("Collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# Menu
while True:
    print("\n----- MENU -----")
    print("1. Print all movie details")
    print("2. Display movies released before 2015")
    print("3. Display movies that made profit")
    print("4. Display movies by a particular director")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAll Movie Details:")
        for name, details in movies.items():
            print("\nMovie Name:", name)
            print("Year:", details["year"])
            print("Director:", details["director"])
            print("Production Cost:", details["cost"])
            print("Collection:", details["collection"])

    elif choice == "2":
        print("\nMovies released before 2015:")
        for name, details in movies.items():
            if details["year"] < 2015:
                print(name)

    elif choice == "3":
        print("\nMovies that made profit:")
        for name, details in movies.items():
            if details["collection"] > details["cost"]:
                print(name)

    elif choice == "4":
        search = input("Enter director name: ")
        print("\nMovies directed by", search + ":")
        for name, details in movies.items():
            if details["director"].lower() == search.lower():
                print(name)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")