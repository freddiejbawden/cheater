import cv2
import time
import datetime
import requests
import csv

f_api = open("api_code.txt", "r")
api_key = f_api.readline()


def pred_image(frame):
    headers = {'Ocp-Apim-Subscription-Key': api_key, 'Content-Type': 'application/octet-stream'}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'smile,emotion',
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=frame)
    jsonResponse = response.json()

    return jsonResponse[0]["faceId"], jsonResponse[0]["faceAttributes"]


face_api_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect'

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():  # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    ts = time.time()
    st = str(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))
    if key == 13:
        frame_bytes = cv2.imencode('.jpg', frame)[1].tobytes()
        _, face_atts = pred_image(frame_bytes)
        print(face_atts)
        key = cv2.waitKey()
        if key == 43:
            print("Truth")
            cv2.imwrite("Truth/" + st + ".jpg", frame)
            told = "1"
        if key == 45:
            print("Lie")
            cv2.imwrite("Lie/" + st + ".jpg", frame)
            told = "0"
        if key == 43 or key == 45:
            f = open("results.csv", "a")
            features = [told, st, str(face_atts["smile"])] + [str(face_atts["emotion"][emotion]) for emotion in
                                                         face_atts["emotion"].keys()]
            f.write(",".join(features) + "\n")
            f.close()
        if key == 27:  # exit on ESC
            cv2.destroyWindow("preview")
            break
