#import library
from flask import Flask,request,app,url_for,render_template
from pdf2image import convert_from_path
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
IMAGE_FOLDER = "pdf_images"

#redirect to html page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    #get uploaded PDF
    pdf_file = request.files['pdf_file']

    #save PDF
    pdf_path = os.path.join(
        UPLOAD_FOLDER,
        pdf_file.filename
    )

    pdf_file.save(pdf_path)

    print("PDF Saved:", pdf_path)

    # Convert PDF into images
    images = convert_from_path(pdf_path)

    # Save images
    for i, image in enumerate(images):

        image_path = os.path.join(
            IMAGE_FOLDER,
            f"page_{i+1}.png"
        )

        image.save(image_path, "PNG")

        print("Saved:", image_path)

    return "PDF Converted Successfully!"


#create condition for run code
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)