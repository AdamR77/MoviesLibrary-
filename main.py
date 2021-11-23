from random import randint, choice


class Movies:
    def __init__(self, name, year, _type, num_plays):
        self.name = name
        self.year = year
        self._type = _type
        self.num_plays = num_plays
    def __str__(self):
        return f'{self.name}\n rok prod.: {self.year}\n gatunek {self._type}\n liczba odtworzeń: {self.num_plays}'
    def __repr__(self) -> str:
        return self.__str__()

    def play(self, num_plays):
        num_plays += 1
        return num_plays

class Series(Movies):
    def __init__(self, episodes, seasons, name, year, _type, num_plays):
        super().__init__(name, year, _type, num_plays)
        self.episodes = episodes
        self.seasons = seasons

    def __str__(self):
        return f'tytuł: {self.name}\n rok prod.: {self.year}\n gatuneK {self._type}\n ilość odcinków: {self.episodes}\n ilość sezonów:{self.seasons}\n ilość odtworzeń: {self.num_plays}'
                 
_list = []    
pulp_fiction = Movies("Pulp fiction",1994,'crime', 0)
killing_zoe = Movies("Killing Zoe", 1994, 'crime', 0)
amelie = Movies("Amelie", 2001, 'romantic-comedy', 0) 
trainspotting = Movies("Trainspotting", 1995, 'drama', 0)
Pi = Movies("Pi", 1996,'drama', 0)
delicatessen = Movies("Delicatessen", 1992, 'comedy/thriller', 0)
breaking_bad = Series(45, 6, "breaking bad", 2012, 'crime', 0) 
queens_gambit = Series(7, 1, "Queen's gambit", 2020,'moral/comedy', 0)
mr_bean = Series(110, 1, "Mr Bean", 1994, 'comedy', 0) 
_list.append(pulp_fiction)
_list.append(killing_zoe)
_list.append(amelie)
_list.append(trainspotting)
_list.append(Pi)
_list.append(delicatessen)
_list.append(breaking_bad)
_list.append(queens_gambit)
_list.append(mr_bean)

names_list = []
for x in _list:
    name = x.name
    names_list.append(name)
    
movies_list = []
series_list = []

def get_movies_type():
    for movie in _list:
        if isinstance(movie, Series) != True:
            movies_list.append(movie)
        else:
           series_list.append(movie)


def search(name_movie):
    flag = False
    for movie in movies_list:
        if movie.name == name_movie:
            flag = True
            return movie

    for serie in series_list:
        if serie.name == name_movie:
           flag = True
           return serie
    
    if flag == False:
        info = 'Nie posiadamy takiego filmu w zasobach'
        return info


def generate_views():
        randomized = choice(_list)
        number_views = randint(0,100)
        print("wylosowano:", randomized.name, number_views)
        randomized.num_plays = number_views
    

def get_movies():
    print(f"lista filmów: {movies_list} ")

def get_series():
    print(f"lista seriali: {series_list}")

def top_titles():
    for movie in _list:
        result = sorted(_list, key=movie.num_plays)
        print(result)
    

get_movies_type()

for x in range(30):
    generate_views()

# to tak dla sprawdzenia czy sortuje filmy i seriale do swoich list 

#get_movies()
#get_series()

name_movie = input('Podaj film który Ciebie interesuje: ')
print(search(name_movie))

top_titles()

















