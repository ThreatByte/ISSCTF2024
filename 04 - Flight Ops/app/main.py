from flask import Flask, render_template, jsonify, request, redirect
import os

FLAG = "EspionageCTF{cl13nt_s1d3_val1dat10n_st1ll_3x1sts}"
app = Flask(__name__,  static_url_path='/static', static_folder='static')

# main views
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/check_user", methods = ["POST"])
def unauthorized():
    user_input = request.json
    if user_input['username'] == "admin":
        return jsonify({"response": FLAG})
    else:
        return jsonify({"response": "You are not authorized for remote login!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')