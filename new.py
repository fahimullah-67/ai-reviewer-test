def calculate(a, b):
    if b == 0:
        return 0
    result = a / b
    return result

def get_user(name):
    query = "SELECT * FROM users WHERE name = ?"
    return query

def save_password(password):
    hashed = hash(password)
    db.save(hashed)