import math
import rules

def main():
	print()
	print("This program was made for MATH 1220's final project.")
	print("As a result, it is quickly coded and not very flexible.")
	print("Please note that all results are rounded to 5 decimal places.")
	print()
	print("Source code available at https://github.com/NeonWizard/MATH1220-Approximate-Integration")

	print()
	print()

	N = int(input("Please enter how many slices you want to take (N): "))
	a = float(input("Please enter the lower integration bound (a): "))
	b = float(input("Please enter the upper integration bound (a): "))

	rules.left_endpoint(N, a, b, lambda x: x**2)

if __name__ == "__main__":
	main()
