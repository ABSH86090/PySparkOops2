from pyspark.sql import SparkSession

class SparkClass:
    def __init__(self,config) -> None:
        self.config = config

    def SparkStart(self,kwargs:dict) -> SparkSession:
        print(self.config)