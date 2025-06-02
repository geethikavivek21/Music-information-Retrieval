import os
import argparse
from pathlib import Path
from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

# 1. Parse CLI arguments
parser = argparse.ArgumentParser(description='INA Speech Segmenter CLI-style Python script.')
parser.add_argument('-i', '--input', required=True, help='Path to input media file')
parser.add_argument('-o', '--output', required=True, help='Output directory for segmentation results')
args = parser.parse_args()

# 2. Expand and prepare paths
input_path = Path(args.input).expanduser().resolve()
output_dir = Path(args.output).expanduser().resolve()
output_dir.mkdir(parents=True, exist_ok=True)

# 3. Run segmentation
print(f"Segmenting: {input_path}")
seg = Segmenter()
segmentation = seg(str(input_path))

# 4. Generate output filenames
base_name = input_path.stem  # e.g., 'top_singer' from 'top_singer.wav'
csv_path = output_dir / f"{base_name}.csv"
textgrid_path = output_dir / f"{base_name}.TextGrid"

# 5. Export results
seg2csv(segmentation, str(csv_path))
seg2textgrid(segmentation, str(textgrid_path))

print(f"Saved segmentation to:\n- {csv_path}\n- {textgrid_path}")
