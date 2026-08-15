import os
import bcrypt
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

MEDCARE_SECRET_KEY = os.getenv("MEDCARE_SECRET_KEY", "default_secret_key")
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    encoded = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(encoded, salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(username: str, role: str) -> str:
    payload = {
        "sub": username,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=20)
    }
    return jwt.encode(payload, MEDCARE_SECRET_KEY, algorithm=ALGORITHM)
