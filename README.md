# recommendation-system-undergraduate-program

Selecting undergraduate program is one of the most challenging phase for a high school graduate.
This repo contains codes from my personal research when I taking a master degree in Islamic University of Indonesia. It is my final project for the thesis. 
In the research, I developed a machine learning model which then will be used in a recommendation system. The recommendation system itself aims to help students identify what undergraduate programs which actually match with their academic achievement during the study in the high school.
Not only the academic performance, the recommendation system also consider other categories like gender, type of high school, school's major and hobby. 

## Machine Learning Model
In this recommendation system, I used Random Forest algorithm to trained the classification model. Random forest was selected because it perform best compared to other classification algoritm such as Multinomial Logistic Regression and Support Vector Machine. 
The model was trained use intenall college students data in Islamic University of Indonesia. I can't explained in detail about the process since it is a credential. 
If you curious about how I developed the model, you can read my journal published [here](http://jurnal.iaii.or.id/index.php/RESTI/article/view/3392).

## Dashboard
The recommendation system is visualized in a simple dashboard using Python Dash. 
Using the dashboard you can experience how the recommendation system work. 

## How to run the dashboard
Run the *index.py* file. 
The dashboard will visible in your localhost in port 8050. 
Access here: http://127.0.0.1:8050/

## Note
The dashboard was build in Indonesian language.