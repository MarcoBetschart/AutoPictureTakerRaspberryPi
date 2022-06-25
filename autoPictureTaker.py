from picamera import PiCamera
from os import system
import datetime
from time import sleep

intervalMinutes = 15
camera = PiCamera()
camera.resolution = (1024, 768)

def TakeAutoPictures():
    while(True):
        dateraw= datetime.datetime.now()
        folder = '/home/pi/projektarbeit/Timelapse/Timelapse/Images/{0}'.format(dateraw.strftime("%Y/%m/%d"))
        system('mkdir -vp ' + folder)
        filename = '/{0}.jpg'.format(dateraw.strftime("%H:%M"))
        camera.capture(folder + filename)
        print('Caputured picture ' + filename)
        sleep(intervalMinutes * 60)

if __name__ == '__main__':
    TakeAutoPictures()