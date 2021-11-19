class Room:
    def __init__(self, name, size, till, fee):
        self.name = name
        self.size = size
        self.till = till
        self.fee = fee
        self.playlist = []
        self.list_of_guests = []
       
    
    def add_song(self,song):
        self.playlist.append(song)

    def check_in_guest(self, guest):
        if self.find_space() and self.check_money(guest):
            self.take_fee()
            guest.pay_fee(self.fee)
            self.list_of_guests.append(guest)
    
    def check_out_guest(self, guest):
        self.list_of_guests.remove(guest)
    
    def check_money(self,guest):
        return guest.wallet >= self.fee
    
    def find_space(self):
        return len(self.list_of_guests) < self.size
    
    def take_fee(self):
        self.till += self.fee
