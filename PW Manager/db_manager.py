import mysql.connector
from aes import encrypt, decrypt


def connect():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Exodia2024!",
            database="vault"
        )
        return cnx
    except mysql.connector.Error as error:
        print(error)


def store_account(username, password, email, url):
    try:
        password = encrypt(password)
        email = encrypt(email)

        cnx = connect()
        cursor = cnx.cursor()

        cursor.execute("INSERT INTO accounts (username, password, email, url) VALUES (%s, %s, %s, %s)", (
            username, password, email, url))
        cnx.commit()
    except mysql.connector.Error as error:
        print(error)


def remove_account(username, url):
    try:
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute(
            "SELECT * FROM accounts WHERE url= %s AND username= %s ", (url, username))

        result = [i for i in cursor]
        if result and username in result[0]:
            cursor.execute("DELETE FROM accounts WHERE username = %s AND url = %s", (
                username, url))
            cnx.commit()
            print('\nAccount removed!\n')
        if not result:
            print('\nAccount not found.\n')
    except mysql.connector.Error as error:
        print(error)


def find_account_by_url(url):
    try:
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM accounts WHERE url = %s", (url,))

        result = [i for i in cursor]
        if len(result) != 0:
            print(f"\n{'-'*8}ACCOUNT(S) FOUND{'-'*8}")
            for account in result:
                result = list(account)
                if url == result[3]:
                    result[1] = decrypt(result[1])
                    result[2] = decrypt(result[2])
                    username = result[0]
                    password = result[1]
                    email = result[2]
                    website = result[3]
                    print(
                        f'\nUsername: {username}\nPassword: {password}\nEmail: {email}\nURL: {website}\n')
        else:
            print(f"\n{'-'*8}NO ACCOUNTS FOUND{'-'*8}\n")
    except mysql.connector.Error as error:
        print(error)


def find_account_by_email(_email):
    _email = encrypt(_email)
    try:
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM accounts WHERE email = %s", (_email,))

        result = [i for i in cursor]
        if len(result) != 0:
            print(f"\n{'-'*8}ACCOUNT(S) FOUND{'-'*8}")
            for account in result:
                result = list(account)
                if _email == result[2]:
                    result[1] = decrypt(result[1])
                    result[2] = decrypt(result[2])
                    username = result[0]
                    password = result[1]
                    email = result[2]
                    website = result[3]
                    print(
                        f'\nUsername: {username}\nPassword: {password}\nEmail: {email}\nURL: {website}\n')
        else:
            print(f"\n{'-'*8}NO ACCOUNTS FOUND{'-'*8}\n")
    except mysql.connector.Error as error:
        print(error)


# store_account("asdasd", "omg123",
#               "test@gmail.com", "lazada.com")
# remove_account(username="timothy", password="cats69420!",
#                url="straitstimes.sg")
# print(find_account_by_email("test@gmail.com"))

# cnx = connect()
# cursor = cnx.cursor()
# cursor.execute(
#     "DELETE FROM accounts;")
# cnx.commit()
# find_account_by_email('jon@gmail.com')
