---
title: Brain Tumor Detection
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
---

# Brain Tumor Detection

Streamlit interface for an MRI image classification project.

## Model and dataset

The repository includes a compatible trained model at
`models/best_model.keras`. To reproduce training, install the requirements and
run `prepare_dataset.py` followed by `train_model.py`. The preparation script
downloads the CC0-licensed [BrainTumorMRI dataset](https://huggingface.co/datasets/Dharamanand/BrainTumorMRI).

This project is for research and education only and is not a medical diagnostic
tool.
