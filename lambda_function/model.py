import onnxruntime
import numpy as np


class CarNet:

    def __init__(self, model):
        self.model = model

    def __call__(self, image):
        session = onnxruntime.InferenceSession(self.model)
        result = session.run(None, {'input': image})[0]

        indexes = np.argpartition(result[0], -3)[-3:]
        values = result[0][indexes]

        masks = dict(zip(indexes.tolist(), values.tolist()))

        return masks