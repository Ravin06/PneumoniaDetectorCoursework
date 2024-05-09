# [Group B -- Team YBN] 2023 Sec 4 Computing+ Coursework



## Purpose

We are interested in using AI for image recognition to identity diseases and possible health risks from chest x-rays. And we hope to be able to create an AI model that can aid the healthcare industry by using machine learning and prevent diseases that are not easily detectable from worsening.



## Summary of Project

This is a repository for a coursework project on detecting pneumonia from chest X-ray images using deep learning. The project is implemented using Python and the PyTorch deep learning library, and is divided into several components, each contained in a separate Python script.



## Build Status and Progress

Currently, the program is essentially functional, where the model is able to detect and give a diagnose based on the image that is being uploaded to the program. 



## Programme Specifics

The code is written with Python3. The AI model was built using Python in Google Colaboratory. 
### Precision vs Recall
![download (1)](https://github.com/Ravin06/PneumoniaDetectorCoursework/assets/77960307/d5880898-ce23-47e8-88f0-93cd793d9343)
### ROC Curve
![download](https://github.com/Ravin06/PneumoniaDetectorCoursework/assets/77960307/9c77e21f-14a3-4f52-9242-4b639af24771)
### Model Accuracy (Final accuracy = 90.8%)
![download (2)](https://github.com/Ravin06/PneumoniaDetectorCoursework/assets/77960307/0879853d-249b-4c66-8d9a-cc13b05908bc)


## Installation

To run the project, you will need to have the following libraries installed:

- Python 3.x  
- PyTorch 1.x  
- NumPy  
- matplotlib  
- scikit-learn  
- Pillow  
- tqdm  
- keras  
- tensorflow(ensure the cpu brand is intel/amd and not m1/m2 apple chip)  
In addition, you will need to download the dataset used in the project from the following link: https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia. The dataset contains two folders of chest X-ray images, one for normal cases and one for pneumonia cases.  
You can run pip install -r requirements.txt to install all the necessary libaries and dependencies(except for tensorflow and PyTorch) needed to run the code.  
You are required to download tensorflow and PyTorch on your own by running this in terminal:  
pip install tensorflow  
pip3 install torch torchvision torchaudio  


## Use of Program

To run the project, open FinalGui.py in IDLE and run it with everything in the same folder.
Disclaimer: We cannot ensure the script working in Terminal/anything outside of IDLE just yet, it is a work in progress as of now.

## Project Presentation

![image](https://github.com/Ravin06/PneumoniaDetectorCoursework/assets/77960307/a113e3b2-acb5-40ca-9a64-92028b1546ac)https://sites.google.com/sst.edu.sg/cp-coursework-gallery/2023/pneumonia-detection?authuser=0
