STANDARD_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}


INVALID_LOGIN_CASES = [
    (
        "standard_user",
        "wrong_password",
        "Username and password do not match",
    ),
    (
        "",
        "",
        "Username is required",
    ),
]