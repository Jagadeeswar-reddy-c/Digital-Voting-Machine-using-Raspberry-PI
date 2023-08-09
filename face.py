
from face_recognition import face_encodings,compare_faces
import os
import pandas as pd
from datetime import date,datetime
import RPi.GPIO as GPIO
import time
import cv2



# Define button callback function
def button_callback(channel):
    print("pressed button")
    global vote_count_1, vote_count_2, vote_count_3, vote
    if channel == button_pin_1:
        vote_count_1 += 1
        vote = 1
        GPIO.output(led_pin_1, GPIO.HIGH)
        print(vote)
    elif channel == button_pin_2:
        vote_count_2 += 1
        vote = 2
        GPIO.output(led_pin_2, GPIO.HIGH)
        print(vote)
    elif channel == button_pin_3:
        vote_count_3 += 1
        vote = 3
        GPIO.output(led_pin_3, GPIO.HIGH)
        print(vote)

    time.sleep(4)
    GPIO.output(led_pin_1, GPIO.LOW)
    GPIO.output(led_pin_2, GPIO.LOW)
    GPIO.output(led_pin_3, GPIO.LOW)
    return vote

def recognise(img1,img2):
    img_encoding1 = readImage(img1)
    img_encoding2 = readImage(img2)
    return compare_faces([img_encoding1],img_encoding2)

def readImage(image):
    img = cv2.imread(image)
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return face_encodings(rgb_img)[0]

lis = os.getcwd()
lst = lis+'/Images/'
temp = os.listdir(lst)
#print(temp)
filename = 'frame.jpg'

# Function to turn the buzzer on
def buzzer_on():
    GPIO.output(buzz_pin, GPIO.HIGH)

# Function to turn the buzzer off
def buzzer_off():
    GPIO.output(buzz_pin, GPIO.LOW)

#vid = cv2.VideoCapture(0)

#button = int(input("button to take pic:"))

lee = pd.read_csv("insert.csv")
dit = list(lee.keys())
dit_adhr = lee['Adhar'].tolist()
print(dit_adhr)
#adhr = input("enter your aadhar:")

today = str(date.today())
today_ap = str(datetime.today().strftime("%p"))
today = today+'-'+today_ap
filecsv = 'valid.csv'
filevot = 'voting.csv'
vot = ['party','count']

id = 'ID'
vt = ''

if os.path.exists(filecsv)==True or os.path.exists(filevot)==True:
    if os.path.exists(filecsv)==True:
        df = pd.read_csv(filecsv)
        eles = list(df.keys())
        lts = df[eles[-1]]
    else:
        lts = [0 for i in range(len(temp))]
    if os.path.exists(filevot)==True:
        df_vot = pd.read_csv(filevot)
    else:
        df_vot = {'party1':0,'party2':0,'party3':0}
        key = list(df_vot.keys())
        
else:
    df_vot = {'party1':0,'party2':0,'party3':0}
    key = list(df_vot.keys())
    lts = [0 for i in range(len(temp))]
kle = 0    

while(True):
    
    # Set up GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    button_pin_1 = 25
    button_pin_2 = 18
    button_pin_3 = 27
    led_pin_1 = 26
    led_pin_2 = 20
    led_pin_3 = 21
    buzz_pin = 4
    GPIO.setup(button_pin_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_pin_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_pin_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzz_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(led_pin_1, GPIO.OUT)
    GPIO.setup(led_pin_2, GPIO.OUT)
    GPIO.setup(led_pin_3, GPIO.OUT)

    vote_count_1 = 0
    vote_count_2 = 0
    vote_count_3 = 0
    vote = 0
    kle = 0
    
    
    
    adhr = input("enter your aadhar:")
    # lts = ["" for i in range(len(temp))]
    
    vid = cv2.VideoCapture(0)
    
    ret, frame = vid.read()
    cv2.imwrite(filename,frame)
    # print(dit_adhr)
    try:
        for _ in range(len(temp)):
            # print(recognise(lis+'/'+filename,lst+temp[_]))
            if int(adhr) == dit_adhr[_]:
                break
        # print(lst+temp[_])
        if _ in dit_adhr:
            if recognise(lis+'/'+filename,lst+temp[_]) == [True]:
                #print(lts[_])
                #print(lts[_] == 1)
                if lts[_] == 1:
                    print("voting fault")
                    buzzer_on() # Turn the buzzer on
                    time.sleep(6) # Wait for 1 second
                    buzzer_off() # Turn the buzzer off
                    time.sleep(1)
                else:
                    #print("pass")
                    lts[_] = 1
                    print("press button")
                    # Add event detection for each button
                    GPIO.add_event_detect(button_pin_1, GPIO.FALLING, callback=button_callback, bouncetime=200)
                    GPIO.add_event_detect(button_pin_2, GPIO.FALLING, callback=button_callback, bouncetime=200)
                    GPIO.add_event_detect(button_pin_3, GPIO.FALLING, callback=button_callback, bouncetime=200)


                    # Run voting system for a specified time period
                    voting_time = 40 # in seconds
                    start_time = time.time()
                    while time.time() - start_time < voting_time:
                        time.sleep(0.1)
                    #print("voted for ",vote," party")
                    op = df_vot['party'+str(vote)]
                    op += 1
                    df_vot['party'+str(vote)] = op
                    #print(df_vot)
                    vt = 1
                    #lts[_] = 0
            else:
                kle = 1
                
        else:
            kle = 1
            
    except:
        kle = 1
        #print("pelase make sure ur aadhar or photo")
    #df = {}
    if kle == 1:
#        else:
        print("please make sure ur aadhar or photo")
        buzzer_on() # Turn the buzzer on
        time.sleep(3) # Wait for 1 second
        buzzer_off() # Turn the buzzer off
        time.sleep(1)
        print('Alert')
    if os.path.exists(filecsv)==True:
        #df[id] = [_[:-4] for _ in temp]
        
        df[today] = lts
    else:
        #print(lts)
        Data = {id:[_[:-4] for _ in temp],today:lts}
        df = pd.DataFrame(Data)
        #print(df)
        #print(df_vot)
    if os.path.exists(filevot) != True:
        df_vot = pd.DataFrame([df_vot])
    print(df_vot)
    df.to_csv(filecsv,index = False)
    df_vot.to_csv(filevot,index = False)
    if vt == '1':
        print("please upload photo")
    # button = 0
    os.remove(lis+'/'+filename)
    
    vid.release()
    cv2.destroyAllWindows()
    

    # Clean up GPIO pins
    GPIO.cleanup()




