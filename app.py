from flask import Flask,jsonify,render_template
import os
import socket
app=Flask(__name__)
 
#find the hostname and machine ip
 
 
def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

def findaddress():
    phone_number="09083456781"
    emailaddress="df@gmail.com"
    companyaddress= "4 Ojo road, Ogba, Lagos"
    return str(phone_number),str(emailaddress),str("companyaddress")


@app.route("/")
def home():
    return "Welcome to my page"

@app.route("/score")
def calculate():
    a=1000
    b=150
    c=a+b
    return render_template("index.html", finalscore=c)


    
@app.route("/details")
def hostname():
    myhost,myip=findhostname()
    return render_template('show.html',host=myhost,IP=myip)

@app.route("/aboutUs")
def aboutUs():
    phone_number,emailaddress,companyad=findaddress()
    return render_template('aboutUs.html',phoneno=phone_number, email=emailaddress, address=companyad)



if __name__ == '__main__':
    app.run(debug=True, port=5001,host="127.0.0.1")

    
