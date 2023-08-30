from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin123@localhost/TodoApplicationDatabase"
# SQLALCHEMY_DATABASE_URL = "postgresql://todoappfastapi_user:YnfdxdTtsSdvmbvSYRMzEqvYoDP2pO9c@dpg-cjnac00cfp5c7385c7f0-a.oregon-postgres.render.com/todoappfastapi"
SQLALCHEMY_DATABASE_URL = "postgresql://todoappfastapi_user:YnfdxdTtsSdvmbvSYRMzEqvYoDP2pO9c@dpg-cjnac00cfp5c7385c7f0-a/todoappfastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
