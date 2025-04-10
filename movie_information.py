import imdb 

ia = imdb.Cinemagoer()
Movie = input('Entrez a movie name:')
items = ia.search_movie(Movie)

print("\nSearch results:")

for index, movie in enumerate(items):
    print(f"{index + 1}. {movie['title']} ({movie.get('year','N/A')})")

movie_index = int(input("\nEntrer the number of the movie you want to get info for :")) - 1
movie_id = items[movie_index].movieID
movie_info = ia.get_movie(movie_id)

print("\nMovie Information:")
print(f"Title:{movie_info.get('title','N/A')}")
print(f"Year:{movie_info.get('year','N/A')}")
print(f"Rating:{movie_info.get('rating','N/A')}")
print(f"Genres:{','.join(movie_info.get('genres', []))}")
print(f"Directory(s):{','.join(str(d) for d in movie_info.get('directory', []))}")
print(f"Cast:{','.join(str(c) for c in movie_info.get('cast',[])[:5])}...")
print(f"Plot:{movie_info.get('plot outline','N/A')}")
print(f"Runtime:{movie_info.get('runtimes',['N/A'])[0]} minutes")
print(f"Country:{','.join(movie_info.get('country',[]))} ")
print(f"Language: {','.join(movie_info.get('languages',[]))}")
