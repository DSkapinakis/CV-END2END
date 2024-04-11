# Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from typing import List
import io
import numpy as np
import sys
import mimetypes

model = load_model(r'C:/Users/dskapinakis/Documents/computer_vision_concrete/saved_models/cnn_cracks.keras')
input_shape = model.layers[0].input_shape
app = FastAPI()

class Prediction(BaseModel):
    filename: str
    contenttype: str
    prediction: float
    
# Define the main route
@app.get('/')
def root_route():
  return { 'error': 'Use POST /prediction instead of the root route!' }

# Define the /prediction route
@app.post('/prediction', response_model=Prediction)
async def prediction_route(file: UploadFile = File(...)):

    content_type = mimetypes.guess_type(file.filename)

    try:
        # Read image contents
        contents = await file.read()
        pil_image = Image.open(io.BytesIO(contents))

        # Resize image to expected input shape
        pil_image = pil_image.resize((input_shape[1], input_shape[2]))

        # Convert from RGBA to RGB *to avoid alpha channels*
        if pil_image.mode == 'RGBA':
            pil_image = pil_image.convert('RGB')

        # Expand the shape of the array (one sample)
        numpy_image = np.expand_dims(pil_image, axis=0)

        # Generate prediction
        predictions = model.predict(numpy_image)
        prediction = predictions[0][0]

        return {
        'filename': file.filename,
        'contenttype': content_type[0],
        'prediction': prediction.tolist(),
        }
    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
