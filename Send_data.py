# Import library and create instance of REST client.
import time
import subprocess
from Adafruit_IO import Client
aio = Client('BENUTZERNAME', 'PRIVATER_SCHLUESSEL')

#Name the feed
print("name the feed")
feedname = input()

while True:

        #Temperatur kriegen
        output = subprocess.check_output (["vcgencmd", "measure_temp"]).decode().strip()

        temp = output.replace("temp=", "").replace("'C","")

        # Add the value 98.6 to the feed 'Temperature'.
        test = aio.feeds(feedname)
        aio.send_data(test.key, temp)
        time.sleep(5)
