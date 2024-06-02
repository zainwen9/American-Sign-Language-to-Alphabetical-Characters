# Sign Language Alphabet Recognizer
This project is a sign language alphabet recognizer using Python, openCV and a convolutional neural network model for classification. 
The goal of this project is to build a neural network which can identify the alphabet of the American Sign Language (ASL) through video input or images and translate it into text.

## Dataset
The primary source of data for this project was the compiled dataset of American Sign Language (ASL) from [Kaggle](https://www.kaggle.com/ayuraj/american-sign-language-dataset).
The dataset is comprised of 18,200 images which are 200x200 pixels. There are 26 total classes, each with 700 images, 26 for the
letters A-Z.
<p align="center" >
  <img  width="600" src="https://github.com/parakh-gupta/Sign_language_alphabet_recognizer/blob/master/alphabet.png">
</p>

## Requirements:
* Python
* OpenCV
* NumPy
* Pandas
* Tensorflow
* Keras

All the requirements can be installed from 

pip install -opencv
pip install -keras
pip install -numpy
pip install -streamlit
pip install -tensorflow
pip install -pillow


## To Run
Command: streamlit run app.py
This command will make a localhost on your system using streamlit a hosting library and package for python.

## Demo Video

<p align="center">
  <iframe width="560" height="315" src="https://www.instagram.com/reel/C7t761PNjom/?igsh=YTg5d3R2Y2t2dGky" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

## Features
Our model was able to predict the 44 characters in the ASL with a prediction accuracy >95%.

Features that can be added:
* Deploy the project on cloud and create an API for using it.
* Increase the vocabulary of our model.
* Incorporate feedback mechanism to make the model more robust.
* Add more sign languages.

## Status
Project is: _finished_. was developed as a 6th semester final project for artificial neural networks.

## Contact
Created by me @zainwen9.

If you loved what you read here and feel like we can collaborate to produce some exciting stuff, or if you
just want to shoot a question, please feel free to connect with me on <a href="zainweb9@gmail.com" target="_blank">email</a>, 
<a href="https://www.linkedin.com/in/zain-mehmood-163254270" target="_blank">LinkedIn</a>, or 
<a href="https://www.instagram.com/zain_dev_?igsh=MTQzYjhqc244OTloOA%3D%3D&utm_source=qr" target="_blank">Instagram</a>. 
My other projects can be found on my GitHub Profile.

