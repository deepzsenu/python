def decor(func):
	def wrap():
 		print("============")

		func()
			print("============")
    return wrap

def print_text():

	print(x)

x = input()
	
decorated = decor(print_text)
decorated()
