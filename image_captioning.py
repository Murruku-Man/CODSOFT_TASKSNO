# CODSOFT Task 3 - Image Captioning
# Uses a pre-trained BLIP vision-language transformer to generate captions.

import argparse
from pathlib import Path

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


MODEL_NAME = "Salesforce/blip-image-captioning-base"


def generate_caption(image_path):
    """Load an image and generate a natural-language caption."""
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path).convert("RGB")

    processor = BlipProcessor.from_pretrained(MODEL_NAME)
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)

    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=30)

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption


def main():
    parser = argparse.ArgumentParser(
        description="Generate a caption for an image using a pre-trained AI model."
    )
    parser.add_argument(
        "image",
        help="Path to the image file, e.g. sample.jpg"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("              IMAGE CAPTIONING AI")
    print("                 CODSOFT - TASK 3")
    print("=" * 60)
    print(f"Image: {args.image}")
    print("Generating caption...")

    try:
        caption = generate_caption(args.image)
        print(f"Caption: {caption}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
