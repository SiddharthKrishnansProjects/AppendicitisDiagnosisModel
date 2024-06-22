# AppendicitisDiagnosisModel
A binary classification algorithm which takes in several clinical data inputs to aid in the diagnosis of appendicitis in children. Training and testing data was obtained from the Children’s Hospital St. Hedwig in Regensburg, Germany and repurposed into a .csv file, which I downloaded off Kaggle. This data was trimmed to only include numerical and objective feature data and patients with missing parameters were removed from the training and testing data. The Python Sci-kit package's Logistic Regression model was implemented to predict appendicitis, and a simple GUI application was implemented (using the Python Tkinter package) to enter parameters and get a prediction outputted.

Instructions: Download all files into a single folder, and run appendicitisApp.py. Input data into the required fields and it will output a diagnosis prediction as well as the score of the model.



References:

Marcinkevičs, R., Reis Wolfertstetter, P., Klimiene, U., Ozkan, E., Chin-Cheong, K., Paschke, A., Zerres, J., Denzinger, M., Niederberger, D., Wellmann, S., Knorr, C., & Vogt, J. E. (2023). Regensburg Pediatric Appendicitis Dataset (1.01) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7669442
