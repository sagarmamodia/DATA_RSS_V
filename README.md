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

    Metrics used for evaluation (Accuracy, AUC, F1-score, etc.).
    Model performance summary with tables/graphs (if applicable).
    Comparisons with baseline models.

## Results & Visualizations

    ![Uploading image.png…]()


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
