import time
import board
import busio
from w1thermsensor import W1ThermSensor             #Importing necessary libraries
from Adafruit_ADS1x15 import ADS1115
from adafruit_veml7700 import VEML7700
import gpiod
from datetime import timedelta



FLOW_SENSOR_PIN = 17 
TDS_POWER_PIN= 26       #Initializing Raspberry Pi pins
TRIG = 27  
ECHO = 24

PULSES_AT_1_LPM = 7.5                       #Constants for water flow sensor
PULSES_AT_30_LPM = PULSES_AT_1_LPM * 30  # Pulses at 30 L/min
PH_CALIBRATION_OFFSET = 0.0             #Placeholders for pH and TDS
TDS_FACTOR = 0.5


i2c = busio.I2C(board.SCL, board.SDA)       #Inializing i2c for SCL/SDA input

ads= ADS1115(address=0x48, busnum=1)        #Inializing ADS 1115 board for converting analogue to digital input

light_sensor = VEML7700(i2c)            #Initializing light sensor based on i2c

temp_sensor = W1ThermSensor()                       #Initialize DS18B20 temperature sensor



######### SENSORS' CONFIGURATION METHODS START HERE ##########################

##### Using gpiod for configuring ###########

def configure_water_level_sensor(trig_pin, echo_pin):           #Configuring water level sensor
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


def configure_tds_sensor(pin):          #Configuring TDS sensor
    chip = gpiod.chip(0)
    line = chip.get_line(pin)  # Retrieve the GPIO line for the sensor
    config = gpiod.line_request()
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT  # Set as output
    line.request(config)  # Apply the configuration
    return line


def configure_flow_sensor(pin):         #Configuring water flow sensor
    chip = gpiod.chip(0)
    line = chip.get_line(pin)  # Retrieve the GPIO line for the sensor
    config = gpiod.line_request()
    config.request_type= gpiod.line_request.EVENT_FALLING_EDGE
    line.request(config)
    return line

#######################################################


############# SENSORS' CONTROL METHODS START HERE ########################################

def toggle_water_level_sensor(line, state):         #Method for toggling water level sensor ON/OFF
    if state:
        line.set_value(1)  # Turn sensor ON 
    else:
        line.set_value(0)  # Turn sensor OFF


def toggle_tds_sensor(line, state):                 #Method for toggling TDS sensor ON/OFF
    if state:
        line.set_value(1)  # Turn ON
    else:
        line.set_value(0)  # Turn OFF



def read_temperature():                     #Method for reading temperature values                                    
    return temp_sensor.get_temperature()


def read_light():                           #Method for reading light sensor value
    return light_sensor.lux


def read_ph(adc_channel):                   #Method for reading pH sensor
    voltage = ads.read_adc(adc_channel, gain=1) * (4.096 / 32767)  # Convert to voltage
    time.sleep(0.5)
    m = -5.436
    ph_value = 7 - (2.5 - voltage) * m;         #Adjust based on calibration
    ph_value= round(ph_value, 3)
    voltage= round(voltage, 3)
    return ph_value + PH_CALIBRATION_OFFSET


def read_tds(adc_channel):                                #Method for reading TDS sensor
    voltage = ads.read_adc(adc_channel, gain=2) * (4.096 / 32767)  # Convert to voltage
    tds_value = voltage * TDS_FACTOR  # Adjust based on calibration
    return tds_value


def read_water_level(trig_line, echo_line):             #Method for reading water level sensor
    trig_line.set_value(0)
    time.sleep(0.1)
    trig_line.set_value(1)      #Sending signal
    time.sleep(0.00001)
    trig_line.set_value(0)

    start_time = time.time()                    #Wait for the echo to start
    while echo_line.get_value() == 0:
        start_time = time.time()  #Wait for the echo signal to start
    while echo_line.get_value() == 1:
        end_time = time.time()  #Wait for the echo signal to end

    duration = end_time - start_time                #Calculate duration of echo
    distance = (duration * 17150)                   #Calculate distance based on speed of sound

    if distance <= 0:
        return -1               #Return error if distance is not valid

    return round(distance, 2)


def read_flow(line, duration):                      #Method for reading water flow sensor
    pulse_count = 0
    start_time = time.time()
    
    while time.time() - start_time < duration:                      #Measure flow rate by counting pulses over the specified duration
        timeout = timedelta(seconds=1)  
        event = line.event_wait(timeout=timeout) 
        if event:
            line.event_read()               #Read the event to reset the event flag
            pulse_count += 1                #Count the pulse
    
    if pulse_count == 0:                                    #Calculate the flow rate based on the number of pulses detected
        flow_rate_lpm = 0                   #No pulses detected, no flow
    else:
        flow_rate_lpm = (pulse_count / PULSES_AT_1_LPM)             #Linear scale from 1 L/min to 30 L/min based on pulses
    
    return flow_rate_lpm

