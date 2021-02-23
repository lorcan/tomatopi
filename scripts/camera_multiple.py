#!/usr/bin/env python3
import argparse
from picamera import PiCamera
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("--count", type=int, default=6, help="the number of photos to take")
parser.add_argument("--sleep", type=int, default=10, help="sleep for this amount of seconds between photos")
parser.add_argument("--out", default='.', help="the directory where we will save the photos")

args = parser.parse_args()

print("Taking {} photos, separated by {}s each and saving them to {}".format(args.count, args.sleep, args.out))

with PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(camera.capture_continuous(args.out + '/image-{timestamp:%Y-%m-%d-%H-%M-%S}.jpg')):
            if i == args.count:
                break
            print(filename)
            sleep(args.sleep)
    finally:
        camera.stop_preview()
        camera.close()


