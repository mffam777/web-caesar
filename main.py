from flask import Flask 
# from flask import Flask: this imports 
# the Flask class from the flask module.

app = Flaks(__name__) # app will be the object created by the 
# constructor Flask. __name__ is a variable controlled by Python 
# that tells code what module it's in.

app.config['DEBUG'] = True
# the DEBUG configuration setting for the Flask application will 
# be enabled. This enables some behaviors that are helpful when 
# developing Flask apps, such as displaying errors in the browser, 
# and ensuring file changes are reloaded while the server is 
# running (aka "host swapping")

@app.route("/") 
# this is a decorator that creates a mapping between 
# the path - in this case the root, or "/", and the function that 
# we're about to define

def index(): 
#We define index, a function of zero variables

    return forms
    # Our function returns a string literal.


app.run() 
# Pass control to the Flask object. The run function 
# loops forever and never returns, so put it last. It carries 
# out the responsibilities of a web server, listening for requests 
# and sending responses over a network connection.
