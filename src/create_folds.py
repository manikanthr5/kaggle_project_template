import sys
import argparse
import pandas as pd
from pathlib import Path
from sklearn import model_selection

def parse_arguments(args=None):
    parser_desc = """Process input to create_folds.py.

    Each argument is a dataset from Kaggle competition.
    cat_in_the_data: https://www.kaggle.com/c/cat-in-the-dat/
    covid19_global_forecasting_week1: https://www.kaggle.com/c/covid19-global-forecasting-week-1/
    demand_forecasting_kernels_only: https://www.kaggle.com/c/demand-forecasting-kernels-only/
    home_data_for_ml_course: https://www.kaggle.com/c/home-data-for-ml-course/
    kannada_mnist: https://www.kaggle.com/c/Kannada-MNIST/
    web_traffic_timeseries_forecasting: https://www.kaggle.com/c/web-traffic-time-series-forecasting/
    tensorflow2_question_answering: https://www.kaggle.com/c/tensorflow2-question-answering
    """
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-cid", "--cat_in_the_data", action="store_true", dest="cat_in_the_data", default=False)
    parser.add_argument("-cgfw1", "--covid19_global_forecasting_week1", action="store_true",
                        dest="covid19_global_forecasting_week1", default=False)
    parser.add_argument("-dfko", "--demand_forecasting_kernels_only", action="store_true",
                        dest="demand_forecasting_kernels_only", default=False)
    parser.add_argument("-hdfmc", "--home_data_for_ml_course", action="store_true", dest="home_data_for_ml_course",
                        default=False)
    parser.add_argument("-kmnist", "--kannada_mnist", action="store_true", dest="kannada_mnist", default=False)
    parser.add_argument("-wttsf", "--web_traffic_timeseries_forecasting", action="store_true",
                        dest="web_traffic_timeseries_forecasting", default=False)
    parser.add_argument("-tf2qa", "--tensorflow2_question_answering", action="store_true",
                        dest="tensorflow2_question_answering", default=False)
    args = parser.parse_args(args)
    return vars(args)

class CreateFolds:
    def __init__(self):
        pass

    def createFolds(self):
        pass

def main():
    args = parse_arguments(sys.argv[1:])
    print(args)
    if args['cat_in_the_data']:
        if Path("../input/cat-in-the-dat/train.csv").is_file():
            df = pd.read_csv("../input/cat-in-the-dat/train.csv")
            print(df.shape)
        else:
            raise FileNotFoundError("Train file is not present in ../input/cat-in-the-dat/ folder.")

if __name__ == "__main__":
    main()
