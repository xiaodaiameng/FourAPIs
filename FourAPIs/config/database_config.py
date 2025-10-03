from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import DATABASE_CONFIG

DATABASE_URL = f"mysql+pymysql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_mysql_database():
    try:
        connection = engine.connect()
        connection.close()
        print("成功连接到MySQL数据库")
    except Exception as e:
        print(f"连接MySQL数据库失败: {str(e)}。请确保MySQL服务器已启动，并且数据库{DATABASE_CONFIG['database']}已创建")
