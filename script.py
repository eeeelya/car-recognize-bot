import os
import shutil

valid_dir = "./car_data/valid"
test_dir = "./car_data/test"

for dir_ in os.listdir(test_dir):

    os.mkdir(os.path.join(valid_dir, dir_))
    files = os.listdir(os.path.join(test_dir, dir_))

    for i in range(len(files) // 2):
        shutil.move(os.path.join(test_dir, dir_, files[i]), os.path.join(valid_dir, dir_, files[i]))
