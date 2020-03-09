from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")

def main():
   return render_template('main.html')


@app.route("/<pin>/<action>")
def action(pin, action):
   if pin == "pin1" and action == "on":
       os.system('echo 1=210 /dev/servoblaster')
      

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)