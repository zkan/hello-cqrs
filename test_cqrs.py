import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import command_handlers
import query_handlers
from models import User
from database import Base


@pytest.fixture(scope="function")
def in_memory_db():
    # Create an in-memory SQLite engine
    engine = create_engine("sqlite:///:memory:", echo=False)
    TestSessionLocal = sessionmaker(bind=engine)

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Override session factories in the handlers
    command_handlers.WriteSessionLocal = TestSessionLocal
    query_handlers.ReadSessionLocal = TestSessionLocal

    yield TestSessionLocal

    # Clean up (optional, but explicit)
    Base.metadata.drop_all(bind=engine)


def test_create_user(in_memory_db):
    command_handlers.create_user("Test User", "test@example.com")

    session = in_memory_db()
    user = session.query(User).filter(User.email == "test@example.com").first()
    assert user is not None
    assert user.name == "Test User"


def test_get_user_by_email(in_memory_db):
    session = in_memory_db()
    session.add(User(name="Alice", email="alice@example.com"))
    session.commit()

    user = query_handlers.get_user_by_email("alice@example.com")
    assert user is not None
    assert user.name == "Alice"


def test_list_users(in_memory_db):
    session = in_memory_db()
    session.add_all([
        User(name="U1", email="u1@example.com"),
        User(name="U2", email="u2@example.com")
    ])
    session.commit()

    users = query_handlers.list_users()
    assert len(users) == 2

    emails = [u.email for u in users]
    assert "u1@example.com" in emails
    assert "u2@example.com" in emails


def test_create_user_duplicate_email(in_memory_db):
    command_handlers.create_user("User1", "dupe@example.com")
    command_handlers.create_user("User2", "dupe@example.com")

    session = in_memory_db()
    users = session.query(User).filter(User.email == "dupe@example.com").all()
    assert len(users) == 1


def test_get_user_by_email_not_found(in_memory_db):
    user = query_handlers.get_user_by_email("notfound@example.com")
    assert user is None


def test_list_users_empty(in_memory_db):
    users = query_handlers.list_users()
    assert users == []
