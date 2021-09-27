from db_manager import store_account, remove_account, find_account_by_url, find_account_by_email


def menu():
    print(f"\n{'-'*8}Menu{'-'*8}\n")
    print("1) Store new account")
    print("2) Find accounts")
    print("3) Remove and account")
    print("4) Generate a password")
    print("0) Quit")


def store():
    print(f"\n{'-'*8}Store Account{'-'*8}\n")
    website = input("Enter site/app name: ")
    email = input("Email: ") or "none"
    username = input("Username: ")
    password = input("Password: ")
    store_account(username, password, email, website)
    print('\nAccount stored!\n')


def find():
    print(f"\n{'-'*8}Find Account{'-'*8}\n")
    print('1) Find by URL')
    print('2) Find by email\n')
    while True:
        choice = input('>>> ')
        try:
            choice = int(choice)
        except:
            print('Enter a number. Try again.')
            continue
        if choice not in range(1, 3):
            print('Number out of range. Try again.')
            continue

        if choice == 1:
            url = input('Enter URL: ')
            find_account_by_url(url)
        else:
            email = input('Enter email: ')
            find_account_by_email(email)
        break


def remove():
    url = input('\nEnter site/app name: ')
    username = input('Enter username: ')
    remove_account(username, url)
