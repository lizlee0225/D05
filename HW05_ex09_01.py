#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body

def twenty_chr():
	fin = open('words.txt')
	for line in fin:
		lst_words = line.split()
		for word in lst_words:
			if len(word) > 20:
				print(word)



##############################################################################
def main():
    twenty_chr() # Call your functions here.

if __name__ == '__main__':
    main()
