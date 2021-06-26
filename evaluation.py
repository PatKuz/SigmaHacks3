import sys, yaml
from google.cloud import automl

def get_prediction(file_path):
    print("Start")
    prediction_client = automl.PredictionServiceClient()
    creds = yaml.safe_load(open("creds.yaml", "r"))
    project_id = creds['PROJ_ID']
    model_id = creds['MODEL_ID']


    print("Here 1")
    with open(file_path, 'rb') as ff:
        content = ff.read()

    print("Here 2")
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {"score_threshold": "0.5"} #will need to change
    request = automl.PredictRequest(
        name=name,
        payload=payload,
        params=params
    )
    print("Here 3")
    print(prediction_client.predict(request=request))
    response = prediction_client.predict(request=request)
    print("here 4")
    print(response.payload)
    