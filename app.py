from flask import Flask, render_template, request, flash, Blueprint
from tarot import tarot

app = Flask(__name__)
app.secret_key="secretpassword"
app.register_blueprint(tarot)



if __name__ == '__main__':
    app.run(debug=True)


