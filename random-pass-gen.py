import string,random

def generate(n):

    """
    This function will take n as password length then generate final string which has letters,digits and puntuation
    then convert that string into list 
    then uses random.shuffle to shuffle that list
    initiale another list in which we store our password
    then iterate a loop to password length so it can save characters through random.choice in pw_list
    shuffle pw_list for more randomness
    converts pw_list into string password. 
    """

    s1 = str(input("\033[92m [*] Enter Name : "))
    s2=str(input("\033[92m [*] Enter Name : "))
    s3=str(input("\033[92m [*] Enter Name : "))

    final = s1+s2+s3

    l1 = list(final)
    random.shuffle(l1)

    pw_list = []

    i=0
    while i<n:
        pw_list.extend(random.choice(l1))
        i+=1

    random.shuffle(pw_list)
    password = ''.join(pw_list)
    print("\033[91m [+] Your Password Is "+password)


if __name__ == "__main__":
    c="y"
    while c=="y":
        try:
            n = int(input("\033[92m [+] Enter desired length of password: "))
            generate(n)
            c=input("\033[96m [*] Do you want to generate another password? (y/n): ").lower()
        except:
            print("\033[91m\n [*] Please Enter integer value for length")
       


