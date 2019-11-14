import argparse # parser for command-line options
from characters import CHARACTERS

def convert_str_to_emoji(input, emoji):
	input.

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	try:
		output = convert_str_to_emoji(args.text, emojis=args.emojis)
		print(output)