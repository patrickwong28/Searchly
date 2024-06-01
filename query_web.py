from search.interface import run_interface_web
import sys
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        query = request.form['query']
    else:
        return render_template('index.html')

    try:
        if len(sys.argv) != 1:
            raise IndexError
        results, execution_time = run_interface_web(query)
    except FileNotFoundError:
        print('File not found!')

    return render_template('index.html', results=results, time=execution_time)


if __name__ == '__main__':
    app.run(debug=True)