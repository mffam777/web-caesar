from flask import Flask, request
# from flask import Flask: this imports 
# the Flask class from the flask module.

from caesar import rotate_string
# import function from caesar.py

app = Flask(__name__) 
# app will be the object created by the 
# constructor Flask. __name__ is a variable controlled by Python 
# that tells code what module it's in.

app.config['DEBUG'] = True
# the DEBUG configuration setting for the Flask application will 
# be enabled. This enables some behaviors that are helpful when 
# developing Flask apps, such as displaying errors in the browser, 
# and ensuring file changes are reloaded while the server is 
# running (aka "host swapping")


# HTML forms string enclosed in triple-quotes """ so it can take up multiple lines.
form = """
<!doctype html>
<html>
    <head>
        <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
    
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
    
        p.error {{
            color: red;
        }}
    </style>
    </head>

    <body>

    <!-- create your form here -->
      <form method = "POST">

        <label>Rotate by:<input name="rot" type="text"/></label>
        <label><textarea name="text">{encrypt_text}</textarea></label>
        <input type="submit" value="Submit Query">

      </form>

    </body>
</html>

"""

# Create your route


@app.route("/")
def index():
    return form.format(encrypt_text="")


@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    encryption_string = rotate_string(text, rot)

    return form.format(encrypt_text=encryption_string)


app.run() 
# Pass control to the Flask object. The run function 
# loops forever and never returns, so put it last. It carries 
# out the responsibilities of a web server, listening for requests 
# and sending responses over a network connection.
