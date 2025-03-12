import hashlib
from models import User, SessionLocal
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

class UserController:
    def __init__(self):
        self.session = SessionLocal()

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password, confirm_password, role):
        """Register a new user"""
        if password != confirm_password:
            return False, "Password do not match."
        
        if role not in ["admin", "user"]:
            return False, "Invalid role. Choose 'admin' or 'user'."

        hashed_password = self.hash_password(password)
        new_user = User(username=username, password=hashed_password, role=role)

        try:
            self.session.add(new_user)
            self.session.commit()
            return True, f"User '{username}' registered successfully as {role}!"
        except IntegrityError:
            self.session.rollback()
            return False, f"Username '{username}' already exists!"
        except SQLAlchemyError as e:
            self.session.rollback()
            return False, str(e)

    def login(self, username, password):
        """Login and return user role"""
        try:
            hashed_password = self.hash_password(password)
            user = self.session.query(User).filter_by(username=username, password=hashed_password).first()

            if user:
                return True, user.role
            else:
                return False, "Invalid username or password."
        except SQLAlchemyError as e:
            return False, str(e)

