"""
ads/ensure_db.py
"""
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.conf import settings


def ensure_db_exists():
    """
    НЕ ЗАПУЩЕН
    Check if the database exists and create it if it doesn't
    :return:
    """
    db_name = settings.DATABASES["default"]["NAME"]
    db_user = settings.DATABASES["default"]["USER"]
    db_password = settings.DATABASES["default"]["PASSWORD"]
    db_host = settings.DATABASES["default"]["HOST"]
    db_port = settings.DATABASES["default"]["PORT"]

    try:
        # Подключаемся к серверу PostgreSQL (не к конкретной БД)
        conn = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            dbname="postgres",  # Подключаемся к системной БД
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Проверяем существование БД
        cursor.execute(
            sql.SQL("SELECT 1 FROM pg_database WHERE datname = {}").format(
                sql.Literal(db_name)
            )
        )
        exists = cursor.fetchone()

        if not exists:
            # Создаём БД, если её нет
            cursor.execute(
                sql.SQL("CREATE DATABASE {} WITH OWNER {} ENCODING 'UTF8'").format(
                    sql.Identifier(db_name), sql.Identifier(db_user)
                )
            )
            print(f"База данных '{db_name}' успешно создана.")
        else:
            print(f"База данных '{db_name}' уже существует.")

    except Exception as e:
        print(f"Ошибка при проверке/создании БД: {e}")
    finally:
        if "conn" in locals():
            conn.close()


# Вызов функции (например, в AppConfig.ready())
ensure_db_exists()
