import datetime
from flask import Flask,render_template
#print("this file name is", __name__)

app = Flask(__name__)

@app.route('/<string:name>')
def hello(name):
	if "&" in name:
		# name = "?name=Big+meow&code=1234"
		temp = name.split("&")
		# temp = ["name=Big+meow", "code=1234"]
		username = temp[0].split('=')[1].replace("+", " ")
		passcode = temp[1].split('=')[1]
		return f"<h1>Username is: <span style='color:green; border:solid 2px'>{username}</span><h1>"\
		       f"<h1>Password is: <span style='color:red; border:dotted 5px'>{passcode}</span><h1>"
	else:
		return f"Hello, {name}!"
	# bad practice, "?" doesn't work for <string:name>
	# hint: "+"" couldn't connect two fstrings without "\"
	# ";" is essential when you have two elements, px is essential

@app.route('/meow')
def helloworld():
	return '<h1 style="color:red">meow meow meow</h1>'
	#case insensitive, meow has higher priority than name

@app.route('/')
def index():
	catname = 'dog'
	color = "green"
	return render_template('index.html', catname = catname, htmlcolor=color)

@app.route("/newyear")
def newyear():
	now = datetime.datetime.now()
	is_newyear = now.month == 1 and now.day == 1
	
	return render_template("newyear.html", is_newyear=is_newyear)