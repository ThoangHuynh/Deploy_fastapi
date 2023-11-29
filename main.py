from fastapi import FastAPI
from joblib import load
import numpy as np
import uvicorn
from pydantic import BaseModel

app = FastAPI()

model = load('model.joblib')



@app.get("/")
async def root():
   return {"message": "Welcome to FastAPI"}

class Info(BaseModel):
    age: float
    bmi: float
    bp: float

@app.post("/predict")
def predict(people: Info):
    data = np.array([[people.age, people.bmi, people.bp]])
    glu_prediction = model.predict(data)

    if glu_prediction <= 100:
        conclusion = "Patient is nomal"
    elif glu_prediction > 100 and glu_prediction <= 125:
        conclusion = "Patient has pre-diabetes"
    else:
        conclusion = "Patient has diabetes"

    return {
        'prediction': glu_prediction[0],
        'conclusion': conclusion
   }


if __name__ == '__main__':
   uvicorn.run(app, host='localhost', port=8000)