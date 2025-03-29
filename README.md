# agentic-OD

**Agentic-OD** is a repository designed for the automatic creation of bounding boxes in datasets using the [Moondream model](https://huggingface.co/vikhyatk/moondream2) from Hugging Face. This project leverages Moondream's capabilities to streamline the process of annotating datasets, enabling efficient object detection tasks.

---

## Tutorial

1. Upload the `agentic-OD` file to Google Colab.
2. Create a folder named `dataset` and add all the images you want to generate bounding boxes for.
3. Modify the `objects` list in the script to specify the objects you want to identify.
4. Run the program. It will create an "annotations" folder containing the bounding box coordinates for each uploaded image.

---

## Visualizing the Bounding Boxes

If you want to visualize the bounding boxes on the images, follow these steps:

1. Download the dataset as a zip file along with the "annotations" folder from Colab.
2. Download the `drawer.py` script.
3. Place the `drawer.py` script in a folder and unzip the dataset inside the folder.
4. Modify the `get_class_color` function inside `drawer.py` to set the desired colors for each class.
5. Run the program to visualize the bounding boxes on the images.

---
