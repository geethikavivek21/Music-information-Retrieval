import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='XDVioDet Inference Options')

    # Mode and modality
    parser.add_argument('--mode', type=str, default='test', choices=['train', 'test'],
                        help='Mode: train or test')
    parser.add_argument('--modality', type=str, default='RGB', choices=['RGB', 'AUDIO'],
                        help='Input modality to use')

    # Data and model paths
    parser.add_argument('--test_list', type=str, required=True,
                        help='Path to the test .list file (one .npy path per line)')
    parser.add_argument('--feature_dir', type=str, required=True,
                        help='Directory containing extracted feature .npy files')
    parser.add_argument('--ckpt', type=str, required=True,
                        help='Path to the trained model checkpoint')
    parser.add_argument('--output_dir', type=str, default='output',
                        help='Directory to save output results')

    # GPU/CPU setup
    parser.add_argument('--gpus', type=str, default='-1',
                        help='GPU ID (use "-1" for CPU)')

    # Ground truth file for evaluation (needed for PR-AUC)
    parser.add_argument('--gt', type=str, required=False, default='ground_truth.npy',
                        help='Path to ground truth .npy file (for test PR-AUC)')

    # Optional model settings
    parser.add_argument('--input_dim', type=int, default=1024,
                        help='Input feature dimension')
    parser.add_argument('--hidden_dim', type=int, default=512,
                        help='Hidden layer dimension')

    return parser.parse_args()
