import os
import json
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from pointnet_model import eval_model
from convert import convert_to_obj

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods = ['POST', 'GET'])
def hello_world(name=None):
    error = None
    val = "Nothing"
    if request.method == 'POST' :
        f = request.files["3Dobject"]
        file_name = f.filename
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file_name))
        f.save(file_path)
        result = eval_model(file_name=file_name)
        print(result)
        res_json = json.dumps(result)
        return redirect(url_for('upload_success', result=res_json, file_name=file_name))
    return render_template("home.html", name=name, error=error, val=val)

@app.route("/upload_success")
def upload_success():
    res_json = request.args['result']
    file_name = request.args['file_name']
    convert_to_obj(file_name=file_name)
    result = json.loads(res_json)
    return render_template("classify.html",  label=result[file_name], filename=file_name.split(".")[0] + ".obj" )

@app.route("/download/<path:filename>", methods = ['GET', 'POST'])
def download(filename):
    print(filename)
    file_path = os.path.join("out", filename)
    return send_file(file_path, as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)
    