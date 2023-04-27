from sklearn.model_selection import train_test_split
from typing import Tuple
import lightgbm as lgb


class ModelBuilding():
    def __init__(self,x_train,x_test,y_train,y_test) -> None:
        self.x_train=x_train
        self.x_test=x_test
        self.y_train=y_train
        self.y_test=y_test
        

    def model_prediction(self) -> Tuple[float,float]:
        model = lgb.LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)
        model.fit(self.x_train,self.y_train,eval_set=[(self.x_test,self.y_test),(self.x_train,self.y_train)],
          verbose=20,eval_metric='logloss')
        train_accuracy=model.score(self.x_train,self.y_train)
        test_accuracy=model.score(self.x_test,self.y_test)
        return train_accuracy,test_accuracy