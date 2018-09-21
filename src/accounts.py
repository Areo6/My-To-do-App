from validation import is_valid_name, is_valid_email,is_valid_password, is_existing_user


accounts = []
def add_account(name, email, password):
    """
    This function creates a user account
    """
    if not is_valid_name(name) == "Valid 1":
        return is_valid_name(name)
    if not is_valid_email(email) == "Valid 2":
        return is_valid_email(email)
    if not is_valid_password(password) == "Valid 3":
        return is_valid_password(password)
    if is_existing_user(accounts, email):
        return "User with email {} already exist".format(email)

    account = {
        "name": name,
        "email": email,
        "password": password
    }
    accounts.append(account)
    return "Successfully Added an account"

def login(email, password):
    """
    This function logs in the user given their email and password
    """
    if is_valid_email(email) == "valid 2":
        return is_valid_email(email)
    if is_existing_user(accounts, email) == False:
        return "You do not have an account with {}".format(email)
    if not is_valid_password(password) == "Valid 3":
        return is_valid_password(password)
    passcode = [x for x in accounts if x["email"] == email and x["password"] == password]
    if len(passcode) == 0:
        return "Invalid password. Please enter the correct password"
    return "You have successfully logged in"

if __name__ == "__main__":
    print(add_account("Eric", "eubule@gmail.com", "mlb 10A"))
    print(login("eubule@gmail.com", "mlb 10A"))
    print(accounts)