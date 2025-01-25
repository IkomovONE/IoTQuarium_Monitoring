import time
import board
import busio
#import Adafruit_DHT
from w1thermsensor import W1ThermSensor
from Adafruit_ADS1x15 import ADS1115
from adafruit_veml7700 import VEML7700
import gpiod
from datetime import timedelta

# GPIO Pins
CHIP_PATH = "/dev/gpiochip0"  # Adjust the chip number as per your setup
FLOW_SENSOR_PIN = 17 


# Initialize I2C for ADS1115 and VEML7700
i2c = busio.I2C(board.SCL, board.SDA)
ads= ADS1115(address=0x48, busnum=1)  # Initialize ADC
light_sensor = VEML7700(i2c)

# Initialize water flow sensor
# Constants
PULSES_AT_1_LPM = 7.5
PULSES_AT_30_LPM = PULSES_AT_1_LPM * 30  # Pulses at 30 L/min


# Initialize DS18B20 temperature sensor
temp_sensor = W1ThermSensor()

# Placeholder for pH and TDS calibration
PH_CALIBRATION_OFFSET = 0.0
TDS_FACTOR = 0.5



def configure_flow_sensor(chip_path, pin):
    """Configure the GPIO line for water flow sensor."""

    
    

    chip = gpiod.chip(0)
    line = chip.get_line(pin)  # Retrieve the GPIO line for the sensor
    config = gpiod.line_request()

    config.request_type= gpiod.line_request.EVENT_FALLING_EDGE

    

    
    
    
    line.request(config)

    
    return line

def read_temperature():
    """Read temperature from DS18B20."""
    return temp_sensor.get_temperature()

def read_light():
    """Read ambient light from VEML7700."""
    return light_sensor.lux

def read_ph(adc_channel):
    

    voltage = ads.read_adc(adc_channel, gain=1) * (4.096 / 32767)  # Convert to voltage

    

    #print("voltage: "+str(voltage))

    time.sleep(0.5)

    m = -5.436


    ph_value = 7 - (2.5 - voltage) * m; # Adjust based on calibration

    ph_value= round(ph_value, 3)

    voltage= round(voltage, 3)

    print("voltage: "+str(voltage) + "     pH: "+str(ph_value))

        

    
    return ph_value + PH_CALIBRATION_OFFSET

def read_tds(adc_channel):
    """Read TDS value from TDS sensor (via ADS1115)."""
    voltage = ads.read_adc(adc_channel, gain=2) * (4.096 / 32767)  # Convert to voltage
    tds_value = voltage * TDS_FACTOR  # Adjust based on calibration
    return tds_value

def read_water_level(adc_channel):
    """Read water level from analog water level sensor."""
    return ads.read_adc(adc_channel, gain=1)

def read_flow(line, duration):
    """Read the flow sensor value and calculate flow rate in L/min."""
    
    pulse_count = 0
    start_time = time.time()
    
    # Measure flow rate by counting pulses over the specified duration
    while time.time() - start_time < duration:
        # Wait for an event on the line (with a timeout of 1 second)
        timeout = timedelta(seconds=1)  # Timeout set to 1 second
        event = line.event_wait(timeout=timeout)  # Wait for falling edge event
        
        if event:
            line.event_read()  # Read the event to reset the event flag
            pulse_count += 1  # Count the pulse
    
    # Calculate the flow rate based on the number of pulses detected
    if pulse_count == 0:
        flow_rate_lpm = 0  # No pulses detected, no flow
    else:
        # Linear scale from 1 L/min to 30 L/min based on pulses
        flow_rate_lpm = (pulse_count / PULSES_AT_1_LPM)  # This scales linearly from 1 L/min to 30 L/min
    
    return flow_rate_lpm, pulse_count

def main():
    try:


        line = configure_flow_sensor(CHIP_PATH, FLOW_SENSOR_PIN)
        
        
        
            
            
        
            
        flow_rate, pulse_count = read_flow(line, duration=1)
    
    # Print the results
            #print(f"Flow rate: {flow_rate:.2f} L/min (based on {pulse_count} pulses in 10 seconds)")
            




        
        # Read all sensors
        temperature = read_temperature()
        light = read_light()
        ph = read_ph(1)  # Assuming pH is connected to ADC channel 0
        tds = read_tds(2)  # Assuming TDS is connected to ADC channel 1
        water_level = read_water_level(3)  # Assuming water level is ADC channel 2
        #flow_rate = read_flow()

        tds= tds*434.78

        # Print the results
        print(f"Temperature: {temperature:.2f} °C")
        print(f"Light Intensity: {light:.2f} lx")
        print(f"pH Value: {ph:.2f}")
        print(f"TDS Value: {tds:.2f} ppm")
        print(f"Water Level: {water_level}")
        print(f"Flow Rate: {flow_rate:.2f} L/min")
        print("-" * 30)

        #time.sleep(1)

        values = []

        values.append(temperature)
        values.append(light)
        values.append(ph)
        values.append(tds)
        values.append(water_level)
        values.append(flow_rate)

        
        

        return values

            

    except KeyboardInterrupt:
        print("Exiting...")
        

if __name__ == "__main__":
    main()