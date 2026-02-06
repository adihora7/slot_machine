import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    for line in range(lines):
        symbol = columns[0][line]


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')

        print()


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
            lines = int(
                input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? '))
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
    while True:
        bet = get_bet()
        total_bet = round(bet*lines, 2)

        if total_bet > balance:
            print(
                f'You do not have enough to bet that amount, your current balance is ${balance}')
        else:
            break

    print(
        f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
