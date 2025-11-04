from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# ✅ ВОТ РЕШЕНИЕ
engine_args = {}

# 1. Проверяем, используем ли мы SQLite (для локальной разработки)
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    # 2. Если да, добавляем connect_args
    engine_args["connect_args"] = {"check_same_thread": False}

# 3. Создаем engine, распаковывая аргументы
# (Если PostgreSQL, engine_args будет пустым)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    **engine_args 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
