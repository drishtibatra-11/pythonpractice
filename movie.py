movies={}
n=int(input("enter number of movies: "))
for i in range(n):
    name=input("enter name of movie: ")
    year=int(input("enter year of movie: "))
    director=input("enter director of movie: ")
    movies[name]={"year":year,"director":director}
    for m in movies:
        print(m, movies[m])
    print("")    