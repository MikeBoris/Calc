# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route ("/") for the default URL, which loads the form 
# Define a route ("/calculate") for the action of the form,
# including which type of requests this route is 
# accepting: POST requests in this case
@app.route('/')
@app.route('/calculate', methods=['GET','POST'])
def hello():
	# Initialize errors variable to empty string
	errors = ''
	if request.method == "GET": #if request is GET, render form template
		return render_template('form_submit.html')
	else:
		# The request is POST with some data, get POST data and validate it
		# Strip to remove leading and trailing whitespaces
		try:
			number=int(request.form['number'].strip())
		except:
			number=False
		try:
			cats=int(request.form['cats'].strip())
		except:
			cats=False
		try:	
			r1=int(request.form['rad_1'])
		except:
			r1=False
		try:
			r2=int(request.form['rad_2'])
		except:
			r2=False
		try:
			r3=int(request.form['rad_3'])
		except:
			r3=False
		try:
			select=int(request.form['selector'])
		except:
			select=False
		try:
			check=int(request.form['checkor'])
		except:
			check=False
		# Check if all the fields are non-empty and raise an error otherwise
		if not number or not cats or not r1 or not r2 or not r3 or not select or not check:
			errors = "Please enter all the fields."
		if not errors:
			result=number*cats*r3*r2*r1*select*check
			result_string="You've got " + str(result) + " cats!!"
			# Since form data is valid, render template with results
			return render_template('form_submit.html', result_string=result_string)
		# Render the form template with error messages
		return render_template('form_submit.html', errors=errors)		

# Run the app
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
