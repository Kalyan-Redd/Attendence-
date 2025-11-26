# Attendance-monitoring-system-using-OpenCV

A real-time Attendance Monitoring System that leverages computer vision for face recognition, allowing automated attendance logging and management. The system integrates with a MySQL database to store user and attendance details and provides a Streamlit-based dashboard for visualizing attendance records for the current day.

# Features
=> Face Detection & Recognition
Utilizes the Haar Cascade classifier for detecting faces and a K-Nearest Neighbors (KNN) classifier for recognition.
=> Automated Attendance Logging
Marks attendance only when a face is clearly detected and recognized, displaying the person's name on the frame in real time.
=> Streamlit Dashboard
Displays attendance records for the current day, refreshing automatically every 2 seconds.
=> Data Persistence
Stores user details and attendance logs securely in a MySQL database.
=> Daily Reset
Automatically clears the dashboard display for the next day while keeping records in the database.

# Technologies Used
=> Python
=> OpenCV for computer vision and face recognition
=> NumPy for data manipulation
=> MySQL Connector for database interaction
=> Streamlit
=> For creating the interactive web app
=> MySQL
=> For managing user and attendance records



# PROJECT STRUCTURE

attendance-monitoring-system/  
│  
├── data/  
│   ├── haarcascade_frontalface_default.xml  
│  
├── face2.py       # Face registration script  
├── test2.py       # Real-time face detection and recognition  
├── app1.py        # Streamlit dashboard  
├── attendance_db.sql  # Database schema  
├── requirements.txt   # Required Python packages  
└── README.md  
