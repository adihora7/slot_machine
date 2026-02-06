MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        try:
            amount = float(input('What would you like to deposit? $'))

            if amount > 0:
                break
            else:
                print('Amount must be a positive number.')

        except ValueError:
            print('Please enter a valid number.')
    return amount


def get_number_of_lines():
    while True:
        try:
            lines = float(
                input('Enter the number of lines to bet on (1- ' + str(MAX_LINES) + ')? '))
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')

        except ValueError:
            print('Please enter a valid number.')
    return lines


def get_bet():
    while True:
        try:
            amount = float(
                input('What would you like to bet on each line? $'))
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')

        except ValueError:
            print('Please enter a valid number.')
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

    print(balance, lines)


main()
