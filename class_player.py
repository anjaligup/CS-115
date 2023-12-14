class Player:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.instruments = []
        
    def __str__(self):
        '''The artist and their instruments'''
        return "Artist " + self.name + " plays " + ", ".join(self.instruments)

    def copy(self):
        p = Player(self.name, self.genre)
        p.instruments = list(self.instruments)
        return p

    def addInst(self, instrument):
        self.instruments.append(instrument)

    def __eq__(self, other):
        if self.name != other.name or self.genre != other.genre:
            return False
        else:
            sortedSelf = sorted(self.instruments)
            sortedOther = sorted(other.instruments)
            if sortedSelf == sortedOther:
                return True 
