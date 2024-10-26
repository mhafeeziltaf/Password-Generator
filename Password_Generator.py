import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
ur_letters = int(input("How many Letters you want to include in your Password: \n"))
ur_numbers = int(input("How many numbers you want to include in your Password: \n"))
ur_symbols = int(input("How many symbols you want to include in your Password: \n"))

# #Easy version (without shuffling the password)
password = ""
for char in range(0,ur_letters):
   password += random.choice(letters)
for char in range(0,ur_numbers):
   password += random.choice(numbers)
for char in range(0,ur_symbols):
   password += random.choice(symbols)
print(password)      

# Hard version
password_list = []
for char in range(0,ur_letters):    
   password_list += random.choice(letters)
for char in range(0,ur_numbers):
   password_list += random.choice(numbers)
for char in range(0,ur_symbols):
   password_list += random.choice(symbols)

random.shuffle(password_list)
password =""
for char in password_list:
 password += char
print(f"Your Generated Password is:  {password}")


    