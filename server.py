from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def homepage():
    return render_template('./index.html')


@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

def write_to_csv(data):
    with open('database.csv', mode = 'a',  newline='\n') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong. Try again!'