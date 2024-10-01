# Jasper - Face Recognition and Voice-Controlled Robot

Jasper is a robot that combines face recognition using OpenCV and voice commands using GPIO control for movement. The project utilizes Haarcascades for face recognition and is capable of executing basic movement commands like moving forward, backward, left, and right through voice input.

## Key Features
- **Face Recognition**: Uses the Haarcascade algorithm for recognizing faces.
- **Voice Control**: Controls movement of the robot (forward, backward, left, right) based on voice commands.
- **Edge Deployment**: Deployed on a Raspberry Pi integrated with a camera module for face recognition.

## Technologies Used
- **OpenCV**: For image processing and face recognition.
- **RPi.GPIO**: For controlling the movement of the robot via GPIO pins on the Raspberry Pi.
- **Python**: Used for scripting the entire logic.
- **Speech Recognition**: For handling voice commands.

## Prerequisites
- Raspberry Pi with a camera module
- OpenCV installed on the Raspberry Pi
- Python 3 installed
- RPi.GPIO library installed

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/jasper-robot.git
    ```
2. Install OpenCV on your Raspberry Pi:
    ```bash
    sudo apt-get install python3-opencv
    ```
3. Install RPi.GPIO for controlling GPIO pins:
    ```bash
    sudo apt-get install python3-rpi.gpio
    ```

## Face Recognition
1. To train the model, run:
    ```bash
    python3 train.py [Your Name]
    ```
    This will capture images and store them in the `att_faces` directory.

2. To start face recognition, run:
    ```bash
    python3 facerec.py
    ```

## Voice Commands for Movement
1. **Move Forward**:
    ```bash
    python3 vfront.py
    ```

2. **Move Backward**:
    ```bash
    python3 vback.py
    ```

3. **Move Left**:
    ```bash
    python3 vleft.py
    ```


## GPIO Pin Layout for Movement Control
- Motor 1A: Pin 16
- Motor 1B: Pin 18
- Motor 1E: Pin 22
- Motor 2A: Pin 23
- Motor 2B: Pin 21
- Motor 2E: Pin 19

## How to Run
1. **Train the Face Recognition Model**: First, use the `train.py` script to capture face images.
2. **Recognize Faces**: Run `facerec.py` to start the camera stream for face recognition.
3. **Control the Robot**: Use the respective Python scripts for moving the robot using voice commands.

## Notes
- Make sure to wire the motors correctly to the GPIO pins for proper control.
- Ensure your Raspberry Pi camera is working and configured correctly.

## License
This project is licensed under the MIT License.
