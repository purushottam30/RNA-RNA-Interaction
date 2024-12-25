from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Available models
MODEL_OPTIONS = ["Model 1", "Model 2", "Model 3"]

@app.route('/')
def upload_page():
    return render_template('upload.html')

@app.route('/results', methods=['POST'])
def results_page():
    # Retrieve form inputs
    selection_type = request.form.get('selection_type')
    manual_model = request.form.get('manual_model')
    fileA = request.files.get('fileA')
    fileB = request.files.get('fileB')

    # Determine the selected model
    if selection_type == "manual" and manual_model:
        selected_model = manual_model
    elif selection_type == "random":
        selected_model = random.choice(MODEL_OPTIONS)
    elif selection_type == "automatic":
        selected_model = "Automatic Model Selection Applied"
    else:
        selected_model = "No model selected"

    # Simulate processing and pass data to the results page
    return render_template(
        'results.html',
        selected_model=selected_model,
        fileA=fileA.filename if fileA else "Not Uploaded",
        fileB=fileB.filename if fileB else "Not Uploaded"
    )

if __name__ == '__main__':
    app.run(debug=True)
