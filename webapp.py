from flask import Flask, render_template, flash, redirect, request, session, abort

app = Flask(__name__)
@app.route("/test")
def test():
    return render_template('demo.html')
    
if __name__ == "__main__":
    app.run()

