from flask import Flask, request, render_template
import os
from evaluation import get_prediction


app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./upload/"



@app.route('/')
def test():
    return render_template("index.html")


@app.route('/information', methods=['GET'])
def info():
    return render_template('info.html')

@app.route('/upload', methods=['Get', 'POST'])
def upload_image():
    if request.method == "POST":
        print("This was called")
        if request.files:
            print("Got the file")
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], 'file.jpg'))
            #will call evulation
            response = get_prediction('upload/file.jpg')
            print("Printing payload")
            x = response.payload
            for item in response.payload:
                result = item.display_name
            # print(result.payload)
            #get result
            #delete image
            #return result
            return render_template("upload.html", result=result)
    return render_template("upload.html")