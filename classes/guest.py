class Guest:
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet
    
    def perform_song(self, song):
        return f"I am singing {song.name} by {song.artist}!"