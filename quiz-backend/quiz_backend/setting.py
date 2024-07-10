from starlette.config import Config

try:
    config = Config('.env')
except FileNotFoundError as e:
    print(e)

db_url = config.get('DB_URL')
test_db_url = config.get('TEST_DB_URL')