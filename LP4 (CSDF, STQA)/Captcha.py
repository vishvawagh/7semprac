import random
import string

# Function to check user input against generated CAPTCHA
def check_captcha(captcha, user_input):
    return captcha == user_input

# Function to generate CAPTCHA of length n
def generate_captcha(n):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(n))
    return captcha

def main():
    input_choice = 'y'
    while input_choice.lower() == 'y':
        n = int(input("\nEnter the required length of CAPTCHA: "))
        captcha = generate_captcha(n)
        print(f"CAPTCHA: {captcha}")
        
        user_input = input("Enter the CAPTCHA: ")
        
        if check_captcha(captcha, user_input):
            print("Valid CAPTCHA")
        else:
            print("Invalid CAPTCHA")
        
        # Ask the user if they want to continue
        input_choice = input("\nDo you want to continue (y/n): ")

if __name__ == "__main__":
    main()
