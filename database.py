from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://home:123456@localhost/fast_api_postgresql',
                       echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
