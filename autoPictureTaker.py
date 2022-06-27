from picamera import PiCamera
from os import system
import datetime
from time import sleep
import sqlite3

intervalMinutes = 15
camera = PiCamera()
camera.resolution = (1024, 768)
connection = sqlite3.connect('Timelapse/db.sqlite3')

def TakeAutoPictures():
    while(True):
        dateraw = datetime.datetime.now()
        folder = '/home/pi/projektarbeit/Timelapse/Timelapse/Images/'
        system('mkdir -vp ' + folder) # Create images folder if not exists
        filename = '/{0}.jpg'.format(dateraw.strftime("%Y%m%d_%H%M"))
        camera.capture(folder + filename) # Caputre image an save in defined path
        print('Caputured picture ' + filename)
        databasePath = 'Timelapse/Timelapse/Images/{0}.jpg'.format(dateraw.strftime("%Y%m%d_%H%M")) # Path to save on database 
        cursor = connection.cursor()
        insertString = '''INSERT INTO Timelapse_timelapseimage (image, date, time) VALUES ('{0}', '{1}','{2}');'''.format(databasePath, str(dateraw.date()), str(dateraw.time())) 
        cursor.execute(insertString)
        connection.commit()
        sleep(intervalMinutes * 60) # Wait minutes defined in intervalMinutes

if __name__ == '__main__':
    try:
        TakeAutoPictures()
    except KeyboardInterrupt:
        print("AutoPictureTaker stopped working.")
        connection.close()