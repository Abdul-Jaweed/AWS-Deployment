from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def regex_tester():
    if request.method == 'POST':
        pattern = request.form['pattern']
        test_string = request.form['test_string']
        try:
            match = re.search(pattern, test_string)
            if match:
                result = f'Match found: {match.group()}'
            else:
                result = 'No match found.'
        except re.error as e:
            result = f'Error: {e}'
    else:
        pattern = ''
        test_string = ''
        result = ''

    return render_template('index.html', pattern=pattern, test_string=test_string, result=result)

if __name__ == '__main__':
    app.run()
