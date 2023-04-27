import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.model_selection import train_test_split

class PreProcessing:

    def __init__(self,train):
        self.missing_values={}
        self.transformed_data=pd.DataFrame()
        self.train=train

    def missing_data_treatment(self) -> None: 
        self.missing_values['Age']=self.train['Age'].median()
        self.missing_values['Embarked']='S'
        self.transformed_data=self.train['Age'].fillna(self.missing_values['Age'])
        self.transformed_data=self.train['Embarked'].fillna(self.missing_values['Embarked'])
        

    def drop_columns(self) -> None:
        self.transformed_data=self.train.drop(columns=['Cabin','PassengerId','Ticket','Name'])

    def categorical_encoding(self) -> None: 
        self.transformed_data=pd.get_dummies(columns=['Sex','Embarked'],data=self.transformed_data)

    def train_test_split(self) -> Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame]:
        X=self.transformed_data.drop(columns=['Survived'])
        y=self.transformed_data['Survived']
        x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.33,random_state=0)
        return x_train,x_test,y_train,y_test
        
    
    def preprocessing_pipline(self) -> pd.DataFrame:
        self.missing_data_treatment()
        self.drop_columns()
        self.categorical_encoding()
        x_train,x_test,y_train,y_test=self.train_test_split()
        return x_train,x_test,y_train,y_test

