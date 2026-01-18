from datasets import load_dataset
import os

# Option A: 40M Tokens (Fast, for Research)
print("Downloading 40M Token Research Data (Streaming mode)...")
ds_iterable = load_dataset("vukrosic/blueberry-1B-pretrain", split="train", streaming=True)
# Materialize only the first 25,000 samples
from datasets import Dataset
ds = Dataset.from_list(list(ds_iterable.take(25000)))

os.makedirs("processed_data/research_40M", exist_ok=True)
ds.save_to_disk("processed_data/research_40M")

# Option B: 1B Tokens (Full Pretraining)
# print("Downloading 1B Pretraining Data...")
# ds = load_dataset("vukrosic/blueberry-1B-pretrain")
# os.makedirs("processed_data/pretrain_1B", exist_ok=True)
# ds.save_to_disk("processed_data/pretrain_1B")

print("✅ Data Ready!")

