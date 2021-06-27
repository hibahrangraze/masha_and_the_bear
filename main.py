from flask import Flask , render_template , request
app=Flask(__name__)
@app.route("/")
def home():
    Name="HIBAH"
    return render_template("main.html",name=Name)

@app.route("/frm",methods=["GET","POST"])
def frm():
    Name="HIBAH"
    if request.method == "POST":
        num1=request.form["num1"]
        num2=request.form["num2"]
        num3=request.form["num3"]
        add=int(num1)+int(num2)+int(num3)
        return render_template("main.html",addition=add)
    return render_template("main.html",name=Name)


if __name__=="__main__":
    app.run(debug=True,port=5000)