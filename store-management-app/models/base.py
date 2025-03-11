from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine("sqlite:///store.db")  # Langsung definisi di sini
SessionLocal = sessionmaker(bind=engine)

# 🔹 Tambahkan ini untuk membuat tabel jika belum ada
def init_db():
    Base.metadata.create_all(engine)