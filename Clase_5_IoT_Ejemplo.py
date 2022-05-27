import random
import time

TEMPERATURE = 10.0
HUMIDITY = 60
 
    
def iot():
    try:
       
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Construya el mensaje con valores de telemetría simulados.
            temperature = TEMPERATURE + (random.random() * 4)
            humidity = HUMIDITY + (random.random() * 20)
           
          
            print ( "mensaje enviado con exito" )
            print ( temperature )
            print ( humidity )

            time.sleep(10)
    except KeyboardInterrupt:
        print ( "IoTHubClient simulacion detenida" )
if __name__ == '__main__':
    iot()
