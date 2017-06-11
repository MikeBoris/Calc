# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    number=float(request.form['number'])
    cats=float(request.form['cats'])
    r1=float(request.form['rad_1'])
    r2=float(request.form['rad_2'])
    r3=float(request.form['rad_3'])
    result=number*cats*r3*r2*r1
    result_string="You've got " + str(result) + " cats!!"
    return render_template('form_submit.html', result_string=result_string)

# Run the app
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
