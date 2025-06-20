# 🧠 XDVioDet - Violence Detection (Inference Only)

This repository enables **inference** for a pretrained violence detection model using graph-based neural networks on pre-extracted video features.

---

## ✅ Features

- CPU-friendly PyTorch inference  
- Uses `.npy` feature segments (e.g., I3D features)  
- Graph Convolutional Network with learned adjacency  
- Pretrained checkpoint loading with flexible shape matching  
- Outputs Offline and Online PR-AUC  

---

## 📁 Folder Structure

.
├── main.py # Inference runner
├── model.py # GCN model definition
├── dataset.py # Feature dataset loader
├── test.py # PR-AUC evaluation logic
├── option.py # Command-line arguments
├── layers.py # GraphConvolution & SimilarityAdj
├── ckpt/ # Pretrained checkpoint (.pkl)
├── list/ # .list and .npy files for test
│ ├── rgb_test.list
│ ├── gt.npy
├── i3d_features_test/ # Folder containing .npy feature files



---

## 📦 Setup Instructions

### 1. ✅ Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install torch numpy scikit-learn

    🔁 Ensure these versions to avoid compatibility issues:

        numpy==1.26.4

        scikit-learn>=1.2.0

2. ✅ Git LFS for Checkpoints

If your .pkl model was stored using Git LFS:

sudo apt install git-lfs
git lfs install
git clone https://github.com/<your-repo> .
git lfs pull

🧪 Run Inference

Make sure your .npy features and list files are ready.
✅ Example Command:

python main.py \
  --test_list list/rgb_test.list \
  --feature_dir i3d_features_test/ \
  --ckpt ckpt/wsanodet_mix2.pkl \
  --gt list/gt.npy \
  --modality RGB \
  --gpus -1 \
  --input_dim 128 \
  --hidden_dim 32 \
  --num_classes 1

DEBUG: Parsed arguments -> Namespace(...)
DEBUG: Input shape -> torch.Size([1, 5, 128])
✅ Inference completed in 1.23 seconds
📈 Offline PR-AUC: 0.8123, Online PR-AUC: 0.7985

🧱 Model Architecture

    Input: (batch_size, num_segments, 128)

    GraphConv1: 128 → 32 (residual)

    GraphConv2: 32 → 32 (residual)

    Mean Pooling over time

    Output Layer: 32 → num_classes (e.g., 1)

Adjacency matrix is dynamically learned using SimilarityAdj.

📁 File Descriptions
File	Description
main.py	Runs inference using pretrained model
model.py	Defines GCN-based violence detection model
layers.py	Contains GCN and adjacency layer classes
dataset.py	Loads .npy features for inference
test.py	Computes PR-AUC (offline & online)
option.py	Argument parser with CLI support


