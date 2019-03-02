import os
from app import createapp

config_name = os.getenv('APP_SETTINGS')
app = createapp(config_name)

if __name__ == '__main__':
    app.run(debug= 1)