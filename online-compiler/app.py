from flask import Flask, render_template, request
import subprocess
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    code = request.form['code']

    with open('temp/code.py', 'w') as f:
        f.write(code)
    start_time = time.time()
    result = subprocess.run(
        ['python', 'temp/code.py'],
        capture_output=True,
        text=True
    )
    end_time = time.time()
    execution_time = round(end_time - start_time, 4)

    output = result.stdout + result.stderr

    return render_template(
    'index.html',
    code=code,
    output=output,
    execution_time=execution_time
)

if __name__ == '__main__':
    app.run(debug=True)