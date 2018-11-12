import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,LogisticRegressionCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

titanic_df = pd.read_csv('C:\\Tensorflow\\titanic_train.csv')
titanic_df .drop('Cabin',axis=1,inplace=True)
titanic_df .drop('Age',axis=1,inplace=True)

sex = pd.get_dummies(titanic_df['Sex'],drop_first=True)
embark = pd.get_dummies(titanic_df['Embarked'],drop_first=True)
titanic_df.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
titanic_df= pd.concat([titanic_df,sex,embark],axis=1)


X_train, X_test, y_train, y_test = train_test_split(titanic_df.drop('Survived',axis=1),
                                                    titanic_df['Survived'], test_size=0.30,
                                                    random_state=101)
logmodel = LogisticRegressionCV(max_iter=1000,cv=10)
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

