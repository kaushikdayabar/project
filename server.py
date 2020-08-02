from flask import *
from ui1 import cf
import os
import des
import ses
import sma
import pslr
import yslr
import pbase
import ybase
import dsma
import dses
import ddes
import dpslr
import dyslr
import dpbase
import dybase

app=Flask(__name__)
app.secret_key="abc"

@app.route("/",methods=["get","post"])
def home():
    form=cf()
    if form.validate()==False:
        flash("all fields are required")
    return render_template("home.html",f=form)

@app.route("/cal",methods=["get","post"])
def calc():
    resu=request.form
    if resu["freq"]=="m" and resu["tech"]=="e1":
           l=des.des()
    elif resu["freq"]=="m" and resu["tech"]=="e":
           l=ses.ses()
    elif resu["freq"]=="m" and resu["tech"]=="a":
           l=sma.sma()
    elif resu["freq"]=="m" and resu["tech"]=="pslr":
           l=pslr.pslr()
    elif resu["freq"]=="m" and resu["tech"]=="yslr":
           l=yslr.yslr()
    elif resu["freq"]=="m" and resu["tech"]=="b":
           l=pbase.pbase()
    elif resu["freq"]=="m" and resu["tech"]=="y":
           l=ybase.ybase()
    elif resu["freq"]=="d" and resu["tech"]=="a":
          l=dsma.dsma()
    elif resu["freq"]=="d" and resu["tech"]=="e":
           l=dses.dses()
    elif resu["freq"]=="d" and resu["tech"]=="e1":
           l=ddes.ddes()
    elif resu["freq"]=="d" and resu["tech"]=="pslr":
          l=dpslr.dpslr()
    elif resu["freq"]=="d" and resu["tech"]=="yslr":
           l=dyslr.dyslr()
    elif resu["freq"]=="d" and resu["tech"]=="b":
           l=dpbase.dpbase()
    elif resu["freq"]=="d" and resu["tech"]=="y":
           l=dybase.dybase()

    return render_template("home.html",f=resu["freq"],t=resu["tech"],ins=l[0],oos=l[1],rmse=l[2])

if __name__=="__main__":
    app.run(debug=True)
