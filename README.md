# Brain Tumor Detection

Streamlit interface for an MRI image classification project.

## Deploy on Streamlit Community Cloud

1. Import `pooja271211/brain-tumour-detection` from GitHub.
2. Set the app file to `app.py` and the Python version to **3.11** in the
   deployment settings.
3. Deploy. Dependencies are pinned in `requirements.txt`, and the trained
   model is included at `models/best_model.keras`.

On the **History** page, use **Download prediction history (CSV)** to export
scan timestamps, predictions, confidence scores, class probabilities, and any
manually corrected labels.

## Model and dataset

The repository includes a compatible trained model at
`models/best_model.keras`. To reproduce training, install the requirements and
run `prepare_dataset.py` followed by `train_model.py`. The preparation script
downloads the CC0-licensed [BrainTumorMRI dataset](https://huggingface.co/datasets/Dharamanand/BrainTumorMRI).
The current model achieved 93.93% accuracy on the dataset's held-out test split
(1,054 images); see `models/eval_results.json` for per-class metrics.
The training script uses early stopping and caps fine-tuning at three epochs to
keep CPU training time manageable. These dataset metrics do not establish
clinical validity; the app is for research use only.

This project is for research and education only and is not a medical diagnostic
tool.
