from mnist import MNIST
from flask import Flask, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mndata = MNIST('samples')
images, labels = mndata.load_training()


@app.route("/images", methods={"GET"})
def getImages():
    send_images = []
    number = int(request.args.get("quantity", default=10))
    for i in range(number):
        print(i)
        send_images.append(images[i])
    response = app.response_class(response=json.dumps(send_images), status=200, mimetype="application/json")
    return response


if __name__ == '__main__':
    app.run()
