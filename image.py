import cv2
import os
import time
import uuid

IMAGES_PATH = "Tensorflow/workspace/images/collectedimages"

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)  # Create the directory if it doesn't exist

    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        image_name = os.path.join(label_path, label + '.' + f'{str(uuid.uuid1())}.jpg')
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
