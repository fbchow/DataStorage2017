from flask import Flask
app = Flask(__name__)

# connect flask to db using connection string that sql alchemy expects
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usTransportation'
db.init_app(app)

app.secret_key = "development-key"

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()