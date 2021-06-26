from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./upload/"



@app.route('/')
def test():
    return "Hello"


@app.route('information', methods=['GET'])
def info():
    return render_template('info.html')

@app.route('/upload', methods=['Get', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            #will call evulation
            #get result
            #delete image
            #return result
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")