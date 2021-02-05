import getpass

user_credentials_dict = {
    "security": {
        "credentials": {
            "username": "zuleyha",
            "password": "1234"
        }
    }
}


def validate_credentials(**kwargs):
    input_uname, input_passwd = kwargs.values()
    u_name = user_credentials_dict.get("security", {}).get("credentials", {}).get("username")
    password = user_credentials_dict.get("security", {}).get("credentials", {}).get("password")

    if input_uname == u_name and input_passwd == password:
        return True
    else:
        return False


if __name__ == '__main__':
    is_valid = False
    while not is_valid:
        user_name = str(input("Please enter your username: "))
        passwd = getpass.getpass("Please enter your password: ")

        if validate_credentials(username=user_name, password=passwd):
            is_valid = True
            print("Login successful!..")
        else:
            print("Your credentials may wrong. Please try again..")
