from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def regexp_fun():
    if request.method == 'POST':
        regexp = request.form['input1']
        string_input = request.form['input2']
        match=re.findall(regexp, string_input)
        count=len(match)


 
        return render_template('index.html',count=count,regexp1= regexp,stro = string_input,match=match)

    else:
        count =None
        return render_template('index.html',count = count)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080) # For deployment
    # app.run(host="127.0.0.1", port=8080, debug=True) # For local