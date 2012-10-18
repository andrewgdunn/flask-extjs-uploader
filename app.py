from flask import Flask, request, render_template, redirect, url_for
from flask import make_response, send_from_directory
from werkzeug import secure_filename
import os

# Configuring the Application
app = Flask(__name__, template_folder='static')
#app.host ='0.0.0.0'
app.debug = True
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')


# Need these to route requests to the proper resources
# Sencha has a particular deploy style that I want to not touch
# The goal of this project was to be able to accomodate rapid protyping using
# Sencha architect. I wanted to be able to use a default deploy folder.
@app.route('/app.js')
def sencha_app():
    return redirect(url_for('static', filename='app.js'))


@app.route('/app/view/Viewport.js')
def sencha_viewport():
    return redirect(url_for('static', filename='app/view/Viewport.js'))


@app.route('/app/view/MainForm.js')
def sencha_mypanel():
    return redirect(url_for('static', filename='app/view/MainForm.js'))


@app.route('/')
def index():
    return render_template('app.html')


@app.route('/upload', methods=['POST'])
def upload():
    # I find it more elegant to iterate rather than specify a key
    for element in request.files:
        file = request.files[element]
        safe_name = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], safe_name))

    # For Ext.form.action.Submit you need to return 'text/html' as a mimetype
    # instead of json (Even though the response is actually json). I'm not sure
    # why. There are many examples where people manually construct the response
    # That I dug through during my confusion. Below is a response object that
    # works.
    response = make_response('{"success":true}')
    response.mimetype = 'text/html'
    return response

# Maybe I'll extend this to be able to download the file back out, but that is
# Less of a concern than just handling forms right now.
# @app.route('/upload/<path:filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
