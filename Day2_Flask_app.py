from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    print('Hello world!!!')
app.run(port=5000)
