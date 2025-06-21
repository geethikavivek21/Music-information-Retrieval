
### Step 1: install Whisper with pip

```bash
pip install git+https://github.com/openai/whisper.git
```

---

### 🔧 Step 2: install `ffmpeg` (required for audio processing)

```bash
sudo apt install ffmpeg
```

---

### Step 3: Created and activated a Conda environment



```bash
conda create -n whisper_env python=3.9 -y
conda activate whisper_env
```

---

### 📂 Step 4: Run  Whisper from your Downloads directory

You navigated to the folder:

```bash
cd ~/Downloads
```

And run the transcription command:

```bash
whisper "yodha padakali tamil.mp3" --language ta --model medium --fp16 False
```
for malayalam 

```bash
whisper "your_malayalam_audio.mp3" --language ml --model medium --fp16 False

```


