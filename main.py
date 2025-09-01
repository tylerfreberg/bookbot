from stats import get_num_words, get_num_char, sort_dict
import sys

def get_book_text(book):
	with open(book) as f:
		file_contents = f.read()
	return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	bookpath = sys.argv[1]
	book = get_book_text(bookpath)
	num_words = get_num_words(book)
	sorted_dict = sort_dict(get_num_char(book))

	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for dict in sorted_dict:
		print(f"{dict["char"]}: {dict["num"]}")
	print("============= END ===============")

main()
