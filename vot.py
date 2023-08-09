import RPi.GPIO as GPIO
import time
#import LCD1602 as LCD

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
button_pin_1 = 17
button_pin_2 = 18
button_pin_3 = 27
led_pin_1 = 22
led_pin_2 = 23
led_pin_3 = 24
GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(led_pin_2, GPIO.OUT)
GPIO.setup(led_pin_3, GPIO.OUT)

# Initialize vote counters
vote_count_1 = 0
vote_count_2 = 0
vote_count_3 = 0

# Set up LCD display
#LCD.init_lcd()

# Define button callback function
def button_callback(channel):
    global vote_count_1, vote_count_2, vote_count_3
    if channel == button_pin_1:
        vote_count_1 += 1
        GPIO.output(led_pin_1, GPIO.HIGH)
    elif channel == button_pin_2:
        vote_count_2 += 1
        GPIO.output(led_pin_2, GPIO.HIGH)
    elif channel == button_pin_3:
        vote_count_3 += 1
        GPIO.output(led_pin_3, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led_pin_1, GPIO.LOW)
    GPIO.output(led_pin_2, GPIO.LOW)
    GPIO.output(led_pin_3, GPIO.LOW)
    # Update LCD display
    LCD.clear_lcd()
    LCD.write_lcd(0, 0, "Option 1: {}".format(vote_count_1))
    LCD.write_lcd(0, 1, "Option 2: {}".format(vote_count_2))
    LCD.write_lcd(0, 2, "Option 3: {}".format(vote_count_3))

# Add event detection for each button
GPIO.add_event_detect(button_pin_1, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button_pin_2, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button_pin_3, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Run voting system for a specified time period
voting_time = 60 # in seconds
start_time = time.time()
while time.time() - start_time < voting_time:
    time.sleep(0.1)

# Print vote counts
print("Vote count for option 1: ", vote_count_1)
print("Vote count for option 2: ", vote_count_2)
print("Vote count for option 3: ", vote_count_3)

# Clean up GPIO pins
GPIO.cleanup()
