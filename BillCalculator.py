def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * (tip_percentage * .01)
    total_bill = bill_amount + tip
    return total_bill


def split_bill (num_of_people, bill):
    split_bill = bill / num_of_people
    return split_bill

def main():
    choice = raw_input("Choose '1' to calculate the tip or '2' to split the bill.")
    if choice == "1":
        bill_amount = float(raw_input("How much is the bill?"))
        tip_percentage = float(raw_input("How much do you want to tip?"))

        print calculate_tip(bill_amount, tip_percentage)

    elif choice == "2":    
        bill_amount = float(raw_input("How much is the bill?"))
        num_of_people = int(raw_input("How many people to split the bill?"))

        print split_bill(num_of_people, bill_amount)

    else:
        print "Not a valid choice. Please enter either 1 or 2."


if __name__ == '__main__':
    main()