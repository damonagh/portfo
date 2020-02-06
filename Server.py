#
# https://flask.palletsprojects.com/en/1.1.x/
#
# Create your project in Pycharm.  It will take care of creating the venv environment
# pip install Flask
#
# http://flask.palletsprojects.com/en/1.1.x/quickstart/
# Every time your start Pycharm do the following:
# - go to the venv\scripts folder and type in 'activate'
# - set FLASK_APP=<your python file>
# - set FLASK_ENV=development  (NOTE:  This allows us to update the code without having to stop and restart the server)
# - type in 'flask run' to start the server.  It will provide a URL that you can click on
#
from flask import Flask, render_template, url_for, request, redirect
import csv
#
# https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for
#
# Mime Types
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
#
app = Flask(__name__)
print(__name__)

#
# Using Variable names in Flask:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
#
@app.route('/')
#def hello_world(username=None, id=None):
def my_home():
#    return 'Hello, David!'
#
#   NOTE:   render_template looks for files in the .\Templates folder
#           so make sure your html files are there
#           http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
#   NOTE:   CSS files and Javascript files need to go in the .\static folder
#           http://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files
#
#   NOTE:   Jinja is what allows the use of scripting in HTML files that Flask can
#           interpret at runtime.
#           https://en.wikipedia.org/wiki/Jinja_(template_engine)
#
#    print(url_for('static', filename='app_icon.ico'))
#    return  render_template('index.html', name=username, id=id)
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('C:/Users/damonagh/PycharmProjects/WebDev/venv/database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
# https://docs.python.org/3/library/csv.html
    with open('C:/Users/damonagh/PycharmProjects/WebDev/venv/database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#@app.route('/blog')
#def blog():
#    return 'This is the blog page.'

#
# Using the Request Object in Flask
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
#
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong!'