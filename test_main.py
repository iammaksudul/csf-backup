#!/usr/bin/env python3
"""
Test file for the main.py program
"""

import unittest
import sys
import os
from io import StringIO

# Add the current directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import main

class TestHi(unittest.TestCase):
    """Test cases for the Hi functionality"""
    
    def test_say_hi_returns_hi(self):
        """Test that say_hi() returns 'Hi'"""
        result = main.say_hi()
        self.assertEqual(result, "Hi")
    
    def test_main_prints_hi(self):
        """Test that main() prints 'Hi'"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            main.main()
            output = captured_output.getvalue().strip()
            self.assertEqual(output, "Hi")
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()