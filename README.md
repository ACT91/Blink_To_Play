🎵 Blink Music Controller

**Blink Music Controller** is a hands-free, eye-blink-based controller for your media player.  
It lets you use **facial gestures** (left eye, right eye, or both blinks) to simulate media keys like play/pause, next/previous track, and even seeking — just by blinking.

Perfect for:
- 🔁 Accessibility applications
- 🧠 Experimental human-computer interaction
- 🎧 Listening to music without touching your device

---

## 👁️ Blink Gesture Controls

| Blink Action              | Simulated Keys     | Media Action           |
|---------------------------|--------------------|-------------------------|
| Blink both eyes           | `Ctrl + P`         | Play / Pause           |
| Blink right eye           | `Ctrl + F`         | Next track             |
| Blink left eye            | `Ctrl + B`         | Previous track         |
| Long blink (right eye)    | `Ctrl + →`         | Seek forward           |
| Long blink (left eye)     | `Ctrl + ←`         | Seek backward          |

> ✅ Works with any media player that supports these shortcuts  
> Examples: Windows Media Player, VLC, Groove Music

---

## 🧠 How It Works

- Uses **OpenCV** to access your webcam
- Tracks face + eye movement with **MediaPipe FaceMesh**
- Detects **left/right/both eye blinks**, and **long blinks**
- Simulates keyboard shortcuts using **pynput**

---

## 🗂️ Project Structure

blink_music_controller/
├── main.py # Main loop: webcam + action triggers
├── eye_tracker.py # Detects left, right, both eye blinks
├── media_keys.py # Simulates media key presses (Ctrl + P, etc.)
├── utils.py # Tracks blink duration for long blinks
├── requirements.txt # Dependencies



---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10 or 3.11
- Webcam

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
▶️ Run the Tool
bash
Copy
Edit
python main.py
Make sure your media player window is active
(e.g., click on the WMP or VLC window)

📋 Requirements
opencv-python

mediapipe

pynput

Already included in requirements.txt

📸 Screenshots
screenshots coming soon

🛠️ Features to Improve
GUI showing current song, eye status, blink type

Sound or popup feedback after an action

Blink customization (e.g., adjust threshold/delay)

Voice fallback or confirmation mode

🧾 License
MIT License — use, share, and improve!

🙌 Author
ACT91
Built with Python, creativity, and a blink of genius 😉
