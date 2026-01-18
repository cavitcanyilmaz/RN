# test_rnnsequence.py
"""
Tests for RNNSequence module.
"""

import unittest
from rnnsequence import RNNSequence

class TestRNNSequence(unittest.TestCase):
    """Test cases for RNNSequence class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RNNSequence()
        self.assertIsInstance(instance, RNNSequence)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RNNSequence()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
