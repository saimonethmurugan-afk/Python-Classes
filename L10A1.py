#Music PLaylist

class Playlist:
    def __init__(self,name,genre):
        self.name = name
        self.genre =genre
        print(f"Playlist {self.name} of {self.genre} is ready!")

my_mix = Playlist("My Mix","Pop")