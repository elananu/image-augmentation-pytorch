# Image Data Augmentation using PyTorch

## Aim

To perform various image data augmentation techniques using PyTorch and TorchVision to increase dataset diversity and improve model performance.

## Problem Statement

Deep learning models require large datasets. However, collecting data is costly and time-consuming. Data augmentation helps generate new training samples from existing images to reduce overfitting.

## Objectives

* Apply image transformations using TorchVision
* Perform scaling, cropping, flipping, padding, rotation
* Apply color augmentation techniques
* Combine multiple transformations
* Save and visualize transformed images

## Technologies Used

* Python
* PyTorch
* TorchVision
* PIL
* Matplotlib

## Project Structure

```
image-augmentation-pytorch/
│── main.py
│── requirements.txt
│── sample_image.jpg
│── outputs/
```

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the program:

```
python main.py
```

## Output

The transformed images will be saved inside the `outputs/` folder.

## Conclusion

Data augmentation techniques improve dataset diversity and reduce overfitting, helping deep learning models generalize better.
