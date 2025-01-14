import time
import board
import busio
#import Adafruit_DHT
from w1thermsensor import W1ThermSensor
#from Adafruit_ADS1x15 import ADS1115
from adafruit_veml7700 import VEML7700
import RPi.GPIO as GPIO

# GPIO Pins
#FLOW_SENSOR_PIN = 23  # Example GPIO pin for water flow sensor (adjust as necessary)

# Initialize I2C for ADS1115 and VEML7700
i2c = busio.I2C(board.SCL, board.SDA)
#ads = ADS1115()  # Initialize ADC
light_sensor = VEML7700(i2c)

# Initialize water flow sensor
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(FLOW_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize DS18B20 temperature sensor
temp_sensor = W1ThermSensor()

# Placeholder for pH and TDS calibration
#PH_CALIBRATION_OFFSET = 0.0
#TDS_FACTOR = 0.5

def read_temperature():
    """Read temperature from DS18B20."""
    return temp_sensor.get_temperature()

def read_light():
    """Read ambient light from VEML7700."""
    return light_sensor.lux

#def read_ph(adc_channel):
  #  """Read pH value from pH sensor (via ADS1115)."""
   # voltage = ads.read_adc(adc_channel, gain=1) * (4.096 / 32767)  # Convert to voltage
  #  ph_value = 7 + (voltage - 2.5)  # Adjust based on calibration
   # return ph_value + PH_CALIBRATION_OFFSET

#def read_tds(adc_channel):
    """Read TDS value from TDS sensor (via ADS1115)."""
    voltage = ads.read_adc(adc_channel, gain=1) * (4.096 / 32767)  # Convert to voltage
    tds_value = voltage * TDS_FACTOR  # Adjust based on calibration
    return tds_value

#def read_water_level(adc_channel):
    """Read water level from analog water level sensor."""
    return ads.read_adc(adc_channel, gain=1)

#def read_flow():
    """Read water flow rate."""
    pulse_count = 0

    def count_pulse(channel):
        nonlocal pulse_count
        pulse_count += 1

    GPIO.add_event_detect(FLOW_SENSOR_PIN, GPIO.FALLING, callback=count_pulse)
    time.sleep(1)  # Measure for 1 second
    GPIO.remove_event_detect(FLOW_SENSOR_PIN)
    flow_rate = (pulse_count / 7.5)  # Adjust based on YF-S201 datasheet
    return flow_rate

def main():
    try:
        
        # Read all sensors
        temperature = read_temperature()
        light = read_light()
        #ph = read_ph(0)  # Assuming pH is connected to ADC channel 0
        #tds = read_tds(1)  # Assuming TDS is connected to ADC channel 1
        #water_level = read_water_level(2)  # Assuming water level is ADC channel 2
        #flow_rate = read_flow()

        # Print the results
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Light Intensity: {light:.2f} lx")
        # print(f"pH Value: {ph:.2f}")
        # print(f"TDS Value: {tds:.2f} ppm")
        # print(f"Water Level: {water_level}")
        #print(f"Flow Rate: {flow_rate:.2f} L/min")
        # print("-" * 30)

        values = []

        values.append(temperature)
        values.append(light)

        return values

            

    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()

if __name__ == "__main__":
    main()