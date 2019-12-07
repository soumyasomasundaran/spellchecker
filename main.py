from spellcheckfile import *
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/report.html')
def report():
    filename= request.args.get('filename')
    (total, j, k, l)= spellchecking(filename)

    return(render_template('report.html',total=total,j=j,k=k,l=l))


if __name__ == '__main__':
    app.run(debug=True)