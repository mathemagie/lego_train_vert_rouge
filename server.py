from flask import Flask, send_file, request

app = Flask(__name__)


@app.route("/vitesse", methods=["GET"])
def get_vitesse():
    vitesse = request.args.get("vitesse")
    if vitesse is not None:
        with open("vitesse.txt", "w") as f:
            f.write(vitesse)
        return "Vitesse saved to file."


@app.route("/")
def serve_index():
    return send_file("index.html")


if __name__ == "__main__":
    app.run()
