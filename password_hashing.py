from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

bcrypt = Bcrypt()
password = "supersecretpassword"
hash = bcrypt.generate_password_hash(password=password)
print(hash)
check = bcrypt.check_password_hash(pw_hash=hash, password="supersecretpassword")
print(check)
check = bcrypt.check_password_hash(pw_hash=hash, password="wrongpassword")
print(check)
