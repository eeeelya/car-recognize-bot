import io
import json
import boto3
import cv2
import numpy as np
import pandas as pd

from bot.config import S3_KEY, S3_SECRET_KEY

NAMES = pd.read_csv("names.csv", header=None, names=['name']).reset_index()


async def read_image(image: io.BytesIO) -> np.ndarray:
    image.seek(0)
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.COLOR_BGR2RGB)

    image = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_NEAREST)
    normalize_image = await normalization(image)

    return normalize_image


async def normalization(image: np.ndarray) -> np.ndarray:
    mean = 255 * np.array([0.5, 0.5, 0.5])
    std = 255 * np.array([0.5, 0.5, 0.5])
    image = image.transpose(-1, 0, 1)
    image = (image - mean[:, None, None]) / std[:, None, None]
    image = np.expand_dims(image, 0).astype(np.float32)

    return image


def launch_calculations(image: np.ndarray):
    aws_lambda = boto3.client(
        "lambda", aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET_KEY, region_name="eu-north-1"
    )

    parameters = {
        "image": image.tolist(),
    }
    result = aws_lambda.invoke(
        FunctionName="car-bot",
        InvocationType="RequestResponse",
        Payload=json.dumps(parameters),
    )
    response = json.loads(result["Payload"].read())

    return json.loads(response)


async def get_results(response):
    answer = []

    for item in dict(sorted(response.items(), key=lambda item: item[1], reverse=True)):
        answer.append(f"Car: {NAMES.iloc[item]['name']}. Confidence: {response[item]:.2f}\n")

    return "".join(answer)
