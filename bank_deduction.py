balance = 0
amount_deposit = int(input("What amount would you like to deposit:\n"))
balance += amount_deposit

deduction_input = int(input("Amount to be deducted:\n"))
balance_new = balance - deduction_input
print(f"Your new account balance is {balance_new}")
cont_input = input("Would you like to deduct further?\n")

if cont_input == "yes":
    deduction_input = int(input("Amount to be deducted:\n"))
    balance_new2 = balance_new - deduction_input
    print(f"Your new account balance is {balance_new2}")
elif cont_input == "no":
    print("Transaction complete, exiting program!")
else:
    print("Invalid input, please try again!")