## Project Description

The project utilized various features related to demographics, lifestyle, and psychological factors to assess potential 
mental health conditions. The model was trained on a labeled dataset and evaluated using metrics like accuracy and AUC.
The goal was to create an accessible tool that could provide preliminary insights into users' mental well-being, aiding 
in early detection and awareness.

## Dataset

Remote work and mental health dataset was used to train the models. (https://www.kaggle.com/datasets/iramshahzadi9/remote-work-and-mental-health/). The data consists of 20 features such as Age, Job, etc and about 5000 rows.

## Model Architecture

Multiple models were trained on the data - XGBoost, SVM, LogisticRegression and KNN. Out of these XGBoost performed best and therefore it was used in the predict_mental_health.py script.

## Installation

1. Clone the repository on your local system (git clone)
2. Install Dependences using
    `pip install -r requirements.txt`
4. Copy the test dataset to the directory (let's say it is named test.csv)
5. Run the following script to get predictions
    `python predict_mental_health.py test.csv`
    

## Evaluation & Performance
```
Metric        Value
---------  --------
Accuracy   0.353
Precision  0.352071
Recall     0.353
F1 Score   0.351785
```

## Sample Predictions
Sample Data:
![Screenshot 2025-02-22 100414](https://github.com/user-attachments/assets/7e2188e1-ebde-48c8-86f3-cb2bd57306ca)

Predictions:
![Screenshot 2025-02-22 100429](https://github.com/user-attachments/assets/d0b0bcbe-aec8-4ef2-a555-b93e0828b9fe)

## Project Structure

```
├── data/                        # Raw and processed dataset
├── models/                      # Trained models
├── model_training.ipynb         # Training notebook
├── predict_mental_health.py/    # predict script
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
```


## Acknowledgments

   Thanks to the IIT Roorkee Cognizance team for conducting this competition.
