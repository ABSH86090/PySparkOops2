import logging
import os, json
from pyspark.sql import SparkSession

### Create var path for root path to our project directory ######
project_drirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = f"{project_drirectory}/logs/job-{os.path.basename(__file__)}.log"

