from spellcheckfile import *
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report.html')
def report():
    filename= request.args.get('filename')
    result= spellchecking(filename)
    if result==False:
        return render_template('error.html')

    return render_template('report.html', total=result[0], j=result[1], k=result[2], l=result[3])


if __name__ == '__main__':
    app.run(debug=True)