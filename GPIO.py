import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin you want to control (change this to your desired pin number)
gpio_pin = 17

# Set the GPIO pin as an output
GPIO.setup(gpio_pin, GPIO.OUT)

try:
    while True:
        # Turn the GPIO pin on (HIGH)
        GPIO.output(gpio_pin, GPIO.HIGH)
        print("GPIO pin {} is ON".format(gpio_pin))
        
        # Pause for 1 second
        time.sleep(1)
        
        # Turn the GPIO pin off (LOW)
        GPIO.output(gpio_pin, GPIO.LOW)
        print("GPIO pin {} is OFF".format(gpio_pin))
        
        # Pause for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    GPIO.cleanup()

# Clean up GPIO on program exit
GPIO.cleanup()
