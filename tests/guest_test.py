import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Frodo", "Heart Don't Stand a Chance", 100)
        self.song = Song("Heart Don't Stand a Chance", "Anderson .Paak")
    
    def test_guest_has_name(self):
        actual = self.guest.name
        expected = "Frodo"
        self.assertEqual(expected, actual)

    def test_guest_has_favourite_song(self):
        actual = self.guest.favourite_song
        expected = "Heart Don't Stand a Chance"
        self.assertEqual(expected, actual)
    
    def test_guest_has_wallet(self):
        actual = self.guest.wallet
        expected = 100
        self.assertEqual(expected, actual)
    
    def test_guest_can_perform_song(self):
        actual = self.guest.perform_song(self.song)
        expected = "I am singing Heart Don't Stand a Chance by Anderson .Paak!"
        self.assertEqual(expected, actual)