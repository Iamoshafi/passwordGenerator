#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Created a universal list to store date after all elements have been collected
password = []

#for loop to pick random letters and store it in the universal list - password
#k represents the number of elements to be randomly picked based on user input
for letter in letters:
    random_letter = random.choices(letters, k = nr_letters)
password.extend(random_letter)
#print(random_letter)
#print(password)


#for loop to pick symbols letters and store it in the universal list - password
for sym in symbols:
    random_symbol =random.choices(symbols, k = nr_symbols)
password.extend(random_symbol)
#print(random_symbol)


#for loop to pick numbers letters and store it in the universal list - password
for num in numbers:
    random_number = random.choices(numbers, k = nr_numbers)
password.extend(random_number)
#print(random_number)



#shuffling the elements in the list
random.shuffle(password)
display_shuffled_password = ""

#for loop to concatenate all the elements and display it
for pword in password:
    display_shuffled_password += pword
print(f"Here is your password: {display_shuffled_password}")



