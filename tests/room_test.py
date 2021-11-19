import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hip Hop", 3, 200, 20)
        self.song = Song("Heart Don't Stand a Chance", "Anderson .Paak")
        self.guest = Guest("Frodo", "Heart Don't Stand a Chance", 100)
        self.guest_2 = Guest("Sam", "Magic", 10)
        self.guest_3 = Guest("Pippin", "Slow Dancing in a Burning Room", 50)
        self.guest_4 = Guest("Merry", "Next Girl", 20 )
    
    def test_room_has_name(self):
        actual = self.room.name
        expected = "Hip Hop"
        self.assertEqual(expected, actual)
    
    def test_room_has_size(self):
        actual = self.room.size
        expected = 3
        self.assertEqual(expected, actual)
    
    def test_room_has_till(self):
        actual = self.room.till
        expected = 200
        self.assertEqual(expected, actual)
    
    def test_room_has_fee(self):
        actual = self.room.fee
        expected = 20
        self.assertEqual(expected, actual)
    
    def test_room_can_add_song_to_playlist(self):
        self.room.add_song(self.song)
        actual = len(self.room.playlist)
        expected = 1
        self.assertEqual(expected, actual)
    
    def test_room_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        actual = len(self.room.list_of_guests)
        expected = 1
        self.assertEqual(expected,actual)
    
    def test_room_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        actual = len(self.room.list_of_guests)
        expected = 0
        self.assertEqual(expected,actual)
    
    def test_room_is_full(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_4)
        actual = len(self.room.list_of_guests)
        expected = 3
        self.assertEqual(expected, actual)
    
    def test_room__has_favourite_song(self):
        self.room.add_song(self.song)
        actual = self.guest.cheer(self.room.playlist)
        expected = "Whoo!"
        self.assertEqual(expected, actual)
    
    def test_room__does_not_have_favourite_song(self):
        self.room.add_song(self.song)
        actual = self.guest_2.cheer(self.room.playlist)
        expected = None
        self.assertEqual(expected, actual)
    
    def test_room__guest_has_enough_money(self):
        self.room.add_song(self.song)
        self.room.check_in_guest(self.guest)
        self.assertEqual(220, self.room.till)
        self.assertEqual(80, self.guest.wallet)
        self.assertEqual(1, len(self.room.list_of_guests))
    
    def test_room__guest_not_enough_money(self):
        self.room.add_song(self.song)
        self.room.check_in_guest(self.guest_2)
        self.assertEqual(200, self.room.till)
        self.assertEqual(10, self.guest_2.wallet)
        self.assertEqual(0, len(self.room.list_of_guests))
        

    

    
