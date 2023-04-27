import sys
import os

from Source.data_ingestion import *
from Source.preprocessing import *
from Source.model_building import *
from typing import Tuple

def main() -> Tuple[float,float]:
    c=DataIngestion()
    train,validation=c.data_ingestion()
    preprocessing=PreProcessing(train)
    x_train,x_test,y_train,y_test=preprocessing.preprocessing_pipline()
    model_building=ModelBuilding(x_train,x_test,y_train,y_test)
    training_accuracy,testing_accuracy=model_building.model_prediction()
    return training_accuracy,testing_accuracy
    
    
    
