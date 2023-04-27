import pandas as pd
import numpy as np
import os
import sys

from Configuration import config
from  typing import Tuple 

class DataIngestion:

    def data_ingestion(self) -> Tuple[pd.DataFrame,pd.DataFrame]:
        train=pd.read_csv(config.TRAIN_DATASET)
        validation=pd.read_csv(config.TEST_DATASET)
        return train,validation


