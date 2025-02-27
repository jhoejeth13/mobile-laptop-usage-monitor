# 📷 Classroom Laptop/Mobile Phone Usage Monitor  

This project detects whether students are using **mobile phones or laptops** during class by analyzing hand gestures via **OpenCV + MediaPipe**.  

🔹 **Detects** if a student is holding a phone or laptop.  
🔹 **Helps professors** monitor classroom distractions.  
🔹 **Can be used in exams** to enforce no-phone policies.  

---

## **📌 Features**
✔️ Real-time **hand tracking** using OpenCV & MediaPipe  
✔️ **Detects** phone/laptop usage based on hand gestures  
✔️ **Works with any webcam** (laptop, external camera)  
✔️ Runs on **Windows, Mac, Linux** (requires Python)  

---

## **🚀 Installation & Setup**
### **1️⃣ Install Anaconda (Recommended)**
Download & install Anaconda from:  
🔗 [https://www.anaconda.com/download](https://www.anaconda.com/download)

### **2️⃣ Create a New Environment**
Open **Anaconda Prompt** and create an environment:  
```sh
conda create --name monitor-env python=3.8
```
### **3️⃣ Install Dependencies
Run the following commands inside Anaconda Prompt:
```sh
conda install -c conda-forge opencv
pip install mediapipe
```

---

# 🎬 How to Run
### **1️⃣ Ensure your webcam is connected (laptop cam or external USB camera).
### **2️⃣ Open Anaconda Prompt and navigate to the project folder:
```sh
cd path/to/your/detection
```
### **3️⃣ Run the script:
```sh
python monitor.py
```

---

# 4️⃣ Press 'q' to exit the program.

---

# 📷 How It Works
The webcam detects hands and analyzes finger positions.

If the thumb, index, and middle fingers are close together, it assumes a phone/laptop is in hand.

A warning message "PHONE/LAPTOP DETECTED!" appears on-screen.

🛠 Troubleshooting
❓ No webcam detected?
🔹 Check if another app (Zoom, Teams, etc.) is using your webcam.
🔹 Try restarting your computer.

❓ Detection not accurate?
🔹 Ensure good lighting for better hand tracking.
🔹 Adjust the detection threshold in monitor.py.

📌 Future Improvements
✅ Capture a screenshot when a phone is detected
✅ Log detections with timestamps
✅ Send a notification to the teacher

👨‍💻 Author
Developed by Good Bitches 🚀
