# utils.py (Helper Functions)
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    """Verify a passwor by comparing hashes."""
    return hash_password(password) == hashed_password