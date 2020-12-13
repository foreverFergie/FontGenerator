import asyncio
from os import path
from flask import Flask, render_template, request
from preprocess import generate
import os
from pathlib import Path
import time 
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, render_template, abort, jsonify, Response
from datetime import datetime

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start() 

@app.route("/uploadFile", methods=["GET", "POST"])
def upload_file():

    # paths where uploaded images are saved locally. 
    testUpper = "C:/Users/cherkanihassanik/Downloads/Testing/Upper/"
    testLower = "C:/Users/cherkanihassanik/Downloads/Testing/Lower/"
    testNums = "C:/Users/cherkanihassanik/Downloads/Testing/Nums/"

    # if request.method == 'POST':
    #Upload Upper
    app.config["UPLOAD_PATH"]=testUpper
    for f in request.files.getlist('file_name_Upper'):
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))

    #Upload Lower
    app.config["UPLOAD_PATH"]=testLower     
    for f in request.files.getlist('file_name_Lower'):
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))

    #Upload Nums
    app.config["UPLOAD_PATH"]=testNums
    for f in request.files.getlist('file_name_Nums'):
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
    
    args = [testUpper, testLower, testNums]
    scheduler.add_job(generate, 'date', run_date=datetime.now(), args=args)
    return render_template("uploadFile.html",msg="Files have been uploaded successfully, you can download your font!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)