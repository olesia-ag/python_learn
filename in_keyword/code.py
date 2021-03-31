friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

movies_watched = {"The Matrix", "Greend Book", "Her"}

user_movie = input("enter movie")
if user_movie in movies_watched:
  print(f"I've watched it {user_movie} too")
else:
  print(f"I haven't watched {user_movie} yet")

