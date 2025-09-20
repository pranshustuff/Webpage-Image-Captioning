# HTML Image Captioning Assistant

### Python + FastAPI project to process HTML lecture or engineering content:

- Image Captioning: Generates captions for all <img> tags using BLIP-2 and wraps them in `<figure>` + `<figcaption>`.

- Section Summaries: Uses LLaMA 3.1 via Hugging Face Inference API to summarize headings and surrounding text.

- Batch Processing: Supports multiple HTML files at once.

- Output: Enhanced HTML + structured JSON with images and section summaries.
