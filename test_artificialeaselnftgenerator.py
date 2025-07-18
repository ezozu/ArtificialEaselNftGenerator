# test_artificialeaselnftgenerator.py
"""
Tests for ArtificialEaselNftGenerator module.
"""

import unittest
from artificialeaselnftgenerator import ArtificialEaselNftGenerator

class TestArtificialEaselNftGenerator(unittest.TestCase):
    """Test cases for ArtificialEaselNftGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselNftGenerator()
        self.assertIsInstance(instance, ArtificialEaselNftGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselNftGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
