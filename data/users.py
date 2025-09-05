from hashlib import sha256

sample_user: dict = {
    "username": "alexey",
    "password": sha256("password_alex".encode()).hexdigest(),
}
