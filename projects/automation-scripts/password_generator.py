import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True):
    """Generate a strong random password"""
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    characters = letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


# Main program
if __name__ == "__main__":
    print("=== Password Generator ===\n")
    
    length_input = input("Enter password length (default 12): ")
    length = int(length_input) if length_input else 12
    
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_symbols, use_numbers)
    
    print(f"\n✅ Your generated password is:")
    print(password)
    print(f"\nLength: {len(password)} characters")