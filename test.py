from flask import Flask,session
from flask_cors import CORS

# Flask init
app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/login')
def test():
   print("----->>Yes")
   print(request.get_data())
   return "233333"

if __name__ == '__main__':
    app.run()
