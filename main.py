from flask import Flask, render_template, request
import io

app = Flask(__name__)

with io.open("capitals.txt", mode="r", encoding="utf-8") as f :
    capitals = f.read().split("\n")

def listInStr(list, str) :
    for x in list :
        if x.lower() in str.lower() :
            return True
    return False

#-----------------------------------------------#

@app.route("/register")
def register() :
    return render_template("register.html", error="")

@app.route("/register-handler", methods=["POST"])
def registerHandler() :
    usr = request.form["username"]
    pswd = request.form["password"]

    if not len(usr) > 2 :
        return render_template("register.html", error="Your username must be at least 3 characters long..", usr=usr, pswd=pswd)

    if not len(pswd) > 2 :
        return render_template("register.html", error="Your password must be at least 3 characters long..", usr=usr, pswd=pswd)

    if len(pswd) > 32 :
        return render_template("register.html", error="Your password cannot be longer than 32 characters for no reason whatsoever..", usr=usr, pswd=pswd)

    if not listInStr(["0","1","2","3","4","5","6","7","8","9"], pswd) :
        return render_template("register.html", error="Your password must include at least 1 number", usr=usr, pswd=pswd)
    
    if not listInStr(["?","!","#","@"], pswd) :
        return render_template("register.html", error="Your password must include at least 1 of theese characters: ?!#@", usr=usr, pswd=pswd)
    
    if not listInStr(capitals, pswd) :
        return render_template("register.html", error="Your password must include at least 1 capital", usr=usr, pswd=pswd)

    return "<h3>You are now registered..</h3>"

app.run(debug=False, host="0.0.0.0", port=5000) 