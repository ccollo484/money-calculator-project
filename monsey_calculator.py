#initialise a variable total_money that stores the overall amount of money
total_money = 0

#loop until user enter "quit"
while True:
    #code to add money here
    money_input = input("Enter amount of money to add here (or type 'quit' to exit): ")
    
    if money_input.lower() == 'quit':
        break

    money = float(money_input)

    total_money += money
    #short way of writing total_money = total_money + money

    print(f"Total amount of money: {total_money}")
