from sys import exit()
colors = {
	"black"		:"\033[1;30m",
	"red"		:"\033[1;31m",
	"green"		:"\033[1;32m",
	"yellow"	:"\033[1;33m",
	"blue"		:"\033[1;34m",
	"magenta"	:"\033[1;35m",
	"cyan"		:"\033[1;36m",
}



def printf(text, color):
	try:
		text = colors[color] + text + "\033[0m"
		print(text)
	except:
		print(text)
		
def inputf(text, color):
	try:
		text = colors[color] + text + "\033[0m"
		colored_prompt = input(text)
		return colored_prompt
	except EOFError: exit()
	except:
		return input(text)
		
def print_error(text):
	first = "\033[7;31m" + "\nError:" + "\033[0m"
	rest  = "\033[1;31m " + text + "\033[0m"
	print(first + rest)
		
