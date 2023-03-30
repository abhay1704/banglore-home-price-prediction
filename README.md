![ML](https://img.shields.io/badge/ML-Regression-blue.svg)

# banglore-home-price-prediction
A machine learning model trained on banglore home prices dataset for home price prediction

## Project Objectives :
The objective of the project is to create a machine learning model using Supervised Machine Learning and Deploy it.

## Data Collection :
The dataset is obtained from Kaggle. 

Link: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data

## Modelling :
The analysis, data processing and model creation can be found in the .ipynb file. 

The main packages used are numpy, pandas, matplotlib, and sklearn.  

## Deployemnt :
The web app has been build using basic HTML, CSS, Javascript, Flask and deploloyed on netlify.

Link: https://bpml.netlify.app/

![](assets/Screenshot%20(223).png)

---
It is also Deployed as API End Point on [pythonanywhere](https://www.pythonanywhere.com/).

Link: https://abhay1704.pythonanywhere.com/get_price

method: POST, <br>
location: "[Location](https://abhay1704.pythonanywhere.com/loc)", <br>
bath: "No of Bathrooms", <br>
size: "No of Bedrooms(BHKs), <br>
total_sqft: "Total area of house in Sqft" <br>
