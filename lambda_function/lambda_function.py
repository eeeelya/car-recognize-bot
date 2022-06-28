import json
import numpy as np
from model import CarNet
import boto3


def lambda_handler(event, context):
    image = np.asarray(event["image"], dtype=np.float32)

    S3 = boto3.client("s3",
                      region_name="eu-north-1")

    obj = S3.get_object(Bucket='car-recognize-bot', Key='model.onnx')
    response = obj['Body'].read()

    model = CarNet(response)
    result = model(image)

    return {"statusCode": 200, "body": json.dumps(result)}
