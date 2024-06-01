from search.interface import run_interface_web
import sys
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        if len(query) < 1:
            return redirect(url_for('home'))
    else:
        return render_template('index.html')

    try:
        if len(sys.argv) != 1:
            raise IndexError
        results = run_interface_web(query)
    except FileNotFoundError:
        print('File not found!')

    if results is None:
        return render_template('index.html', results=[])
    else:
        top_urls = results[0]
        execution_time = results[1]
        return render_template('index.html', results=top_urls, time=execution_time)


if __name__ == '__main__':
    app.run(debug=True)