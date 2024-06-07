import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

is_paused = False

image_dir = 'G:\\Python\\Logo and weekly opponents\\NFL Logos'
image_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir) if file.endswith('.png')]

root = tk.Tk()
root.configure(bg='black')
root.title("NFL Weekly Matchups")


# Create a label for the week's matchup
week_label = tk.Label(root, text="", font=("Arial", 24), bg='black', fg='white')
week_label.pack(side=tk.TOP)

# Create a Frame to hold the labels
frame = tk.Frame(root, bg='black')
frame.pack(side=tk.TOP)

# Create two labels for the images
label1 = tk.Label(frame, bg='black')
label1.pack(side=tk.LEFT)

# Create a label for the text
text = tk.Label(frame, text="@", font=("Arial", 48), bg='black', fg='white')
text.pack(side=tk.LEFT)

label2 = tk.Label(frame, bg='black')
label2.pack(side=tk.LEFT)

import Dictionary

# Create a dictionary that maps team names to image file names
team_to_image = {
    'ATL': 'nfl-atlanta-falcons-team-logo.png',
    'BUF': 'nfl-buffalo-bills-team-logo.png',
    'CAR': 'nfl-carolina-panthers-team-logo.png',
    'CHI': 'nfl-chicago-bears-team-logo.png',
    'CIN': 'nfl-cincinnati-bengals-team-logo.png',
    'CLE': 'nfl-cleveland-browns-team-logo.png',
    'DAL': 'nfl-dallas-cowboys-team-logo.png',
    'DEN': 'nfl-denver-broncos-team-logo.png',
    'DET': 'nfl-detroit-lions-team-logo.png',
    'GB': 'nfl-green-bay-packers-team-logo.png',
    'HOU': 'nfl-houston-texans-team-logo.png',
    'IND': 'nfl-indianapolis-colts-team-logo.png',
    'JAC': 'nfl-jacksonville-jaguars-team-logo.png',
    'KC': 'nfl-kansas-city-chiefs-team-logo.png',
    'LAC': 'nfl-los-angeles-chargers-team-logo.png',
    'LAR': 'nfl-los-angeles-rams-team-logo.png',
    'LV': 'nfl-las-vegas-raiders-team-logo.png',
    'MIA': 'nfl-miami-dolphins-team-logo.png',
    'MIN': 'nfl-minnesota-vikings-team-logo.png',
    'NE': 'nfl-new-england-patriots-team-logo.png',
    'NO': 'nfl-new-orleans-saints-team-logo.png',
    'NYG': 'nfl-new-york-giants-team-logo.png',
    'NYJ': 'nfl-new-york-jets-team-logo.png',
    'PHI': 'nfl-philadelphia-eagles-team-logo.png',
    'PIT': 'nfl-pittsburgh-steelers-team-logo.png',
    'SEA': 'nfl-seattle-seahawks-team-logo.png',
    'SF': 'nfl-san-francisco-49ers-team-logo.png',
    'TB': 'nfl-tampa-bay-buccaneers-team-logo.png',
    'TEN': 'nfl-tennessee-titans-team-logo.png',
    'WAS': 'nfl-washington-football-team-logo.png',
    'ARI': 'nfl-arizona-cardinals-team-logo.png',
    'BAL': 'nfl-baltimore-ravens-team-logo.png',
}

# Create a Combobox for the week number
week_number = tk.StringVar(value='Week 1')
week_combobox = ttk.Combobox(root, textvariable=week_number, width=10)
week_combobox['values'] = [f"Week {i}" for i in range(1, 18)] + ['All Weeks']  # Add 'All Weeks' to the list
week_combobox.pack(side=tk.TOP)

# Create a dictionary to store the current matchup index for each week
current_matchup_index = {}

# Create a dictionary to store the current matchup index for each week when 'All Weeks' is selected
all_weeks_matchup_index = {}

# Create a list to store all matchups across all weeks
all_matchups = []

# Populate the list with all matchups
for week, matchups in sorted(Dictionary.week_opponents.items()):
    for matchup in matchups:
        all_matchups.append((week, matchup))

# Create a variable to store the current index in the all_matchups list
current_all_matchups_index = 0
# Create a variable to store the previous week number
previous_week_number = None

def update_image():
    # Declare current_all_matchups_index and previous_week_number as global
    global current_all_matchups_index, previous_week_number

    # Check if a week number has been selected
    if not week_number.get():
        return

    # Initialize matchup_index
    matchup_index = 0

    # Check if 'All Weeks' is selected
    if week_number.get() == 'All Weeks':
        # If 'All Weeks' is selected and it was not already selected, reset current_all_matchups_index to 0
        if previous_week_number != 'All Weeks':
            current_all_matchups_index = 0
        # Handle 'All Weeks' selection
        # Get the current matchup from the all_matchups list
        week_number_value, matchup = all_matchups[current_all_matchups_index]
        matchups = [matchup]  # Create a list with the current matchup
        # Increment the current index in the all_matchups list (or reset to 0 if it was at the end)
        current_all_matchups_index = (current_all_matchups_index + 1) % len(all_matchups)
        # Update matchup_index
        matchup_index = all_weeks_matchup_index.get(week_number_value, 0)
    else:
        # Get the current week's matchups
        week_number_value = int(week_number.get().split()[1])
        matchups = Dictionary.week_opponents.get(week_number_value)
        # Update matchup_index
        matchup_index = current_matchup_index.get(week_number_value, 0)


    # Update the previous week number
    previous_week_number = week_number.get()

    if matchups:
        # Get the current matchup
        matchup = matchups[matchup_index]  # Use matchup_index to get the current matchup

        # Get the team names
        team1, team2 = matchup

        # Get the image file names for the team names
        image_file1 = team_to_image.get(team1)
        image_file2 = team_to_image.get(team2)

        if image_file1 and image_file2:
            # Construct the paths to the image files
            image_path1 = os.path.join(image_dir, image_file1)
            image_path2 = os.path.join(image_dir, image_file2)

            try:
                # Update the first image
                image1 = Image.open(image_path1)
                photo1 = ImageTk.PhotoImage(image1)
                label1.config(image=photo1)
                label1.image = photo1  # keep a reference to the image
            except FileNotFoundError:
                print(f"Could not find image file: {image_path1}")
                return

            try:
                # Update the second image
                image2 = Image.open(image_path2)
                photo2 = ImageTk.PhotoImage(image2)
                label2.config(image=photo2)
                label2.image = photo2  # keep a reference to the image
            except FileNotFoundError:
                print(f"Could not find image file: {image_path2}")
                return

            # Update the week's matchup
            week_label.config(text=f"Week {week_number_value}: {team1} vs {team2}")

        # Update the current matchup index for the selected week
        if week_number.get() == 'All Weeks':
            all_weeks_matchup_index[week_number_value] = (matchup_index + 1) % len(matchups)
        else:
            current_matchup_index[week_number_value] = (matchup_index + 1) % len(matchups)

# Initialize update_image.current_image and update_image.current_week
update_image.current_image = 0
update_image.current_week = 1

def auto_update():
    if is_paused:
        return
    update_image()
    root.after(2000, auto_update)  # change image every 2 seconds

def toggle_pause(event):
    # Check if the event was triggered by the combobox
    if event.widget is week_combobox:
        return

    global is_paused
    is_paused = not is_paused
    if is_paused:
        root.title("NFL Weekly Matchups - PAUSED")
    else:
        root.title("NFL Weekly Matchups")
        auto_update()

root.bind("<Button-1>", toggle_pause)

auto_update()
root.mainloop()