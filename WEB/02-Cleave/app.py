from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        template = '<h2>Welcome agent!, %s!</h2>' % request.form.get('name', 'W')
        return render_template_string(template, **request.form)
    else:
        return render_template_string('''
            <form method="POST">
                <label for="name">Enter your name:</label><br>
                <input type="text" id="name" name="name"><br>
                <input type="submit" value="Submit">
            </form>
        ''')
        #EspionageCTF{u5e_sEcUr3
if __name__ == "__main__":
    app.run(debug=True)