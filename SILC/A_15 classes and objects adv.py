class Movie:
    def __init__(self, list_of_songs):
        self.list_of_songs = list_of_songs
      
    def __repr__(self):  
       return 'Movie(list_of_songs=%s)' % (self.list_of_songs)
    
    def __str__(self):  
       return 'Movie(list_of_songs=%s)' % (self.list_of_songs)

class song:
    def __init__(self, name, length, people):
        self.name = name
        self.length = length
        self.people = people
  
    def __repr__(self):  
       return 'song(name=%s, length=%s, people=%s)' % (self.name, self.length, self.people)
    
    def __str__(self):   
       return 'song(name=%s, length=%s, people=%s)' % (self.name, self.length, self.people)
    
class people:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
  
    def __repr__(self):  
       return 'people(name=%s, age=%s,salary=%s)' % (self.name, self.age, self.salary)
    
    def __str__(self):  
       return 'people(name=%s, age=%s,salary=%s)' % (self.name, self.age, self.salary)
       



#instances for people
people_1 = people("adithya", 25, "30k")
#print(people_1)

people_2 = people("srikar", 23, "30k")

people_3 = people("modu", 20, "25k")

people_4 = people("harry", 22, "27k")

#objects for songs
song_1 = song("close","3.15 mins", people_2)
#print(song_1)

song_2 = song("summer", "3.45 mins", people_1)

song_3 = song("friends", "2.45 mins", people_3)

song_4 = song("silent", "3.23 mins", people_4)

song_5 = song("ocean", "3.00 mins", people_1)

#each movie with its number of songs
Movie_1_songs = [song_1, song_4,song_5]
Movie_1 = Movie(Movie_1_songs)
print(Movie_1)

Movie_2_songs = [song_2 , song_3]
Movie_2 = Movie(Movie_2_songs)
print(Movie_2)