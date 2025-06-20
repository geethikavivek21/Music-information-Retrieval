import torch
import numpy as np
from torch.utils.data import DataLoader
from model import Model
from dataset import ViolenceDataset
from test import test
import option
import time

if __name__ == '__main__':
    from option import parse_args
args = parse_args()


    # ✅ Debug argument parsing
    print(f"DEBUG: args -> {args}")  

    # ✅ Set default values if missing
    if not hasattr(args, "input_dim"):
        args.input_dim = 128  
    if not hasattr(args, "hidden_dim"):
        args.hidden_dim = 32  

    device = torch.device("cpu")  

    test_loader = DataLoader(CustomDataset("/home/ssl/XDVioDet/list/", test_mode=True),
                         batch_size=1, shuffle=False, num_workers=0, pin_memory=False)  # ✅ Lower batch size


    model = Model(args)
    model = model.to(device)

    checkpoint = torch.load("ckpt/wsanodet_mix2.pkl", map_location=torch.device("cpu"))
    model_dict = model.state_dict()
    filtered_checkpoint = {k: v for k, v in checkpoint.items() if k in model_dict and model_dict[k].shape == v.shape}
    model.load_state_dict(filtered_checkpoint, strict=False)

    gt = np.load("/home/ssl/XDVioDet/list/gt.npy")

    for input_tensor in test_loader:
        print(f"DEBUG: Input shape -> {input_tensor.shape}")
for input_tensor in test_loader:
        print(f"DEBUG: Input shape -> {input_tensor.shape}")
        if input_tensor.shape[1] == 0:
            raise ValueError("Error: Input tensor has zero-sized features.")
        break

    start_time = time.time()
    pr_auc, pr_auc_online = test(test_loader, model, device, gt)

    print(f"Inference Time: {time.time() - start_time:.2f} seconds")
    print(f"Offline PR-AUC: {pr_auc:.4f}, Online PR-AUC: {pr_auc_online:.4f}")
