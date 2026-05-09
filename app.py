import flask, requests, jsonify
app = flask.Flask(__name__)
data = []
@app.route('/')
def home():
    return "Api is running"

if __name__ == '__main__':
    app.run(debug=True)

