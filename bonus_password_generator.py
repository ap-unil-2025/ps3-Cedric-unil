import random
import string


def generate_password(length=12, use_uppercase=True, use_lowercase=True,
                     use_digits=True, use_special=True):
    """
    Generate a random password based on criteria.
    """
    characters = ""
    required = []

    if use_lowercase:
        characters += string.ascii_lowercase
        required.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required.append(random.choice(string.digits))
    if use_special:
        characters += string.punctuation
        required.append(random.choice(string.punctuation))

    if not characters:
        return "Error: No character types selected!"

    # Fill the rest of the password
    remaining_length = length - len(required)
    password = required + [random.choice(characters) for _ in range(remaining_length)]

    # Shuffle so required chars are not always at the start
    random.shuffle(password)
    return ''.join(password)


def password_strength(password):
    """
    Rate password strength from 1-5.
    """
    score = 0

    # Add points for different criteria
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    strength = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    return strength[min(score, 5)]


def main():
    """Main function to run the password generator."""
    print("Password Generator")
    print("-" * 30)

    # Get password length from user
    length_input = input("Password length (default 12): ").strip()
    length = int(length_input) if length_input else 12

    # Generate password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
    print(f"Strength: {password_strength(password)}")

    # Generate alternative passwords
    print("\nAlternative passwords:")
    for i in range(3):
        alt_password = generate_password(length)
        print(f"{i+1}. {alt_password} ({password_strength(alt_password)})")


if __name__ == "__main__":
    main()