#Práctica 15
#Jesús Gómez Guijarro
#Flask
from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola mundo '

if __name__ =='__main__':
#     app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)