# Food Browning Level Analysis

This project explores how image processing can be used to estimate the browning level of baked food products from photographs.

## Current progress

The first Python script loads a food photograph, prints its dimensions, and displays it. Browning detection and classification have **not** been implemented yet.

## Project structure

- `src/load_image.py` — opens and previews a photo
- `data/samples/` — location for local test images (not uploaded)
- `requirements.txt` — Python libraries

## Try it

1. Install Python 3.10 or newer.
2. Run `pip install -r requirements.txt`.
3. Add your own image as `data/samples/food.jpg`.
4. Run `python src/load_image.py`.

## Next step

Explore image preprocessing and color information before attempting to identify browned regions.
