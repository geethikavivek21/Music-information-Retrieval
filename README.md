

---

## Step 1: Set Up Your Environment
Before running segmentation, ensure your *Anaconda environment* is set up.

1️ Activate Your Conda Environment  
```bash
conda activate speech_seg
```

If the environment doesn't exist, create it first:
```bash
conda create --name speech_seg python=3.8 -y
conda activate speech_seg
```

2️ Install Required Dependencies  
```bash
conda install -c conda-forge numpy scipy matplotlib ffmpeg requests -y
pip install torch tensorflow inaSpeechSegmenter
```

Verify installation:
```bash
pip show inaSpeechSegmenter
```

---

## Step 2: Navigate to Your Audio File Directory
Move to the directory where your *MP3 file* is stored:
```bash
cd /home/ssl/Downloads/
ls
```
Make sure you see your file path
here(Top Singer _ Musical Reality Show _ Flowers _ Ep# 09.mp3)

---
---

## Step 3: Segment the Audio Using inaSpeechSegmenter

```bash
ina_speech_segmenter.py -i "/home/ssl/Downloads/top_singer.mp3" -o ~/ina_output
```
here,
Inputs: the mp3 file.
Outputs: the segmentation results into ~/ina_output/.

If mp3 file doesn't work then convert it into wav. Since inaSpeechSegmenter works best with WAV files
```bash
ffmpeg -i "Top Singer _ Musical Reality Show _ Flowers _ Ep# 09.mp3" "top_singer.wav"
```
---

## Step 5: Verify the Segmentation Output
```bash
ls ~/ina_output/
```
If segmentation was successful, you should see a *CSV file* with timestamps and labels.

---

## Step 6: Open the CSV to Check Labels
Navigate to your project folder and check the formatted CSV:
```bash
cat ~/speech_seg_project/top_singer.csv
```

This will display the timestamps and segmented labels.

---

## Step 7: Import Labels into Sonic Visualiser
1️ Open Sonic Visualiser:
```bash
sonic-visualiser
```

2️ Load the mp3/wav File: (File > Open > select top_singer.mp3).
3️ Import Labels Automatically: (File > Import Annotation > select top_singer.csv > select correct data format-Label,Time,End Time >Tick-first row contains column heading > Time is specified-Explicitly in seconds > Plot type -Segmentation).