##################################################################




############# MAIN METHOD STARTS HERE ###################################

def main():
    try:
        flow_line = configure_flow_sensor(FLOW_SENSOR_PIN)
        trig_line, echo_line = configure_water_level_sensor(TRIG, ECHO)     #Initializing sensor lines
        tds_line = configure_tds_sensor(TDS_POWER_PIN)


        flow_rate_status = "Not initialized"
        light_sensor_status = "Not initialized"
        water_level_sensor_status = "Not initialized"
        tds_sensor_status = "Not initialized"
        temp_sensor_status= "Not initialized"
        ph_sensor_status= "Not initialized"
        
           
        try:

            flow_rate= read_flow(flow_line, duration=1)
            flow_rate= round(flow_rate, 1)              #Measuring and processing water flow rate
            flow_rate= str(flow_rate) + " L/min"

            flow_rate_status = "OK"

        except Exception as e:
            print(f"[Error] Flow sensor: {e}")
            flow_rate = 0

            flow_rate_status = "Malfunction"

        try:


            light = read_light()
            if light > 500.0:
                light= "ON"                 #Measuring and processing light status
            else:
                light= "OFF"

            light_sensor_status = "OK"

        except Exception as e:
            print(f"[Error] Light sensor: {e}")
            light = "-"

            light_sensor_status = "Malfunction"


        try:

            max_level= 11.3             #Mentioning min-max levels thresholds
            min_level= 13.2

            level_list= []          #Water level list for precise measurement

            for i in range(0, 21):
                temp_water_level = read_water_level(trig_line, echo_line)       #Taking 20 water level measurements, then finding average
                level_list.append(temp_water_level)
            water_level= round(sum(level_list)/len(level_list), 2)
            print("Water level: "+ str(water_level)+ " cm")   


            if water_level <= max_level:
                water_level= "100%"
            elif water_level >= min_level:
                water_level= "0%"                                           #Calculating water level percentage
            else:
                percentage = ((min_level - water_level) / (min_level - max_level)) * 100
                percentage= round(percentage, 1)
                water_level= str(percentage) + "%"
                
            water_level = str(water_level)

            water_level_sensor_status = "OK"

        except Exception as e:
            print(f"[Error] Water level sensor: {e}")
            water_level = "-"

            water_level_sensor_status = "Malfunction"

       
        try:

            toggle_tds_sensor(tds_line, True)
            time.sleep(5)
            tds = read_tds(2)                               #Toggling TDS sensor ON, reading value, processing the value and toggling TDS sensor OFF
            tds= tds*434.78
            tds= int(tds)
            toggle_tds_sensor(tds_line, False)
            time.sleep(2)

            tds_sensor_status = "OK"

        except Exception as e:
            print(f"[Error] TDS sensor: {e}")
            tds = 0

            tds_sensor_status = "Malfunction"


        try:
       
            temperature = read_temperature()            #Reading and processing temperature
            temperature= round(temperature, 1)

            temp_sensor_status= "OK"

        except Exception as e:
            print(f"[Error] Temperature sensor: {e}")
            temperature = 0

            temp_sensor_status= "Malfunction"


        try:

            ph = read_ph(1)                 #Reading and processing pH value
            ph= round(ph, 2)

            ph_sensor_status= "OK"

        except Exception as e:
            print(f"[Error] pH sensor: {e}")
            ph = 0.0

            ph_sensor_status= "Malfunction"

        

        sensors_status= {"temperature sensor": temp_sensor_status, "light sensor": light_sensor_status, "flow rate sensor": flow_rate_status, "ph sensor": ph_sensor_status, "water level sensor": water_level_sensor_status, "TDS sensor": tds_sensor_status}
        

        # Print the results
        #print(f"Temperature: {temperature} °C")
        #print(f"Light Intensity: {light}")
        #print(f"pH Value: {ph}")
        #print(f"TDS Value: {tds} ppm")
        #print(f"Water Level: {water_level}")           #Print statements for testing and debugging
        #print(f"Flow Rate: {flow_rate}")
        #print("-" * 30)

        print("Data recorded")


        values = []

        values.append(temperature)
        values.append(light)
        values.append(ph)
        values.append(tds)                      #Returning processed values
        values.append(water_level)
        values.append(flow_rate)
        values.append(sensors_status)

        return values

            

    except KeyboardInterrupt:
        print("Exiting...")
        

if __name__ == "__main__":
    main()



##################################################################