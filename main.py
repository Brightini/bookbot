#!/usr/bin/python3
""" This program counts the number of words in a text """

def main():
	book_path = "books/frankenstein.txt"
	text = get_text(book_path)
	count = get_word_count(text)
	print(count)


def get_word_count(text):
	word_count = text.split()
	return len(word_count)

def get_text(path):
	with open(path, "r") as file:
		return file.read()

main()
