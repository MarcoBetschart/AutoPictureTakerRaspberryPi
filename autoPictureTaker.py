from picamera import PiCamera
from os import system
import datetime
from time import sleep
import sqlite3

intervalMinutes = 15
camera = PiCamera()
camera.resolution = (1024, 768)
conn = sqlite3.connect('Timelapse/db.sqlite3')

def TakeAutoPictures():
    while(True):
        dateraw= datetime.datetime.now()
        folder = '/home/pi/projektarbeit/Timelapse/Timelapse/Images/'
        system('mkdir -vp ' + folder)
        filename = '/{0}.jpg'.format(dateraw.strftime("%Y%m%d_%H%M"))
        camera.capture(folder + filename)
        print('Caputured picture ' + filename)
        databasePath = 'Timelapse/Timelapse/Images/{0}.jpg'.format(dateraw.strftime("%Y%m%d_%H%M"))
        cursor = conn.cursor()
        insert = '''INSERT INTO Timelapse_timelapseimage (image, date, time) VALUES ('{0}', '{1}','{2}');'''.format(databasePath,str(dateraw.date()),str(dateraw.time()))
        cursor.execute(insert)
        conn.commit()
        sleep(intervalMinutes * 60)

if __name__ == '__main__':
    TakeAutoPictures()

#conn close