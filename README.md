# Spycrop

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Spycrop**! This web application, built with Flask and Python, utilizes computer vision to detect whether a person is wearing a mask. If the app detects the absence of a mask, it triggers an alert mechanism, such as sending an email or displaying a notification. This app was made during the covid era to help control the spread of the virus in confined campuses

## Features

- **Mask Detection**: Utilizes computer vision to identify whether the user is wearing a mask.
- **Alert Mechanism**: Sends an email or displays a notification if a mask is not detected.
- **Flask Web Application**: Built with Flask for the server-side logic.
- **Python Backend**: The backend is implemented in Python.
- **User-friendly Interface**: Provides a simple and intuitive web interface for users.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3 installed on your machine.
- Pipenv installed (for managing dependencies).

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/annuraggg/SpyCrop-Desktop-App
   ```

2. Navigate to the project directory:
   ```bash 
   cd Spycrop-Desktop-App
   ```

3. Install dependencies using Pipenv:
    ```bash
    pipenv install
    ```

4. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

5. Run the Flask App
    ```bash
    Run the Flask application:
    ```

## Usage
Open the app.
Grant necessary permissions for camera access.
Position yourself in front of the camera.
The app will detect whether you are wearing a mask.
If no mask is detected, the alert mechanism will be triggered.

## Alert Mechanism Configuration
To configure the alert mechanism (e.g., email notifications), follow these steps:

Open the app settings.
Navigate to the "Alerts" section.
Enter your email credentials or configure the notification settings.


