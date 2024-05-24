# AI-Based Fire Detection System

This project implements an AI-based fire detection system using Python. It utilizes computer vision techniques to detect fire in real-time video streams and sends email alerts in case of fire detection.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The AI-Based Fire Detection System is designed to detect fire using a webcam or any video input source. It employs a cascade classifier for fire detection and runs the detection algorithm on video frames captured by the camera. When fire is detected, the system triggers an alarm sound and sends an email alert to the specified recipient.

## Features

- Real-time fire detection using computer vision.
- Email alert notification with customizable message and attachment.
- User-friendly GUI built with Tkinter.
- Adjustable parameters for cascade classifier tuning.
- Alarm sound played upon fire detection.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/fire-detection-system.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have Python installed on your system.

## Usage

1. Run the `fire_detection_system.py` script:

    ```bash
    python fire_detection_system.py
    ```

2. Enter your email credentials and recipient email address in the GUI.
3. Click on the "Save Email" button to save the email credentials.
4. Start the fire detection system by clicking on the "Start Fire Detection" button.
5. The system will continuously monitor the video feed for fire detection.
6. If fire is detected, an alarm sound will be triggered, and an email alert will be sent.

## Libraries Used

The following libraries were used in this project:

- `threading`: For running tasks concurrently.
- `smtplib`: For sending email alerts.
- `tkinter`: For creating the graphical user interface.
- `pygame`: For playing alarm sounds.
- `opencv-python`: For computer vision tasks such as image processing and object detection.
- `Pillow`: For image processing tasks.
- `requests`: For making HTTP requests.
- `folium`: For visualizing geographical data.
- `ssl`: For SSL certificate handling.
- `json`: For reading and writing JSON files.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
