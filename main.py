from random import randint, choice


class Movies:
    def __init__(self, name, year, _type, num_plays):
        self.name = name
        self.year = year
        self._type = _type
        self.num_plays = num_plays
    def __str__(self):
        return f'{self.name}\n rok prod.: {self.year}\n gatunek {self._type}\n liczba odtworzeń: {self.num_plays}'

    def play(self, num_plays):
        num_plays += 1
        return num_plays

class Serials(Movies):
    def __init__(self, episodes, seasons, name, year, _type, num_plays):
        super().__init__(name, year, _type, num_plays)
        self.episodes = episodes
        self.seasons = seasons
        self.name = name 
        self.year = year
        self._type = _type
        self.num_plays = num_plays

    def __str__(self):
        return f'tytuł: {self.name}\n rok prod.: {self.year}\n gatuneK {self._type}\n ilość odcinków: {self.episodes}\n ilość sezonów:{self.seasons}\n ilość odtworzeń: {self.num_plays}'
        
    def play(self, num_plays):
        num_plays += 1
        return num_plays

           
_list = []    
pulp_fiction = Movies("Pulp fiction",1994,'crime', 0)
killing_zoe = Movies("Killing zoe", 1994, 'crime', 0)
amelie = Movies("Amelie", 2001, 'romantic-comedy', 0) 
trainspotting = Movies("Trainspotting", 1995, 'drama', 0)
Pi = Movies("Pi", 1996,'drama', 0)
delicatessen = Movies("Delicatessen", 1992, 'comedy/thriller', 0)
breaking_bad = Serials(3, 45, "breaking bad", 2012, 'crime', 0) 
queens_gambit = Serials(1, 7, "Queen's gambit", 2020,'moral/comedy', 0)
mr_bean = Serials(1, 110, "Mr Bean", 1994, 'comedy', 0) 
_list.append(pulp_fiction)
_list.append(killing_zoe)
_list.append(amelie)
_list.append(trainspotting)
_list.append(Pi)
_list.append(delicatessen)
_list.append(breaking_bad)
_list.append(queens_gambit)
_list.append(mr_bean)

movies_list = []
serials_list = []
def get_movies():
    for movie in _list:
        if isinstance(movie,Movies) == True:
            movies_list.append(movie)

def get_serials():
    for serial in _list:
        if isinstance(movie,Serials) == True:
           serials_list.append(serial)

def search(name_movie):
    flag = 0
    for movie in _list:
        if movie.name == name_movie:
            print(movie)
            flag = 1
    for serial in serials_list:
        if serial.name == name_movie:
           print(serial)
           flag = 1
    if flag == 0:
        print('Nie posiadamy takiego filmu w zasobach')

def generate_views():
    movie_views = choice(_list)
    number_views = randint(0,100)
    movie_views.num_play = number_views


for play in range(30):
    generate_views()


name_movie = input('Podaj film który Ciebie interesuje: ')
search(name_movie)

tuples_list_movies = []
for movie in _list:
    movie_tuple = (movie.num_plays, movie.name) 
    tuples_list_movies.append(movie_tuple)
sorted_list= sorted(tuples_list_movies)    
print(tuples_list_movies)

get_movies()
get_serials()

print(_list)
print(movies_list)
print(serials_list)










