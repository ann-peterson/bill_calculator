def calculate_tip(bill_amount, tip_percentage):
	tip = bill_amount * tip_percentage * .01
	return tip

def total_bill(bill_amount, tip):
	bill = bill_amount + tip
	return bill

def split_bill(bill_amount, num_of_people):
	split_bill = bill_amount / num_of_people
	return split_bill


def main():
	choice = raw_input("Choose '1' to calculate the tip or '2' to split the bill.")
	bill_amount = float(raw_input("How much is the bill?"))
	tip_percentage = float(raw_input("How much would you like to tip?"))
	if choice == "1":
		tip = calculate_tip(bill_amount, tip_percentage)

		bill = total_bill(bill_amount, tip)

		print bill

	# elif:

	






if __name__ == '__main__':
	main()