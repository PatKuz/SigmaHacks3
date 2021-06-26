from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./upload/"



@app.route('/')
def test():
    return "Hello"

@app.route('/upload', methods=['Get', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")