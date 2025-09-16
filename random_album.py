import os
import random
import re

# Function to parse and display album details
def parse_and_display_line(line):
    # Handle quoted fields (i.e., "Rock, Classic") and split by commas
    fields = re.findall(r'\"([^\"]+)\"|([^,]+)', line.strip())
    # Flatten the tuple list and strip spaces
    fields = [f[0] if f[0] else f[1] for f in fields]
    
    # Define the genre and handle "Rock" subgenres
    genre = fields[0]

    # If genre is "Rock", check for subgenres
    rock_subgenres = ["Classic", "Indie", "Psych", "Soft"]
    if genre == "Rock" and len(fields) > 1:
        subgenre = fields[1].strip()
        if subgenre in rock_subgenres:
            genre = "Rock, " + subgenre
            fields = fields[2:]  # Skip the subgenre from further processing

    # Now extract Artist, Album, and Release Date from the remaining fields
    try:
        # Skip empty fields
        fields = [field.strip() for field in fields if field]

        # Assign Artist, Album, and Release Date
        artist = fields[1] if len(fields) > 1 else "Unknown Artist"
        album = fields[2] if len(fields) > 2 else "Unknown Album"
        release_date = fields[3] if len(fields) > 3 else "Unknown Release Date"

        # Display the parsed fields
        print("Genre       : {}".format(genre))
        print("Artist      : {}".format(artist))
        print("Album       : {}".format(album))
        print("Release Date: {}".format(release_date))
    except IndexError:
        print("Invalid line format. Skipping...")

# Function to display a random album based on genre
def display_random_album_by_genre(file_path, genre_choice):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found: {}".format(file_path))
        return

    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter lines by genre
    filtered_lines = [line for line in lines if genre_choice in line]

    # Display a random album from the filtered genre
    if filtered_lines:
        random_line = random.choice(filtered_lines)
        parse_and_display_line(random_line)
    else:
        print("No albums found for this genre.")

# Function to display the menu and handle user input
def display_random_line(file_path):
    genres = {
        'b': 'Bluegrass',
        'r': 'Rock',
        'e': 'Electronic',
        'h': 'Hip Hop',
        'j': 'Jazz',
        'c': 'Comedy',
        'n': 'Concertos',
        'o': 'Folk',
        'f': 'Funk/Soul',
        'p': 'Punk',
        's': 'Soundtrack'
    }

    while True:
        # Display the menu
        print("\nPress Enter for a random album.")
        print("For a random album by genre, press letter:")
        print("(B)luegrass   (R)ock   (E)lectronic   (H)ip-hop")
        print("(J)azz   (C)omedy   Co(n)certos   F(o)lk")
        print("(F)unk/Soul   (S)oundtrack   (P)unk")
        print("\n'control q' to quit.")

        # Wait for user input
        user_input = raw_input().lower()

        # Clear the screen after the user makes a choice
        if user_input == 'q':
            print("Goodbye!")
            break
        elif user_input == '':
            # If Enter is pressed, display a random album from any genre
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if lines:
                    random_line = random.choice(lines)
                    os.system('clear' if os.name != 'nt' else 'cls')
                    parse_and_display_line(random_line)
                else:
                    print("The file is empty.")
                    break
        elif user_input in genres:
            genre_choice = genres[user_input]
            # Display the selected genre album
            os.system('clear' if os.name != 'nt' else 'cls')
            display_random_album_by_genre(file_path, genre_choice)
        else:
            print("Invalid option. Please press a valid key.")

file_path = '/home/chip/VinylProject/vinyl.csv'

# Run the program
display_random_line(file_path)
