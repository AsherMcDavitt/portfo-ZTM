from email import message
import csv
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
app.run()

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
app.run()

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'wrong'
    










# Set-ExecutionPolicy RemoteSigned then portfolio\Scripts\activate.ps1 then Set-ExecutionPolicy Restricted
# MAKE SURE YOU'RE IN THE CORRECT DIRECTORY IN TERMINAL! (python/portfolio)
# activate with: $env:FLASK_APP = "server.py"   then: $env:FLASK_ENV = "development"  then put in: flask run


# .......................................................................................

# NOTES:
# You can only access one 'work' on "works", this is not because of the course, if you want to continue with that you must do it on your own.
# Render Template wants to look for html's in a folder called 'templates' so make that in the future when using this