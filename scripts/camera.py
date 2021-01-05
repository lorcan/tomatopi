#!/usr/bin/env python3
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture('public/photos/snap.jpg')
camera.stop_preview()
print('photo taken')
