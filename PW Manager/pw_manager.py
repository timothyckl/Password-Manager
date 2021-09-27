from menu import menu, store, find, remove
from secret import generate_password, master_pw
import hashlib
import getpass
import time

passwd = hashlib.sha512(getpass.getpass(
    "\nEnter master password: ").encode()).hexdigest()

if passwd == master_pw:
    time.sleep(1)
    print("\nWelcome!")
    while True:
        menu()
        choice = input('\n>>> ')
        try:
            choice = int(choice)
        except:
            print('Please use numeric digits.')
            continue
        if choice not in range(5):
            print('Number not in range. Try again.')
            continue
        if choice == 1:
            store()
            input("Press a key to continue...")
        elif choice == 2:
            find()
            input("Press a key to continue...")
        elif choice == 3:
            remove()
            input("Press a key to continue...")
        elif choice == 4:
            generate_password()
            input("Press a key to continue...")
        else:
            break
else:
    print("\nWRONG PASSWORD BOZO\n")
    exit()
