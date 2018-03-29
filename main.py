from flask import Flask
import caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot" value="0">
            <textarea name="text"></textarea>
            <button type="submit">Submit</button>
        </form>  
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def encrypt():

@app.route("/")
def index():
    return form

app.run()