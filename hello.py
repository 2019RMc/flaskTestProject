from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')

#def index():
 #   return "<h1>Hello World!</h1>"


#filters

#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
    first_name = "John"
    stuff="This is <strong>Bold</strong> Text"
    favorite_pizza=["Pepperoni","Pineapple","meat",41,"cheese"]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',
                           user_name=name)

# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# internal server error
@app.errorhandler(500)
def Internal_Server_Error(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)