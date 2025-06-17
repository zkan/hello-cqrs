from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Same DB now, but we can split these later
WRITE_DB_URL = "sqlite:///cqrs.db"
READ_DB_URL = "sqlite:///cqrs.db"  # Same for now, can change to replica later

write_engine = create_engine(WRITE_DB_URL, echo=False)
read_engine = create_engine(READ_DB_URL, echo=False)

WriteSessionLocal = sessionmaker(bind=write_engine)
ReadSessionLocal = sessionmaker(bind=read_engine)

Base = declarative_base()
