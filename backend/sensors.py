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

FLOW_SENSOR_PIN = 17 



TDS_POWER_PIN= 26

TRIG = 27  
ECHO = 24


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

def configure_water_level_sensor(trig_pin, echo_pin):

    chip = gpiod.chip(0)
    
    trig_line = chip.get_line(trig_pin)
    echo_line = chip.get_line(echo_pin)

    trig_config = gpiod.line_request()
    trig_config.request_type = gpiod.line_request.DIRECTION_OUTPUT
    trig_line.request(trig_config)

    echo_config = gpiod.line_request()
    echo_config.request_type = gpiod.line_request.DIRECTION_INPUT
    echo_line.request(echo_config)

    return trig_line, echo_line

def configure_tds_sensor(pin):
    
    chip = gpiod.chip(0)
    line = chip.get_line(pin)  # Retrieve the GPIO line for the sensor
    config = gpiod.line_request()
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT  # Set as output
    line.request(config)  # Apply the configuration
    return line

def configure_flow_sensor(pin):
   
    chip = gpiod.chip(0)
    line = chip.get_line(pin)  # Retrieve the GPIO line for the sensor
    config = gpiod.line_request()

    config.request_type= gpiod.line_request.EVENT_FALLING_EDGE
    
    line.request(config)

    return line


def toggle_water_level_sensor(line, state):
   
    if state:
        line.set_value(1)  # Turn ON (HIGH)
    else:
        line.set_value(0)  # Turn OFF (LOW)

def toggle_tds_sensor(line, state):
   
    if state:
        line.set_value(1)  # Turn ON (HIGH)
    else:
        line.set_value(0)  # Turn OFF (LOW)

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

    #print("voltage: "+str(voltage) + "     pH: "+str(ph_value))

        

    
    return ph_value + PH_CALIBRATION_OFFSET

def read_tds(adc_channel):
    """Read TDS value from TDS sensor (via ADS1115)."""
    voltage = ads.read_adc(adc_channel, gain=2) * (4.096 / 32767)  # Convert to voltage
    tds_value = voltage * TDS_FACTOR  # Adjust based on calibration
    return tds_value

def read_water_level(trig_line, echo_line):
    """Measure distance using HC-S203 ultrasonic sensor."""
    
    trig_line.set_value(0)
    time.sleep(0.1)
    trig_line.set_value(1)
    time.sleep(0.00001)
    trig_line.set_value(0)

    # Wait for the echo to start
    start_time = time.time()
    while echo_line.get_value() == 0:
        start_time = time.time()  # Wait for the echo signal to start

    # Wait for the echo to end
    while echo_line.get_value() == 1:
        end_time = time.time()  # Wait for the echo signal to end

    # Calculate duration of echo
    duration = end_time - start_time
    distance = (duration * 17150)  # Calculate distance based on speed of sound

    if distance <= 0:
        return -1  # Return error if distance is not valid

    return round(distance, 2)

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
    
    return flow_rate_lpm

def main():
    try:


        flow_line = configure_flow_sensor(FLOW_SENSOR_PIN)

        trig_line, echo_line = configure_water_level_sensor(TRIG, ECHO)


        

        tds_line = configure_tds_sensor(TDS_POWER_PIN)
        
        
        
            
            
        
            
        flow_rate= read_flow(flow_line, duration=1)

        flow_rate= round(flow_rate, 1)

        flow_rate= str(flow_rate) + " L/min"
    
    # Print the results
        #print(f"Flow rate: {flow_rate:.2f} L/min")
            

        light = read_light()

        if light > 500.0:

            light= "ON"
        else:

            light= "OFF"


        


        

        water_level = read_water_level(trig_line, echo_line)
        water_level = str(water_level) + " cm"



        toggle_tds_sensor(tds_line, True)

        time.sleep(5)

        tds = read_tds(2)


        tds= tds*434.78

        tds= int(tds)

        toggle_tds_sensor(tds_line, False)

        time.sleep(2)






        
        # Read all sensors
        temperature = read_temperature()
        
        ph = read_ph(1)  # Assuming pH is connected to ADC channel 0
          # Assuming TDS is connected to ADC channel 1

        ph= round(ph, 2)

        

        temperature= round(temperature, 1)



          # Assuming water level is ADC channel 2
        

        

        # Print the results
        #print(f"Temperature: {temperature} °C")
        #print(f"Light Intensity: {light}")
        #print(f"pH Value: {ph}")
        print(f"TDS Value: {tds} ppm")
        print(f"Water Level: {water_level}")
        #print(f"Flow Rate: {flow_rate}")
        #print("-" * 30)

        print("Data recorded")

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