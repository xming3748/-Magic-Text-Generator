# -*- coding: utf-8 -*-
"""
Magic Text Generator - Simplified Version
Version: 1.0.0
Warning: This tool generates text with special Unicode characters that may not be supported on all platforms and could potentially cause account restrictions. Use at your own risk.
"""

import re

def make_magic_text(visible_part, hidden_part):
    control_chars = '\u2067\u2061\u2067\u2061\u2067'
    return f"{visible_part}{control_chars}{hidden_part}\u2067\u2061"

def main():
    print("WARNING: This tool generates text with special Unicode characters.")
    print("These characters may not be supported on all platforms and could potentially cause account restrictions.")
    print("Use at your own risk.\n")
    
    visible_text = input("Enter front text: ")
    hidden_text = input("Enter hidden text: ")
    
    result = make_magic_text(visible_text, hidden_text)
    
    print("\nGenerated text:")
    print("-" * 40)
    print(result)
    print("-" * 40)
    print("Copy the text above for use.")

if __name__ == "__main__":
    main()