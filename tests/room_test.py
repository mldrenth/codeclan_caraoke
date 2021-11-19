import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Hip Hop", 3)
        self.song = Song("Heart Don't Stand a Chance", "Anderson .Paak")
        self.guest = Guest("Frodo", "Heart Don't Stand a Chance", 100)
    
    def test_room_has_name(self):
        actual = self.room.name
        expected = "Hip Hop"
        self.assertEqual(expected, actual)
    
    def test_room_has_size(self):
        actual = self.room.size
        expected = 3
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
    
    

    
