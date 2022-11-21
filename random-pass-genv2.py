capchar=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spchar=['!','@','#','$','%','^','&','*','(',')','_','-',',','.']
smallchar=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z'] 
import random, time
passlen=int(input("\033[92m [*] Enter the desired length of password : "))
capans=str(input("\033[92m [*] Are CAPITAL Alphabets allowed ? (Y/N) : "))
smallans=str(input("\033[92m [*] Are lowercase Alphabets allowed ? (Y/N) : "))
digans=str(input("\033[92m [*] Are Digits allowed ? (Y/N) : "))
spans=str(input("\033[92m [*] Are Special Charecters allowed ? (Y/N) : "))
print("\033[91m [*] Way 1 is meant for Minimal Resource Usage and Way 2 for more secure generation.")
rep=input("\033[93m [*] Way 1 or Way 2 ? (1/2) : ")
capans,smallans,digans,spans=capans.title(),smallans.title(),digans.title(),spans.title()
if capans=='Y':
     if smallans=='Y':
          if digans=='Y':
               if spans=='Y':
                    comblis=capchar+dig+spchar+smallchar
               else:
                    comblis=capchar+dig+smallchar
          else :
               if spans=='Y':
                    comblis=capchar+spchar+smallchar
               else:
                    comblis=capchar+smallchar
     else:
          if digans=='Y':
               if spans=='Y':
                    comblis=capchar+dig+spchar
               else:
                    comblis=capchar+dig
          else :
               if spans=='Y':
                    comblis=capchar+spchar
               else:
                    comblis=capchar
else :
     if smallans=='Y':
          if digans=='Y':
               if spans=='Y':
                    comblis=dig+spchar+smallchar
               else:
                    comblis=dig+smallchar
          else :
               if spans=='Y':
                    comblis=spchar+smallchar
               else:
                    comblis=smallchar
     else:
          if digans=='Y':
               if spans=='Y':
                    comblis=dig+spchar
               else:
                    comblis=dig
          else :
               if spans=='Y':
                    comblis=ar+spchar
               else:
                    print("\033[91m Error, You denied the usage of all possible charecters")
                    quit()

password=""
if rep=='1':
     for i in range(passlen):
          password+=comblis[random.randint(0,len(comblis)-1)]
          
else:
     random.shuffle(comblis)
     for i in range(passlen):
          q=random.choice(comblis)
          random.shuffle(comblis)
          password=password+q
print("\n\033[92m [+] Generated Password is : ",password)
print()
time.sleep(3)
