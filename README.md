 👋 Hi, I’m @Anand3074
- 👀 I’m interested in Frontend development
- 🌱 I’m currently learning javascript
- 💞️ I’m looking to collaborate on web development
- 📫 How to reach me ...


FITSYNC: AI-TRAINER --> CVZone-Based Real-Time & Video Analysis for Workouts and Yoga Asanas

This project utilizes the powerful CVZone library to perform real-time video analysis of your workouts and yoga postures, helping you improve your form and track progress. It provides valuable insights into various parameters, including:

Intensity: Gauge the level of engagement of your muscles during exercises.
Workout Count: Automatically track the number of repetitions you perform for each exercise.
Form Accuracy: Receive real-time feedback on your form to ensure proper technique and minimize injury risk.
Requirements:

Python 3.x: Ensure you have Python 3.x installed on your system.
OpenCV: Install OpenCV using pip install opencv-python.
MediaPipe: Install MediaPipe using pip install mediapipe.
NumPy: NumPy is typically already installed with Python.
CVZone: Install CVZone using pip install cvzone.
Installation:

Clone this repository: git clone https://github.com/Anand3074/exercise_intensity_Fitsync.git
Navigate to the repository directory: cd exercise_intensity_Fitsync
Install the required packages: pip install -r requirements.txt
Usage:

Using a Video File:

Edit the video_path variable in the main.py file to point to your desired video file.
Run the script: python main.py
Using Your Camera:

Set the video_path variable to 0 (for the default camera).
Run the script: python main.py
Notes:

The script will display the analyzed video along with feedback on intensity, workout count, and form accuracy.
You can adjust various parameters in the angles function and other parts of the code to fine-tune the analysis for your specific needs.
Consider adding options for different exercises and yoga postures in future versions.
Additional Tips:

Ensure proper lighting and camera placement for optimal video analysis accuracy.
Experiment with different exercises and yoga postures to test the capabilities of the project.
Feel free to contribute to the project by suggesting improvements or adding new features.
Explanation of the Code:

Imports: The script imports necessary libraries like OpenCV, MediaPipe, NumPy, and CVZone.
Function Definition: The angles function calculates angles from specific body landmarks to assess form accuracy.
Main Loop: The while loop reads frames from the video or camera, processes them using CVZone, and displays the results.
Key Points:

The project leverages CVZone's pose estimation capabilities for effective body tracking.
Real-time feedback and insights help users improve their workouts and yoga practice.
The code is well-structured and commented for easy understanding and modification.



