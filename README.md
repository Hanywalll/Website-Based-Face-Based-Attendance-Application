# Face Recognition Attendance System

## Overview
Face detection, as a research field in image processing, has attracted many scientists due to its ability to identify individuals through facial images. Although related applications already exist, this technology continues to evolve and requires further research to achieve optimal results. This project aims to develop an application capable of detecting and recognizing faces in real-time with high accuracy.

## Technologies Used
- **Face Detection**: Viola-Jones method
- **Face Recognition**: Eigenface method based on PCA (Principal Component Analysis)
- **Image Processing Library**: OpenCV
- **Programming Language**: Python

## Features
- Real-time face detection and recognition
- Handles variations in age, facial expressions, and accessories (e.g., glasses)
- Works efficiently under different lighting conditions and distances
- Faster recognition time compared to fingerprint-based attendance systems

## Performance
- The average face recognition time is **2.17 seconds**, compared to **3.24 seconds** for fingerprint recognition, making it **1.07 seconds faster**.
- The system can recognize users in various positions and lighting conditions with high accuracy.

## Applications
This face recognition-based attendance system is particularly useful in schools, allowing teachers to mark their presence efficiently. The high accuracy and adaptability to different angles and accessories make it a modern and effective solution for attendance management.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for discussion.

