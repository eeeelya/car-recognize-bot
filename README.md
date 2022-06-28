# Car Recognize Bot

Telegram bot that classify car on images. 

## Data

I used data from https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder, but
also I used my own transformation to get data for validation. You can find the script for this in the file script.py, 
also you need to go to the **_car data_** directory and run this script there:

```console
cd car_data
python script.py
```

## Model

You need to train the model using an example from _**model/car_recognize_bot.ipynb**_. Next, upload it to AWS S3.

## Launch

It is also necessary to load the function on AWS lambda for cloud computing.
An example of this function is located in the lambda_function directory.

## Usage

```console
docker-compose up --build
```
