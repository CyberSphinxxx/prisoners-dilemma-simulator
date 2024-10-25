import random
import time

class Prisoner:
    def __init__(self, strategy):
        self.strategy = strategy
        self.revenger_mode = False
        self.round_counter = 0

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
        
        elif self.strategy == 'random':
            return random.choice(['cooperate', 'defect'])
        
        elif self.strategy == 'detective':
            if self.round_counter < 4:
                return 'cooperate' if self.round_counter % 2 == 0 else 'defect'
            else:
                if opponent_last_choice == 'defect':
                    return opponent_last_choice
                else:
                    return 'defect'

        else:
            raise ValueError("Unknown strategy!")

def prisoners_dilemma(prisoner_a, prisoner_b, rounds=1, delay=1):
    a_points, b_points = 0, 0
    last_a_choice, last_b_choice = None, None

    for round_number in range(1, rounds + 1):
        if delay > 0:
            print(f"\nRound {round_number}...")
        
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

        if delay > 0:  # Only print choices if there's a delay
            print(f"Prisoner A chose: {a_choice}, Prisoner B chose: {b_choice}")
            print(f"Current points - Prisoner A: {a_points}, Prisoner B: {b_points}")

        last_a_choice = a_choice
        last_b_choice = b_choice

        # Increment round counter for Detective strategy
        if prisoner_a.strategy == 'detective':
            prisoner_a.round_counter += 1
        if prisoner_b.strategy == 'detective':
            prisoner_b.round_counter += 1

        time.sleep(delay)

    return a_points, b_points

# Define strategies
strategies = {
    1: 'cooperator',
    2: 'defector',
    3: 'revenger',
    4: 'tit_for_tat',
    5: 'random',
    6: 'detective'  # Add Detective to the strategies
}

separator = "=" * 45  # Separator line

while True:  # Loop for simulating again
    # Game setup
    print(separator)  
    print("Choose your prisoner type:")
    print("1. Cooperator")
    print("2. Defector")
    print("3. Revenger")
    print("4. Tit-for-Tat")
    print("5. Random")
    print("6. Detective")
    print(separator)

    # Safety check for prisoner choices
    while True:
        try:
            prisoner_a_choice = int(input("Choose strategy for Prisoner A (1-6): "))
            prisoner_b_choice = int(input("Choose strategy for Prisoner B (1-6): "))
            if prisoner_a_choice in strategies and prisoner_b_choice in strategies:
                break  # Valid choices, exit loop
            else:
                print("Invalid choice! Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(separator)

    # Create prisoner instances
    prisoner_a = Prisoner(strategies[prisoner_a_choice])
    prisoner_b = Prisoner(strategies[prisoner_b_choice])

    # Get number of rounds with a safety check
    while True:
        try:
            rounds = int(input("Enter the number of rounds to simulate: "))
            if rounds > 0:
                break
            else:
                print("Number of rounds must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a positive integer.")
    
    print(separator)

    # Ask if the user wants a time delay
    use_delay = input("Add time delay between rounds? (y/n): ").strip().lower()
    print(separator)

    # Set delay based on user input
    delay = 1 if use_delay == 'y' else 0

    # Run the simulation
    a_points, b_points = prisoners_dilemma(prisoner_a, prisoner_b, rounds, delay)

    # Display results
    print(separator)
    print(f"Results after {rounds} rounds:")
    print(f"Prisoner A ({strategies[prisoner_a_choice]}): {a_points} points")
    print(f"Prisoner B ({strategies[prisoner_b_choice]}): {b_points} points")

    # Determine the winner
    if a_points > b_points:
        print("Winner: Prisoner A")
    elif b_points > a_points:
        print("Winner: Prisoner B")
    else:
        print("Result: tie")

    print(separator)

    # Ask if the user wants to simulate again
    simulate_again = input("Do you want to simulate again? (y/n): ").strip().lower()
    if simulate_again != 'y':
        break  # Exit the loop if the user doesn't want to simulate again
