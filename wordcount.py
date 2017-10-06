#!/usr/bin/python

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def read_file(filename):
	dict = {}
	f = open(filename, "rU")
	for line in f:
		l = line.split()
		for word in l:
			word = word.strip()
			word = word.lower()
			#global dict
			if dict.get(word):
				dict[word] = dict[word] + 1
			else:
				dict[word] = 1
	f.close()				
	return dict

def myFn(t):
	return t[1]

def print_words(filename):
	dict = read_file(filename)
	for k, v in sorted(dict.items()):
		print k,v



def print_top(filename):
	dict = read_file(filename)
	l = sorted(dict.items(), key=myFn, reverse=True)
	for k, v in l[:20]:
		print k, v

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
	print 'usage: ./wordcount.py {--count | --topcount} file'
	sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
	print_words(filename)
  elif option == '--topcount':
	print_top(filename)
  else:
	print 'unknown option: ' + option
	sys.exit(1)

if __name__ == '__main__':
	main()
