class Movies:
    def __init__(self, name, year, _type, num_plays):
        self.name = name
        self.year = year
        self._type = _type
        self.num_plays = num_plays
    def __str__(self):
        return f'{self.name}\t{self.year}\t{self._type}\t{self.num_plays}'
class Serials(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs )
        self.episode = episode
        self.season = season

def play(num_plays):
    num_plays += 1
    return num_plays
movies = []
serials = []    
pulp_fiction = Movies("Pulp fiction",1994,'crime', 0)
killing_zoe = Movies("Killing zoe", 1994, 'crime', 0)
amelie = Movies("Amelie", 2001, 'romantic-comedy', 0) 
trainspotting = Movies("Trainspotting", 1995, 'drama', 0)
Pi = Movies("Pi", 1996,'drama', 0)
delicatessen = Movies("Delicatessen", 1992, 'comedy/thriller', 0)
breaking_bad = Serials("breaking bad", 2012, 'crime', 3, 45, 0) 
quins_gambit = Serials("Queen's gambit", 2020,'moral/comedy', 1, 7, 0)
mr_bean = Serials("Mr Bean", 1994, 'comedy', 1, 110, 0) 
movies.append(pulp_fiction)
movies.append(killing_zoe)
movies.append(amelie)
movies.append(trainspotting)
movies.append(Pi)
movies.append(delicatessen)
serials.append(breaking_bad)
serials.append(quins_gambit)
serials.append(mr_bean)


def search(name):
    for key_name in movies:
        if key_name == name:
            movie_data = key_name[name]
            play(num_plays)
            return movie_data, num_plays


def titles_list():
    print('Lista dostepnych filmów')
    print('   Tytuł    \tRok prod.\tgatunek\tsezony\todcinki')
    print('------------\t---------\t-------\t------\t-------')
    for movie in movies:
        print(movie)
    for serial in serials:
        print(serial)


#search(name = "Pi")
titles_list()



