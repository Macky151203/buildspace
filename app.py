from flask import Flask, render_template, request
import apr as a



app = Flask(__name__)

m="Enter the Number"

@app.route("/",methods=["GET","POST"])
def sal():
    
    global m
   
    if request.method=="POST":
        pred=a.apyo()
        m=str(pred)
        print("hi im out")
    return render_template("index.html",prediction=m)

if __name__=="__main__":
    app.run(debug=True)