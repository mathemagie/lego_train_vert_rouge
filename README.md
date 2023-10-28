# Train Control

This code controls a train motor using a PoweredUpHub and a speed value read from a file. The motor speed is updated whenever the value in the file changes.

## Installation

To run this code, you will need to install the `curio`, `bricknil`, and `bricknil_sensor` packages. You can do this using pip:

```console
pip install curio bricknil bricknil_sensor
```

```console
python train.py
```

Launch WebAPI for the train

```console
python server.py
```

To use the api_train API, you can make HTTP GET requests to the following URLs:

* http://127.0.0.1:5000/api_train?vitesse=0: Sets the train speed to 0.
* http://127.0.0.1:5000/api_train?vitesse=60: Sets the train speed to 60.

To use these APIs, you can open a web browser or use a tool like curl to make the HTTP requests. For example:
