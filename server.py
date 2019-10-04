from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def usersForm():
    print(request.form)
    form_name = request.form['name']
    form_location = request.form['location']
    form_language = request.form['language']
    form_framework = request.form.getlist('framework')
    print(form_framework)
    form_hours = request.form['hours']
    form_comment = request.form['comment']
    
    return render_template('results.html', temp_name=form_name, temp_location=form_location, temp_language=form_language, temp_framework=form_framework, temp_hours=form_hours, temp_comment=form_comment)

if __name__=="__main__":
    app.run(debug=True)
