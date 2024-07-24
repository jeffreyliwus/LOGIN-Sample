def account():
    print("WELCOME TO MY LOGIN PROJECT")
    while True:
        login = input(str("Username : "))

        if len(login) == 0:
            print("invalid. pls enter a username now")
        else:
            len(login) == 1
            print("sucess!")

            break

    while True:
        password = input(str("Password: "))
        if len(password) == 0:
            print("invalid. pls enter a password now")

        else:
            len(password) == 1
            print("sucess!")

            break


account()
