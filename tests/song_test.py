import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Heart Don't Stand a Chance", "Anderson .Paak")
    
    def test_song_has_name(self):
        actual = self.song.name
        expected = "Heart Don't Stand a Chance"
        self.assertEqual(expected, actual)
    
    def test_song_has_artist(self):
        actual = self.song.artist
        expected = "Anderson .Paak"
        self.assertEqual(expected, actual)