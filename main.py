dict_list = []

def sort_on(dict):
	return dict['num']

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		words = file_contents.split()
		word_count = len(words)
		print("--- Begin report of books/frankenstein.txt ---")
		print(f"{word_count} words found in the document")

		my_dict = {}

		for char in file_contents.lower():
			if char in my_dict:
				my_dict[char] += 1
			else:
				my_dict[char] = 1
		for character, count in my_dict.items():
			if character.isalpha():
				char_dict = {'char': character, 'num': count}
				dict_list.append(char_dict)

		dict_list.sort(reverse=True, key=sort_on)
		for item in dict_list:
			print(f"The '{item['char']}' character was found {item['num']} times")
		
	
if __name__ == "__main__":	
	main()