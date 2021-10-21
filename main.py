from flask import Flask, render_template, request
import io

app = Flask(__name__)

with io.open("kerulets.txt", mode="r", encoding="utf-8") as f :
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
        return render_template("register.html", error="neved 3 karakter hossz..", usr=usr, pswd=pswd)

    if not len(pswd) > 2 :
        return render_template("register.html", error="szavad 3 karakter hossz..", usr=usr, pswd=pswd)

    if len(pswd) > 32 :
        return render_template("register.html", error="szavad 365 (nap trianon végéig) karakter hossz-nál több..", usr=usr, pswd=pswd)

    if not listInStr(["1","2","3","4","5","6","7","8","9"], pswd) :
        return render_template("register.html", error="kell egy number ami nem 0", usr=usr, pswd=pswd)
    
    if not listInStr(["?","!","#","@"], pswd) :
        return render_template("register.html", error="ezekből jelszó egy & több: ?!#@", usr=usr, pswd=pswd)
    
    if not listInStr(capitals, pswd) :
        return render_template("register.html", error="legyen egy kerület jelszóban", usr=usr, pswd=pswd)

    return "<h3>istenáldmegamagyart bass boosted..</h3>"

app.run(debug=False, host="0.0.0.0", port=5000) 
