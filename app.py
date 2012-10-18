from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory
from werkzeug import secure_filename
import os

# Configuring the Application
app = Flask(__name__, template_folder='static')
#app.host ='0.0.0.0'
app.debug = True
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')


# Need these to route requests to the proper resources
# Sencha has a particular deploy style that I want to not touch
@app.route('/app.js')
def sencha_app():
    return redirect(url_for('static', filename='app.js'))


@app.route('/app/view/Viewport.js')
def sencha_viewport():
    return redirect(url_for('static', filename='app/view/Viewport.js'))


@app.route('/app/view/MyForm.js')
def sencha_mypanel():
    return redirect(url_for('static', filename='app/view/MyForm.js'))


@app.route('/')
def index():
    return render_template('app.html')


@app.route('/upload', methods=['POST'])
def upload():
    # I find it more elegant to iterate rather than specify a key
    for element in request.files:
        file = request.files[element]
        print file.filename
        safe_name = secure_filename(file.filename)
        print safe_name
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], safe_name))
        #upload_success = True

    # Doesn't work
    # if upload_success:
    #     return jsonify(success=True)
    # else:
    #     return jsonify(success=False)

    # Working
    return '''\
            {
            "success":true
            }\
            '''


# @app.route('/upload/<path:filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
