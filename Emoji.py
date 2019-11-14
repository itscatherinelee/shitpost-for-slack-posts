import argparse # parser for command-line options
from Characters import CHARACTERS

# def convert_arr_to_str(character, string, space):
# 	output_str = ' '
# 	for row in arr:
# 		for col in row:
# 			output_str += string if col else space
# 		output_str += '\n'
# 	return output_str

def convert_str_to_emoji(input_str, input_emoji):
	input_str = input_str.lower() #maybe in the future i would do uppercase and lowercase
	#want to have all the strings that are input turn into the arrays
	output_emoji = ' '
	return output_emoji

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Convert your string into emojis")
	parser.add_argument('text', help='The text to emoji-fy')
	parser.add_argument('emoji', help='The choosen emoji')
	# parser.add_argument('-e', '--emojis')
	
	args = parser.parse_args()
	#stringInput, emojiNameString
	try:
		output = convert_str_to_emoji(args.text, args.emoji)
	except ValueError as e:
		print("catherine doesnt want to deal with this right now")