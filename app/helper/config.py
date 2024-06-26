import os

APP_NAME = os.getenv("APP_NAME", "My App")

MONGO_DETAILS = "mongodb://localhost:27017" # database url
MONGO_DATABASE = "py-pos-coffee"  # database name

JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 770
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = 1440
JWT_SECRET_KEY = "-gZNIH52GyRUXi9hThhTw8Kvbi6UMlgz8UjKHJIL3faJqqAXreq_I0WAdfSqjnxk"
JWT_ALGORITHM = "HS256"
