from app import createapp

app = createapp(config_name='development')

if __name__ == '__main__':
    app.run()