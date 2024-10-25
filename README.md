# Prisoners Dilemma Simulator
This Python program simulates the Prisoner's Dilemma game, allowing players to choose between different prisoner strategies (Cooperator, Defector, Revenger).

The game runs for a specified number of rounds, with a brief delay between each round, and includes an option to view descriptions of each strategy before starting.

## Features

- **Three Strategies**:
  - **Cooperator**: Always cooperates.
  - **Defector**: Always defects.
  - **Revenger**: Cooperates until the opponent defects, then always defects afterward.
  
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

## Code Overview

### `Prisoner` Class

The `Prisoner` class contains a strategy and a revenger mode. Depending on the strategy, the prisoner chooses to cooperate or defect in each round.

- **Attributes**:
  - `strategy`: Defines the strategy the prisoner follows (cooperator, defector, or revenger).
  - `revenger_mode`: Activated if the prisoner is in "revenger" mode and the opponent defects.

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
