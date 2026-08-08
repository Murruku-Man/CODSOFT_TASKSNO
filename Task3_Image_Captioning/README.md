# CODSOFT Task 3 - Image Captioning

## Project Description

This project combines **computer vision** and **natural language processing** to generate a natural-language description of an image.

A pre-trained **BLIP (Bootstrapping Language-Image Pre-training)** vision-language transformer is used to understand the image and generate a caption.

The model used is:

`Salesforce/blip-image-captioning-base`

## Features

- Accepts a local image as input
- Uses a pre-trained vision-language model
- Generates a natural-language caption
- Supports common image formats such as JPG and PNG
- Simple command-line interface
- Uses a transformer-based architecture

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Pillow
- BLIP image-captioning model

## Project Structure

```text
Task3_Image_Captioning/
├── image_captioning.py
├── requirements.txt
└── README.md
```

## Installation

Create or activate a Python environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Place an image in the project folder, for example:

```text
sample.jpg
```

Then run:

```bash
python image_captioning.py sample.jpg
```

On the first run, the pre-trained model will be downloaded. An internet connection is required for the initial model download.

Example:

```text
============================================================
              IMAGE CAPTIONING AI
                 CODSOFT - TASK 3
============================================================
Image: sample.jpg
Generating caption...
Caption: a dog sitting on the grass
```

## How It Works

1. The program receives the path of an image.
2. Pillow opens the image and converts it to RGB.
3. The BLIP processor prepares the image for the model.
4. The pre-trained BLIP vision-language transformer analyzes the image.
5. The model generates a sequence of words describing the image.
6. The processor converts the generated tokens into readable text.
7. The caption is displayed in the terminal.

## AI Concepts Demonstrated

- Computer vision
- Natural language generation
- Transfer learning
- Pre-trained models
- Transformer architecture
- Vision-language modeling

## Learning Outcome

This project demonstrates how computer vision and natural language processing can be combined to automatically generate descriptive captions for images using a pre-trained transformer model.

## Internship Task

**Task 3: Image Captioning**

The CodSoft Artificial Intelligence internship task asks students to combine computer vision and natural language processing to build an image-captioning AI, using pre-trained image recognition models and an RNN or transformer-based model to generate captions.
