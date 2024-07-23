from starlette.config import Config
from quiz_backend.utils.imports import timedelta
try:
    config = Config('.env')
except FileNotFoundError as e:
    print(e)



# Get variables from config file

db_url = config.get('DB_URL')
test_db_url = config.get('TEST_DB_URL')
access_expiry_time = timedelta(minutes=int(config.get("ACCESS_EXPIRY_TIME")))
refresh_expiry_time = timedelta(days=int(config.get('REFRESH_EXPIRY_TIME')))
secret_key = config.get('SECRET_KEY')
algorithm = config.get('ALGORITHM')