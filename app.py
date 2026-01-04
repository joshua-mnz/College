from flaskimport Flask
app = Flask(__name__)

@app.route("/")
defhome():
return"Hello from Dockerized App!"

app.run(host="0.0.0.0", port=8080)

