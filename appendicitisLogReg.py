import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('Regensburg Pediatric Appendicitis.csv')
diagnosis_map = {'appendicitis': 1, 'no appendicitis': 0}
df['Diagnosis'] = df['Diagnosis'].map(diagnosis_map)

cleaned_df = df[
    ['Age', 'BMI', 'Height', 'Weight', 'Body_Temperature', 'WBC_Count', 'RBC_Count', 'Hemoglobin', 'Thrombocyte_Count',
     'Diagnosis']].dropna()
features = ['Age', 'BMI', 'Height', 'Weight', 'Body_Temperature', 'WBC_Count', 'RBC_Count', 'Hemoglobin',
            'Thrombocyte_Count']
X = cleaned_df.loc[:, features]
Y = cleaned_df.loc[:, ['Diagnosis']]

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=.75)
y_train = np.ravel(y_train)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
model.predict(X_test)

def prediction(age, bmi, h, w, bt, wbcc, rbcc, hg, tc):
    X_predict = {'Age': [age],
                 'BMI': [bmi],
                 'Height': [h],
                 'Weight': [w],
                 'Body_Temperature': [bt],
                 'WBC_Count': [wbcc],
                 'RBC_Count': [rbcc],
                 'Hemoglobin': [hg],
                 'Thrombocyte_Count': [tc]
                 }
    X_predict_df = pd.DataFrame(X_predict)
    print(X_predict_df)
    return model.predict(X_predict_df)

def score():
    return model.score(X_test, y_test)
