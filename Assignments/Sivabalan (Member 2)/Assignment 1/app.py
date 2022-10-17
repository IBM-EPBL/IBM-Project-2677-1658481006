from flask import Flask, request, render_template
 
app = Flask(__name__)  

@app.route('/', methods =["GET", "POST"])
def fun():
    if request.method == "POST":
       
       first_name = request.form.get("uname")
       mail_id = request.form.get("umail")
       mobile = request.form.get("uphn")
       return "Your name is "+first_name+" "+"you have logged in with this mail id : "+mail_id+" and phone : "+mobile
    return render_template("home.html")
 
if __name__=='__main__':
   app.run()