from flask import Flask,render_template,redirect,url_for,request
import webview
import threading
import sys
from win32api import GetSystemMetrics

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")

#if __name__== "__main__":
#    app.run(debug=True)

from webview.platforms.cef import settings
settings.update({
    'persist_session_cookies': True
})

def start_server():
    app.run(host='127.0.0.1', port=5000)

if __name__ == "__main__":

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("SCRIPT", "http://localhost:5000", width=(GetSystemMetrics(0)-50), height=(GetSystemMetrics(1)-100),resizable=False,confirm_close=True)
    webview.start(gui='cef')
  
    sys.exit()