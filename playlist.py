#A music playlist where I can add,delete and list my favourite songs
class Playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]

    def add_song(self,song):
        self.songs.append(song)
        print(f"Added:{song}")
    
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed:{song}")
        else:
            return f"Song {song} is not in the {self.name} playlist"
        
    def show_songs(self):
        print(f"\nPlaylist-{self.name}:")
        for song in self.songs:
            print(f"{song}")
        
#Make two playlist and add,delete or show songs
playlist1=Playlist("Quran")
print(playlist1.add_song("Islam Sobhi-Baqarah"))
print(playlist1.add_song("Islam Sobhi-Luqman"))
print(playlist1.add_song("Islam Sobhi-Jathiyah"))
playlist1.show_songs()