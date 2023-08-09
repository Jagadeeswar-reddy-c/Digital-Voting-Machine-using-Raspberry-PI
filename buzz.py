import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Define the GPIO pin number for the buzzer
BUZZER_PIN = 4

# Set the buzzer pin as an output pin
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Function to turn the buzzer on
def buzzer_on():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

# Function to turn the buzzer off
def buzzer_off():
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Main loop
while True:
    print(1)
    buzzer_on() # Turn the buzzer on
    time.sleep(10) # Wait for 1 second
    buzzer_off() # Turn the buzzer off
    time.sleep(1) 
    break# Wait for 1 second
