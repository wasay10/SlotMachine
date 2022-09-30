import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}  

symbol_value = {
    "A": 10,
    "B": 5,
    "C": 3,
    "D": 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def getSlotMachineSpin(rows, cols, symbols):
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

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ") 
            else:
                print(column[row], end = "")
        
        print()
            
def deposit():
    while True:
        amount = input("Enter your amount of deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount has to be greater than 0.")
        else:
            print("Please enter a valid number.")
    
    return amount

def getNumberOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
            )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines


def getBet():
    while True:
        amount = input("What would you like to bet on each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount has to be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    
    return amount
  
def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You have an insufficient balance to bet that amount. You current balance is: ${balance}")
        else:
            break
            
    print(f"You are about to bet, ${bet} on {lines} lines. Your total bet is: ${total_bet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    printSlotMachine(slots)
    winnings, winning_lines = checkWinnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines: ", *winning_lines)    
    return winnings - total_bet
    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)   
        
    print(f"Final balance: ${balance}. L.")
    
main()