# Initialize logical variables to store the answers
interested_in_computer_science = None
like_playing_computer_games = None
has_instagram_account = None

# Ask the survey questions and record the answers
interested_in_computer_science = input("Are you interested in computer science? (Y/N): ").strip().lower() == "y"
like_playing_computer_games = input("Do you like playing computer games? (Y/N): ").strip().lower() == "y"
has_instagram_account = input("Do you have an Instagram account? (Y/N): ").strip().lower() == "y"

# Display the survey results
print("Survey Results:")
print("Interested in computer science:", "Yes" if interested_in_computer_science else "No")
print("Playing computer games:", "Yes" if like_playing_computer_games else "No")
print("Has an Instagram account:", "Yes" if has_instagram_account else "No")
