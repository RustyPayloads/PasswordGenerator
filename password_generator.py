import random
import string

def generate_password(length=12):
    """
    Generates a random password of a specified length.

    The password includes a mix of uppercase letters, lowercase letters,
    digits, and punctuation characters.
    """
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one of each character type for strength
    # Start the password with one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length with random choices from all characters
    if length > 4:
        # Generate the remaining characters
        remaining_length = length - len(password)
        password.extend(random.choices(characters, k=remaining_length))

    # Shuffle the list to ensure the character types aren't always at the start
    random.shuffle(password)

    # Join the list of characters into a final string
    return "".join(password)

# --- Main execution block ---
if __name__ == "__main__":
    try:
        # Prompt the user for the desired length
        # Defaulting to 12 if no valid input is provided or is too short
        default_length = 12
        
        while True:
            length_input = input(f"Enter the desired password length (min 4, default {default_length}): ")
            if not length_input:
                password_length = default_length
                break
            try:
                password_length = int(length_input)
                if password_length >= 4:
                    break
                else:
                    print("Length must be 4 or more. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        # Generate and print the password
        strong_password = generate_password(password_length)
        
        print("\n🔒 Generated Password:")
        print(f"**{strong_password}**")
        print(f"Length: {len(strong_password)}")

    except Exception as e:
        print(f"An error occurred: {e}")
