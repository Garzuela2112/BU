# Example Program that conversts gallons to liters

def main ():
	# list instructions
	intro ()

try:
  
# get gallons to liters
  
	gallons_needed = float(input("gallons to liters: "))

	
# convert gallons to liters
gallons_to_liters(gallons_needed)

except ValueError:
		print("Error: try again using only numbers")
		print()
		main()

def intro():
	print("This program converts gallons to liters")
	print("Gallons to Liters")
	print("1 gallon = 1.7854 liters")
	print()

# shows gallons_to_liters function accepts a number of 
# liters and displays the equivalent number of gallons.
def gallons_to_liters(gallons):
	liters = gallons * 3.7854
	print("converts to {:.3f} liters.".format(liters))

	main()

	