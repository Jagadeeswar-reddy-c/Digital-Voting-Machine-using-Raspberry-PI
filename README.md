# Digital Voting System Using Raspberry Pi

## Overview:

This project is a digital voting system implemented on a Raspberry Pi. The system utilizes facial recognition to verify voter identity and ensures that each voter can only vote once. It includes real-time voting tally updates and alerts for any voting irregularities.

## Key Features:
  - Facial Recognition: Uses a facial recognition library to verify voter identity.
  - GPIO Integration: Utilizes GPIO pins on Raspberry Pi for button inputs and LED/Buzzer outputs.
  - Voting Process: Voters cast their vote by pressing buttons corresponding to different parties.
  - Real-Time Alerts: Buzzer alerts for invalid votes or double voting attempts.
  - Data Management: Maintains voter data and voting results in CSV files.

## Prerequisites
  - Raspberry Pi with Raspbian OS
  - Python 3.x
  - Required Python libraries:
    - face_recognition
    - opencv-python
    - pandas
    - RPi.GPIO

## Setup
  1. Install Required Libraries:
```
pip install face_recognition opencv-python pandas RPi.GPIO
```
  2. Prepare Images: Place the images of voters in the `Images` directory. The image filenames should be named according to the voter's Aadhar number.
  3. Initialize Data:
     - Run the provided script to initialize the voter data from the images.

## Usage
Installation and Cloning Project:
```
git clone https://github.com/Jagadeeswar-reddy-c/Digital-Voting-System-Using-Raspberry-Pi.git
cd Digital-Voting-System-Using-Raspberry-Pi
```

  1. Insert Voter Data:
     - Run `insert.py` to insert the voter data into the system.
  2. Initialize Facial Recognition and Run the Voting System:
     - Execute face.py to start the voting system. The script will prompt for the voter's Aadhar number, capture their image using the webcam, and verify their identity using facial recognition.
    
## Voting Process
  - If the voter's identity is verified and they have not voted yet, they will be prompted to press one of the buttons corresponding to different parties to cast their vote.
  - The system will register the vote and update the tally in real-time.
  - If the voter attempts to vote again, a buzzer will alert indicating a voting fault.

## Data Management
  - Voter Data: Stored in `insert.csv` containing Aadhar numbers and corresponding image filenames.
  - Voting Data: Maintained in `valid.csv` and `voting.csv` to track voter participation and voting results, respectively.

## Notes
  - Ensure the Aadhar numbers in the `insert.csv` file match the filenames of the images (excluding the file extension).
  - The system is designed to allow only one vote per Aadhar number. Any attempt to vote again will trigger an alert.

## Conclusion
The digital voting system developed using Raspberry Pi integrates facial recognition technology and GPIO for secure and efficient voting. This system prevents multiple voting attempts and ensures reliable vote counting. By leveraging image processing, real-time data management, and hardware interaction, the project showcases practical applications of these technologies. Users can set up and run this system following the provided steps, enhancing traditional voting processes with improved security and accuracy. This project exemplifies the potential of technology to address challenges in voting systems, providing a robust and scalable solution.
