import random
import argparse

def cap(input_str):
	output_str = " "
	for character in input_str:
		num = random.randint(0,1)
		if num == 1:
			character = character.upper()
		output_str += character
	return output_str

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Convert string with inconsistent capitalization")
	parser.add_argument('text', help='Input string')
	args = parser.parse_args()

	print(cap(args.text))