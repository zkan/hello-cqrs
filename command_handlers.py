from database import WriteSessionLocal
from models import User


def create_user(name: str, email: str):
    session = WriteSessionLocal()
    try:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print(f"User '{name}' created.")
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()

