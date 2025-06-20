Based on your **previous conversation**, here's exactly how you installed and used **Whisper** to transcribe Tamil audio on your Linux system:

---

## ✅ Whisper Setup from Previous Conversation

### Step 1: You installed Whisper with pip

```bash
pip install git+https://github.com/openai/whisper.git
```

---

### 🔧 Step 2: You installed `ffmpeg` (required for audio processing)

```bash
sudo apt install ffmpeg
```

---

### Step 3: You created and activated a Conda environment

You attempted this but had some environment issues:

```bash
conda create -n whisper_env python=3.9 -y
conda activate whisper_env
```

> At some point, you were inside `(whisper_env)` — although later the environment seemed broken.

---

### 📂 Step 4: You ran Whisper from your Downloads directory

You navigated to the folder:

```bash
cd ~/Downloads
```

And ran the transcription command:

```bash
whisper "yodha padakali tamil.mp3" --language ta --model medium --fp16 False
```
for malayalam 

```bash
whisper "your_malayalam_audio.mp3" --language ml --model medium --fp16 False

```


