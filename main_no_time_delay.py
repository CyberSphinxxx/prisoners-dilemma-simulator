import random

class Prisoner:
    def __init__(self, strategy):
        self.strategy = strategy
        self.revenger_mode = False

    def choose(self, opponent_last_choice=None):
        if self.strategy == 'cooperator':
            return 'cooperate'
        
        elif self.strategy == 'defector':
            return 'defect'
        
        elif self.strategy == 'revenger':
            if self.revenger_mode:
                return 'defect'
            elif opponent_last_choice == 'defect':
                self.revenger_mode = True
                return 'defect'
            else:
                return 'cooperate'
        
        elif self.strategy == 'tit_for_tat':
            if opponent_last_choice is None:
                return 'cooperate'
            else:
                return opponent_last_choice

        else:
            raise ValueError("Unknown strategy!")

def prisoners_dilemma(prisoner_a, prisoner_b, rounds=1):
    a_points, b_points = 0, 0
    last_a_choice, last_b_choice = None, None

    for _ in range(rounds):
        a_choice = prisoner_a.choose(last_b_choice)
        b_choice = prisoner_b.choose(last_a_choice)

        if a_choice == 'cooperate' and b_choice == 'cooperate':
            a_points += 1
            b_points += 1

        elif a_choice == 'cooperate' and b_choice == 'defect':
            b_points += 4

        elif a_choice == 'defect' and b_choice == 'cooperate':
            a_points += 4

        elif a_choice == 'defect' and b_choice == 'defect':
            a_points += 2
            b_points += 2

        last_a_choice = a_choice
        last_b_choice = b_choice

    return a_points, b_points

# Define strategies
strategies = {1: 'cooperator', 2: 'defector', 3: 'revenger', 4: 'tit_for_tat'}

# Game setup
print("Choose your prisoner type:")
print("1. Cooperator")
print("2. Defector")
print("3. Revenger")
print("4. Tit-for-Tat")

prisoner_a_choice = int(input("Choose strategy for Prisoner A (1-4): "))
prisoner_b_choice = int(input("Choose strategy for Prisoner B (1-4): "))

# Create prisoner instances
prisoner_a = Prisoner(strategies[prisoner_a_choice])
prisoner_b = Prisoner(strategies[prisoner_b_choice])

# Run the simulation
rounds = int(input("Enter the number of rounds to simulate: "))
a_points, b_points = prisoners_dilemma(prisoner_a, prisoner_b, rounds)

# Display results
print(f"\nAfter {rounds} rounds:")
print(f"Prisoner A ({strategies[prisoner_a_choice]}): {a_points} points")
print(f"Prisoner B ({strategies[prisoner_b_choice]}): {b_points} points")
