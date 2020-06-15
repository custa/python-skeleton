import ssl
import time
import nsq
import json
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser(description="probe images from nsq")
parser.add_argument('--server', type=str, help="NSQ Server", required=True)
parser.add_argument('--topic', type=str, help="topic(s) to read", nargs="+")
args = parser.parse_args()

im = []
count = 0
stats = []


def handler(message):
    global count
    count += 1
    t0 = time.time()
    obj = json.loads(message.body)
    base64ed = obj.get('image')
    device_code = obj.get('device_code')
    occur_time = obj.get('occur_time')
    t1 = time.time()
    load_time = t1 - t0
    binary_data = base64.b64decode(base64ed)
    t2 = time.time()
    b64decode_time = t2 - t1
    # with open("save.jpg", "wb") as f:
    #     f.write(binary_data)
    image = Image.open(BytesIO(binary_data))
    # image = cv2.resize(image, (1, 2))
    t3 = time.time()
    binary_image_time = t3 - t2
    global im
    im = np.asarray(image)
    t4 = time.time()
    asarray_time = t4 - t3

    # cv2.putText(im, "occur_time: " + occur_time, (10, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    # cv2.namedWindow(device_code, 0)
    # cv2.resizeWindow(device_code, 640, 480)
    cv2.imshow(device_code, im)
    cv2.waitKey(1)
    t5 = time.time()
    show_time = t5 - t4
    message.finish()
    t6 = time.time()
    total_time = t6 - t0
    # print(
    #     "load {:.3f}, base64 decode {:.3f}, binary to image {:.3f}, image to ndarray {:.3f}, show {:.3f}, total {:.3f}"
    #     .format(load_time, b64decode_time, binary_image_time, asarray_time,
    #             show_time, total_time))
    global stats
    stats.append([
        load_time, b64decode_time, binary_image_time, asarray_time, show_time,
        total_time
    ])
    if count % 10 == 0:
        mean = np.mean(stats, axis=0)
        print(
            "Mean: load {:.3f}, base64 decode {:.3f}, binary to image {:.3f}, image to ndarray {:.3f}, show {:.3f}, total {:.3f}"
            .format(
                mean[0],
                mean[1],
                mean[2],
                mean[3],
                mean[4],
                mean[5],
            ))
        stats = []


if __name__ == "__main__":

    opts = {
        'cert_reqs': ssl.CERT_REQUIRED,
        'keyfile': 'client-key.pem',
        'certfile': 'client-cert.pem',
        'ca_certs': 'ca-cert.pem',
    }
    for t in args.topic:
        nsq.Reader(message_handler=handler,
                   nsqd_tcp_addresses=[args.server],
                   topic=t,
                   channel="hello#ephemeral",
                   tls_v1=True,
                   tls_options=opts,
                   max_in_flight=10)

    nsq.run()
