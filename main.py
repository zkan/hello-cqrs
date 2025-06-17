from database import Base, write_engine
from command_handlers import create_user
from query_handlers import get_user_by_email, list_users


def main():
    # Create DB schema
    Base.metadata.create_all(bind=write_engine)

    # Command
    create_user("Alice", "alice@example.com")
    create_user("Bob", "bob@example.com")

    # Query
    user = get_user_by_email("alice@example.com")
    print(f"Queried User: {user.name} - {user.email}")

    all_users = list_users()
    print("All users:")
    for u in all_users:
        print(f"{u.name} ({u.email})")


if __name__ == "__main__":
    main()
