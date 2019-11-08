#Home by Morgan Williams

def myHome(family, gone):
	for love in family:
		print(love, end="")
		if(love == "Sister"):
			continue
		print(" <3 ", end="")
	print(gone)

def Departures(family, changes):
	myhome = "happy"
	print("Time moves forward")
	if(changes == False):
		family.pop()
		myHome(family, "")

	if(changes == True):
		family.pop()
		myHome(family, "")

	return family

my_home = ["Home", "Mom", "Me", "Sister"]
myHome(my_home, "");

for living in my_home:
	if(len(my_home) > 2):
		desire = False
		my_home = Departures(my_home, desire)

	if(len(my_home) == 2):
		desire = True
		my_home = Departures(my_home, desire)

	if(len(my_home) == 1):
		break


