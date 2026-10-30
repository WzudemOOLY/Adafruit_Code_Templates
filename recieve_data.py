# Import library and create instance of REST client.
import time
from Adafruit_IO import Client
aio = Client('BENUTZERNAME', 'PRIVATER_SCHLUESSEL')

while True:

        # Get the last value of the temperature feed.
        data = aio.receive('temp')

        # Print the value and a message if it's over 100.  Notice that the value is
        # converted from string to int because it always comes back as a string from IO.
        temp = float(data.value)
        print('Temperature: {0}'.format(temp),"'C")
        if temp > 100:
                print ("Hot enough for you?")
        time.sleep(5)
