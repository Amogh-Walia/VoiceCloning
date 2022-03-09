from distutils.command.upload import upload
from flask import Flask,request
from flask.templating import render_template
from Generate import Run
import numpy as np
import os

UPLOAD_FOLDER = './upload'




app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/",methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        
        file1 = request.files['file1']
        text = request.form['text']
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'Input.wav')
        print(path)
        file1.save(path)
        #print(path)
        Run('./upload/Input.wav',text)
        return render_template('result.html',DATA = 'Halwa')


    return render_template('index.html')


if __name__ == '__main__':
    app.run()



if __name__ == "__main__":
    app.run()
