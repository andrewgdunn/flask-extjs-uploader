from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory
from werkzeug import secure_filename
import os

# Configuring the Application
app = Flask(__name__, template_folder='static')
#app.host ='0.0.0.0'
#app.debug = True
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
    file = request.files['file_selector-inputEl']
    print(file.filename)
    response = {"success": "true"}

    print response
    print jsonify(response)

    return jsonify(response)

    # print (jsonify("success"="true"))
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], "1.pdf"))
    #return jsonify(success=True)

    # return '''\
    #         {
    #         "success":true, // note this is Boolean, not string
    #         }\
    #         '''


    # return jsonify(success=True,
    #     file='1.pdf',
    #     file_url='/upload/1.pdf')
    # file = request.files.values()[0]
    # #filename = secure_filename(file)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], "1.pdf"))


@app.route('/upload/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)


if __name__ == '__main__':
    app.run()
