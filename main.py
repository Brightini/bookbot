#!/usr/bin/python3
""" This program counts the number of words in a text """

with open("books/frankenstein.txt", "r") as file:
	file_content = file.read()

word_count = len(file_content.split())
print(word_count)
