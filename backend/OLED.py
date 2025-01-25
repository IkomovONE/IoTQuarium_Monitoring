import time
import board
import busio
import sensors
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create an SSD1306 OLED object (128x32 resolution example)
oled = SSD1306_I2C(128, 32, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Load a font (you can use default or custom fonts)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)

def display_temperature(temp):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"T: {temp}°C"
    draw.text((10, 10), text, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()


def display_light_status(light):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"Light: {light}"
    draw.text((10, 10), text, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()


def display_ph(pH):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"pH: {pH}"
    draw.text((10, 10), text, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()


def display_tds(tds):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"S: {tds}ppm"
    draw.text((10, 10), text, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()


def display_water_flow(flow):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"F: {flow}"

    fontt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 17)

    draw.text((10, 10), text, font=fontt, fill=255)

    # Display image
    oled.image(image)
    oled.show()


def display_level(level):
    """Display temperature on the OLED screen."""
    # Create a blank image for drawing
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a black rectangle to clear the screen
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Display the temperature
    text = f"W: {level}"
    draw.text((10, 10), text, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()





# Example: Update temperature every second
try:

    time.sleep(1)

    attempt= 0

    while True:

        try:

            attempt+= 1

            if attempt== 10:
                 
                 break
             


        

            sensor_data_list= sensors.main()

            temperature = sensor_data_list[0]
            ph = sensor_data_list[2]
            tds = sensor_data_list[3]
            light = sensor_data_list[1]
            w_level = sensor_data_list[4]
            w_flow = sensor_data_list[5]

            display_temperature(temperature)
            time.sleep(5)
            display_light_status(light)
            time.sleep(5)
            display_ph(ph)
            time.sleep(5)
            display_tds(tds)
            time.sleep(5)
            display_water_flow(w_flow)
            time.sleep(5)
            display_level(w_level)
            time.sleep(5)

            time.sleep(10)

            attempt=0

            continue

        except Exception as e:
            print("Failed to access sensors.")
            print(f"GPIO is busy.")
            time.sleep(10)

            continue



except Exception as e:
            print("Failed to access sensors.")
            print(f"GPIO is busy.")
            time.sleep(10)