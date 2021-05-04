import math
import sys

import rules

def getValues():
	n = int(input("Please enter how many slices you want to take (N): "))
	a = float(input("Please enter the lower integration bound (a): "))
	b = float(input("Please enter the upper integration bound (a): "))

	# pls don't hack me
	string = input("Please enter a mathematical function in terms of x: ")
	function = lambda x: eval(string)

	return (n, a, b, function)

def main():
	print()
	print("This program was made for MATH 1220's final project.")
	print("As a result, it is quickly coded and not very flexible.")
	print("Please note that all results are rounded to 5 decimal places.")
	print()
	print("Source code available at https://github.com/NeonWizard/MATH1220-Approximate-Integration")

	print()
	print()

	while True:
		n, a, b, function = getValues()

		integrating = True
		while integrating:
			print()
			print("Choose which rule to use: ")
			print("[1] Left endpoint")
			print("[2] Right endpoint")
			print("[3] Midpoint")
			print("[4] Trapezoidal")
			print("[5] Simpsons")
			print("[6] Enter different values")
			print("[7] Exit")

			choice = int(input("> "))
			print()

			while True:
				if choice == 1:
					val = rules.left_endpoint(n, a, b, function)
				elif choice == 2:
					val = rules.right_endpoint(n, a, b, function)
				elif choice == 3:
					val = rules.midpoint(n, a, b, function)
				elif choice == 4:
					val = rules.trapezoidal(n, a, b, function)
				elif choice == 5:
					val = rules.simpsons(n, a, b, function)
				elif choice == 6:
					integrating = False
				elif choice == 7:
					sys.exit(0)
				else:
					print("Please enter a valid choice.")
					continue
				break

			if not integrating: break

			if val != None:
				print(f"Result: {val}")

			input("Press enter to continue...")


if __name__ == "__main__":
	main()
