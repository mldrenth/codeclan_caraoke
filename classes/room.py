class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.playlist = []
        self.list_of_guests = []
    
    def add_song(self,song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        self.list_of_guests.append(guest)
    
    def check_out_guest(self, guest):
        self.list_of_guests.remove(guest)