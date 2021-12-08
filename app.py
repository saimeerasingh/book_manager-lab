from flask import Flask, render_template


app = Flask(__name__)

from controllers.books_controller import books_blueprint
app.register_blueprint(books_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
