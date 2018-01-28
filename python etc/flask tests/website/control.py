from flask import Flask, render_template

app= Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) #this line will be only executed if this script is executed, will not run if this script is imported