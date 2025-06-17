from database import ReadSessionLocal
from models import User


def get_user_by_email(email: str):
    session = ReadSessionLocal()
    try:
        return session.query(User).filter(User.email == email).first()
    finally:
        session.close()


def list_users():
    session = ReadSessionLocal()
    try:
        return session.query(User).all()
    finally:
        session.close()

