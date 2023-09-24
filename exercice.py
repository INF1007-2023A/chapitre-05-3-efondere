#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	sum = 0
	for c in text:
		if c.isalnum():
			sum += 1
	return sum

def get_word_length_histogram(text):
	length_data = []
	longest = 0
	for word in text.split():
		length = get_num_letters(word)
		length_data.append(length)
		if length > longest:
			longest = length

	histogram_data = [0 for _ in range(longest + 1)]
	for length in length_data:
		histogram_data[length] += 1

	return histogram_data

def format_histogram(histogram):
	ROW_CHAR = "*"
	alignment = len(str(len(histogram) - 1))
	result = ""
	for i in range(1, len(histogram)):
		histogram_bar = ROW_CHAR * histogram[i]
		result += f"{i:>{alignment}} {histogram_bar}\n"

	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	max_value = 0
	for value in histogram:
		if value > max_value:
			max_value = value

	result = ""
	for y in range(max_value, 0, -1):
		for x in range(1, len(histogram)):
			if histogram[x] >= y:
				result += BLOCK_CHAR
			else:
				result += " "
		result += "\n"

	result += LINE_CHAR * len(histogram)
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
