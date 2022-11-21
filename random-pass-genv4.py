import random,time
import string

alphabtes = string.ascii_letters
digits = string.digits
specialCharacters = string.punctuation

passwordChara = list(alphabtes + digits + specialCharacters)

def condition_random_password():
  length = input("\033[92m [*] Enter the Password Length: ")
  if int(length.isdigit()):
     alpha_count = input("\033[92m [*] Enter the Alphabtes Count in Password: " )
     if int(alpha_count.isdigit()):
        digits_count = input("\033[92m [*] Enter the Digits Count in Password: ")
        if int(digits_count.isdigit()):
            special_count = input("\033[92m [*] Enter the Special Characters Count: ")
            if int(special_count.isdigit()):
                    characters_count = int(alpha_count) + int(digits_count) + int(special_count)
                    if characters_count > int(length):
                        print("\033[92m [*] The entered Character Count is Greater than the total Password Length")
                        return
                    password = [] 
                    for i in range(int(alpha_count)):
                        password.append(random.choice(alphabtes))
                    for i in range(int(digits_count)):
                        password.append(random.choice(digits))
                    for i in range(int(special_count)):
                        password.append(random.choice(specialCharacters))
                    if characters_count < int(length):
                        random.shuffle(passwordChara)
                        for i in range(int(length) - characters_count):
                            password.append(random.choice(passwordChara))
                    print("".join(password))
            else:
              print("\033[92m [*] Enter a valid special count")
        else:
          print("\033[92m [*] Enter a valid digit count")
     else: 
       print('\033[92m [*] Enter a valid alpha count')
  else: 
    print("\033[92m [*] Enter a valid length")

def random_password():
  singlePassword = string.ascii_letters + string.digits + string.punctuation
  length = input("\033[92m [*] Enter the Password Length: ")
  if length.isdigit():
    print("".join(random.sample(singlePassword, int(length))))
  else:
    print("\033[91m [-] Please enter a valid length")

print("\033[92m [*] Please Select the below options \n ")
option = input("\033[92m [*] 1 - Generating based on Conditions \n [*] 2 - Randomly Generating the Password \n\n [*] Enter the Option: ")
print("")
if option == "1": 
  condition_random_password()
elif option == "2":
    random_password()
else:
  print("\033[91m [-] Invalid Option")
time.sleep(4)
