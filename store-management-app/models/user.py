from sqlalchemy import Column, Integer, String
from models import Base


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # 🔹 Simpan dalam bentuk hash nanti
    role = Column(String, nullable=False)  # 🔹 'admin' atau 'user'

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"