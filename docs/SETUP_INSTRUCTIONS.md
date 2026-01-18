# 🧪 Research Setup Guide

This guide will help you set up the environment and run experiments for Deep Delta Learning (DDL).

## 🛠️ 1. Environment Setup

We recommend using **Python 3.10+**.

### Clone and Install
```bash
git clone https://github.com/vukrosic/deep-delta-learning
cd deep-delta-learning
pip install -r requirements.txt
```

## 📊 2. Preparing Data

DDL research uses the Blueberry 1B pretraining dataset.

### Download Research Subset (40M Tokens)
```bash
python3 -c "
from datasets import load_dataset
import os
print('Downloading research subset...')
ds = load_dataset('vukrosic/blueberry-1B-pretrain', split='train[:20000]')
os.makedirs('processed_data/research_40M', exist_ok=True)
ds.save_to_disk('processed_data/research_40M')
print('✅ Data Ready!')
"
```

## 🚀 3. Running Experiments

### Base Training
To run a standard pretraining run with Deep Delta Learning:
```bash
python train_llm.py
```

### Customizing Experiments
Modify `configs/llm_config.py` to adjust:
- `beta_dim`: Dimension for the delta update mechanism.
- `sigmoid_scale`: Scaling factor for the value projection.
- `k_eps`: Epsilon for normalization.

## 📈 4. Evaluating Results

After training, evaluate the model on standard benchmarks:
```bash
python benchmarks/compare_models.py
```

## 📋 Research Methodology

1. **Isolate Variables**: Change only one hyperparameter or architectural detail at a time.
2. **Log Baselines**: Always compare against the current main branch performance.
3. **Analyze Loss Curves**: Use `utils/plot_loss.py` to visualize the training dynamics.
