# Python Slot Machine Game 🎰

This is a simple command-line **Slot Machine game built in Python**.  
The player deposits money, chooses how many lines to bet on (1-3), places a bet per line, and spins the slot machine. Winnings are calculated based on matching symbols across the selected lines.

---

## Features
- Deposit system with input validation
- Betting on **1 to 3 lines**
- Adjustable bet amount per line
- Random slot machine spins (3x3 grid)
- Different symbols have different probabilities and payout values
- Displays winning lines and updated balance after every spin

---

## How It Works
- The slot machine has **3 rows and 3 columns**
- Symbols have different chances of appearing:
  - A (rare, highest payout)
  - B
  - C
  - D (most common, lowest payout)
- If all 3 symbols match across a chosen line, you win.

---

## Requirements
- Python 3.x

No external libraries are needed.

---

## How To Run
1. Clone the repository:
   `git clone https://github.com/your-username/your-repo-name.git`
2. Navigate into the folder:
   `cd your-repo-name`
3. Run the program:
   `python slot_machine.py`
