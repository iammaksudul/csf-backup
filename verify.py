#!/usr/bin/env python3
"""
Verification script to demonstrate the implementation works
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and show the results"""
    print(f"\n=== {description} ===")
    print(f"Command: {cmd}")
    print("Output:")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd='/workspace')
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}")
        print(f"Return code: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"Exception: {e}")
        return False

def main():
    """Main verification function"""
    print("Verifying the 'test Hi' implementation...")
    
    # Test the main program
    success1 = run_command("python3 main.py", "Running main program")
    
    # Test the test suite
    success2 = run_command("python3 test_main.py -v", "Running tests")
    
    # Summary
    print(f"\n=== Summary ===")
    print(f"Main program: {'✓ PASS' if success1 else '✗ FAIL'}")
    print(f"Tests: {'✓ PASS' if success2 else '✗ FAIL'}")
    
    if success1 and success2:
        print("\n🎉 All tests passed! The implementation successfully fulfills the 'test Hi' requirement.")
    else:
        print("\n❌ Some tests failed. Please check the output above.")

if __name__ == "__main__":
    main()