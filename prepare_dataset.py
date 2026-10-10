"""Download and extract the CC0 brain MRI dataset into train/test folders."""

import os
from urllib.request import urlretrieve

import pandas as pd
from PIL import Image
from io import BytesIO

DATASET_URL = "https://huggingface.co/datasets/Dharamanand/BrainTumorMRI/resolve/main/data"
SOURCE_DIR = "dataset-source"
OUTPUT_DIR = "dataset"
LABELS = {
    0: "glioma",
    1: "meningioma",
    2: "notumor",
    3: "pituitary",
}
SPLITS = ("train", "test")


def main():
    os.makedirs(SOURCE_DIR, exist_ok=True)

    for split in SPLITS:
        parquet_name = f"{split}-00000-of-00001.parquet"
        parquet_path = os.path.join(SOURCE_DIR, parquet_name)
        if not os.path.exists(parquet_path):
            urlretrieve(f"{DATASET_URL}/{parquet_name}", parquet_path)

        data = pd.read_parquet(parquet_path)
        for row_index, row in data.iterrows():
            label = LABELS.get(int(row["label"]))
            if label is None:
                raise ValueError(f"Unexpected label {row['label']!r} in {parquet_name}")

            image_data = row["image"]
            image_bytes = image_data.get("bytes") if isinstance(image_data, dict) else None
            if not image_bytes:
                raise ValueError(f"Missing image bytes at row {row_index} in {parquet_name}")

            output_dir = os.path.join(OUTPUT_DIR, split, label)
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{split}_{row_index:05d}.jpg")
            with Image.open(BytesIO(image_bytes)) as image:
                image.convert("RGB").save(output_path, format="JPEG")

        print(f"Prepared {len(data)} images for {split}.")


if __name__ == "__main__":
    main()
