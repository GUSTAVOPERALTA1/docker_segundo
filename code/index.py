from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/docker')
def docker():
    return render_template('docker.html')
@app.route('/ubuntu')
def ubuntu():
    return render_template('ubuntu.html')

if __name__ == '__main__':
    app.run(debug=True)