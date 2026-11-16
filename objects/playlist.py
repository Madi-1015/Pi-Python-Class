class Song:
    def __str__(self):
        return f"{self.title}, {self.artist},{self.duration}"
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = int(duration)
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def get_total_duration(self):
        t = 0
        for dur in self.songs:
            t += (dur.duration)
        seconds = t // 60
        minutes = t % 60
        print(f"{minutes:02d}:{seconds:02d}")
    def find_by_artist(self, artist_name):
        for art in self.songs:
            if art.artist == artist_name:
                print(art.title)
    def print_playlist(self):
        for song in self.songs:
            print(song)
    def load_songs(self, filename):
            lines = []
            with open(filename, "r")as f:
                lines = f.readlines()
            for line in lines:
                track = line.split(",")
                song = Song(track[0], track[1], track[2])
                self.add_song(song)

def main():
    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")

main()