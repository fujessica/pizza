from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')

# @app.route('/about')
# def about():
#     return "amongus"

# @app.route("/pizza_gpt/<int:id>")
# def pizza(id):
#     connection = sqlite3.connect("pizza_gpt.db")
#     cursor = connection.cursor()
#     cursor.execute("SELECT * from Pizza where pizza_id = ?", (id,))
#     pizza = cursor.fetchone()
#     return pizza



if __name__ == "__main__":
    app.run(debug = True)