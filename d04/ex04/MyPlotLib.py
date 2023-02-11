import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import scatter_matrix
from FileLoader import FileLoader

class MyPlotLib:
    def histogram(df, features):
        for feat in features:
            plt.figure()
            plt.title(feat)
            plt.hist(df[feat])
        plt.show()

    def density(df, features):
        plt.figure()
        for feat in features:
            df[feat].plot(kind='density')
        plt.show()

    def pair_plot(df, features):
        data = pd.DataFrame()
        for feat in features:
            data[feat] = df[feat]
        scatter_matrix(data)
        plt.show()

    def box_plot(df, features):
        for feat in features:
            df.boxplot(features)
        plt.show()

if __name__ == '__main__':
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    #MyPlotLib.histogram(df, ["Weight", "Height"])
    #MyPlotLib.density(df, ["Weight", "Height"])
    MyPlotLib.pair_plot(df, ["Weight", "Height"])
    #MyPlotLib.box_plot(df, ["Weight", "Height"])
