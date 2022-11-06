from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def index():
   return "TEKO PANAS!"
	
@app.route('/Hello')
def hello():
   return "Hello, World!"
	
@app.route("/members")
def members():
   return "Members"
	
@app.route("/members/<name>/")
def getMember(name):
   return name
	
if __name__ == '__main__':
   app.run(debug=True)
