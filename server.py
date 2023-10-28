from flask import Flask, send_file, request

app = Flask(__name__)


@app.route("/api_train", methods=["GET"])
def get_vitesse():
    vitesse = request.args.get("vitesse")
    if vitesse is not None:
        with open("speed.txt", "w") as f:
            f.write(vitesse)
        return "Vitesse saved to file."


@app.route("/")
def serve_index():
    return send_file("index.html")


if __name__ == "__main__":
    app.run()
