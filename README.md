# Prisoners Dilemma Simulator

This Python program simulates the Prisoner's Dilemma, allowing players to choose from various strategies (Cooperator, Defector, Revenger, Tit-for-Tat, Random, and Detective). Players can specify the number of rounds, with an optional delay to observe each round’s interactions.

## Features

- **Six Strategies**:
  - **Cooperator**: Always cooperates.
  - **Defector**: Always defects.
  - **Revenger**: Cooperates until the opponent defects, then always defects afterward.
  - **Tit-for-Tat**: Starts by cooperating, then mimics the opponent's last move.
  - **Random**: Randomly chooses to cooperate or defect each round.
  - **Detective**: Alternates between cooperation and defection for the first four rounds, then switches to Tit-for-Tat if the opponent defects; otherwise, it continues to defect.

- **Point System**:
  - Both prisoners cooperate: +1 point each.
  - One defects while the other cooperates: Defector gets +4 points, cooperator gets 0 points.
  - Both defect: +2 points each.

- **Customizable Rounds**: Specify the number of rounds to simulate.

## How It Works

1. The program asks the user to choose a strategy for each prisoner.
2. It then simulates the selected number of rounds where each prisoner makes a decision to cooperate or defect.
3. Points are awarded based on the prisoners' choices each round.
4. At the end of the simulation, the total points for both prisoners are displayed.

## Sample Output
![Screenshot 2024-10-26 031847](https://github.com/user-attachments/assets/1748b442-3236-49b0-b066-7911d12ac41e)


## Code Overview

### `Prisoner` Class

The `Prisoner` class contains a strategy and a revenger mode. Depending on the strategy, the prisoner chooses to cooperate or defect in each round.

- **Attributes**:
  - `strategy`: Defines the strategy the prisoner follows (cooperator, defector, revenger, tit_for_tat, random, or detective).
  - `revenger_mode`: Activated if the prisoner is in "revenger" mode and the opponent defects.
  - `round_counter`: Tracks the number of rounds for the Detective strategy.

- **Methods**:
  - `choose(opponent_last_choice)`: Determines whether to cooperate or defect based on the chosen strategy.

### `prisoners_dilemma()` Function

This function simulates the Prisoner's Dilemma over a specified number of rounds, using two prisoners and their strategies.

- **Parameters**:
  - `prisoner_a`: Prisoner A's strategy.
  - `prisoner_b`: Prisoner B's strategy.
  - `rounds`: Number of rounds to simulate.

- **Returns**:
  - Points for both prisoners after the rounds are completed.
