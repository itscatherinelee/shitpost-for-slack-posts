import argparse # parser for command-line options
from Characters import CHARACTERS

def convert_arr_to_character(input_character, input_emoji):
	if input_character == ' ':
		return '\n\n\n\n\n\n\n\n'
	arr = CHARACTERS[input_character]
	output_character = ' '
	for row in arr:
		for col in row:
			if (col == 1): 
				output_character += input_emoji
			else:
				output_character += "     "
		output_character += '\n'
	output_character += '\n\n'
	return output_character

def convert_str_to_emoji(input_str, input_emoji):
	input_str = input_str.lower() #maybe in the future i would do uppercase and lowercase
	#want to have all the strings that are input turn into the arrays
	
	#disect the string into characters and convert_arr_to_character(input_characters)
	output_emoji_str = ' '
	for character in input_str:
		output_emoji_str += convert_arr_to_character(character, input_emoji)
	return output_emoji_str

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Convert your string into emojis")
	parser.add_argument('text', help='The text to emoji-fy')
	parser.add_argument('emoji', help='The choosen emoji')
	# parser.add_argument('-e', '--emojis')
	
	args = parser.parse_args()
	#stringInput, emojiNameString
	try:
		output = convert_str_to_emoji(args.text, args.emoji)
		print(output)
	except ValueError as e:
		print("catherine doesnt want to deal with this right now")