# 🖐️ Gesture Controller (Roboflow + OpenCV)

Control your computer using hand gestures via webcam.

This project uses a custom-trained model from Roboflow to detect hand gestures and trigger keyboard actions in real time.

---

## 🚀 Features

- ✋ Palm → Play / Pause
- ✊ Fist → Toggle / Stop
- 🎥 Real-time webcam detection
- 🧠 Gesture smoothing (no flickering)
- ⚡ Cooldown system (no spam inputs)

---

## 🛠 Tech Stack

- Python
- OpenCV
- Roboflow Inference API
- PyAutoGUI

---

## 📂 Project Structure
```
gesture-controller/
│
├── src/
│ ├── main.py # Entry point
│ ├── detector.py # Roboflow inference
│ ├── controls.py # Keyboard actions
│ ├── config.py # Config + API key
│
├── utils/
│ ├── cooldown.py # Prevents repeated triggers
│
├── dataset/ # (optional, not required to run)
├── requirements.txt
├── README.md
└── .env # API key (not committed)
```

## ⚙️ Setup

### 1. Clone the repo


git clone https://github.com/YOUR_USERNAME/gesture-controller.git

cd gesture-controller


---

### 2. Create virtual environment


python3 -m venv venv
source venv/bin/activate


---

### 3. Install dependencies


pip install -r requirements.txt


---

### 4. Add your Roboflow API key

Create a `.env` file:


ROBOFLOW_API_KEY=your_api_key_here


---

### 5. Run the project

python src/main.py

---

## 🎯 How it Works

1. Webcam captures frames
2. Frames are sent to Roboflow model
3. Model detects gesture (palm / fist)
4. Gesture is stabilized using buffer
5. Action is triggered using PyAutoGUI

---

## ⚠️ Notes

- Make sure your browser/video is focused
- Works best in good lighting conditions
- Requires webcam access

---

## 💡 Future Improvements

- Add more gestures (volume, next/prev)
- Switch to local model (reduce latency)
- Add UI overlay with detection feedback
- Build desktop app version

---

## 📸 Demo (optional)

_Add a GIF or screenshot here_

---

## 📄 License

MIT License