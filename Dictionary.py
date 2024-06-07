import pandas as pd

# Read the .xlsx file
df = pd.read_excel('NFL Schedule.xlsx')

# If the Excel file does not contain headers, you can add them
df.columns = ['Team'] + [f'Opponent_{i}' for i in range(1, 19)]  # Adjust as necessary

# Create a dictionary where the keys are the week numbers and the values are tuples of the team and its opponent
week_opponents = {}

# Iterate over the DataFrame
for index, row in df.iterrows():
    # Get the team name from the 'Team' column
    team = row['Team']

    # Get the opponents from the 'Opponent' columns
    opponents = row['Opponent_1':'Opponent_18']  # Adjust as necessary

    # Iterate over the opponents
    for i, opponent in enumerate(opponents, start=1):
        # If the opponent's name starts with '@', skip creating the tuple for that matchup
        if not str(opponent).startswith('@'):
            # Create a tuple of the team and its opponent
            matchup = (team, opponent)

            # If the week is not in the dictionary, add it with a list containing the matchup
            if i not in week_opponents:
                week_opponents[i] = [matchup]
            # If the week is already in the dictionary and the matchup is not already in the list, append the matchup to the list
            elif matchup not in week_opponents[i]:
                week_opponents[i].append(matchup)


for week, matchups in week_opponents.items():
    print(f"Week {week}: {matchups}")

