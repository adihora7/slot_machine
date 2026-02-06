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

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return round(winnings, 2), winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count

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
        print(" | ".join(column[row] for column in columns))


def deposit():
    while True:
        try:
            amount = float(input('What would you like to deposit? $'))
            if amount > 0:
                return round(amount, 2)
            print('Amount must be greater than 0.')
        except ValueError:
            print('Please enter a valid number.')


def get_number_of_lines():
    while True:
        try:
            lines = int(
                input(f'Enter the number of lines to bet on (1-{MAX_LINES}): '))
            if 1 <= lines <= MAX_LINES:
                return lines
            print('Invalid number of lines.')
        except ValueError:
            print('Please enter a valid integer.')


def get_bet():
    while True:
        try:
            amount = float(input('What would you like to bet on each line? $'))
            if MIN_BET <= amount <= MAX_BET:
                return round(amount, 2)
            print(f'Bet must be between ${MIN_BET} and ${MAX_BET}.')
        except ValueError:
            print('Please enter a valid number.')


def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = round(bet * lines, 2)

        if total_bet <= balance:
            break
        print(f'Insufficient funds. Current balance: ${balance}')

    print(
        f'\nYou are betting ${bet} on {lines} lines. Total bet = ${total_bet}\n')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print(f'\nYou won ${winnings}')
    if winning_lines:
        print('Winning lines:', *winning_lines)
    else:
        print('No winning lines')

    return winnings - total_bet


def main():
    balance = deposit()

    while balance > 0:
        print(f'\nCurrent balance: ${balance}')
        choice = input('Press ENTER to spin (q to quit): ').lower()
        if choice == 'q':
            break

        balance = round(balance + spin(balance), 2)

    if balance <= 0:
        print('\nYou ran out of money!')

    print(f'\nYou left with ${balance}')


main()
