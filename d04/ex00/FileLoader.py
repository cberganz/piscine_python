import pandas as pd

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions " + str(len(df)) + " x " + str(len(df.columns)))
        return df

    def display(self, df, n):
        print(df.head(n).to_string())

if __name__ == '__main__':
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    fl.display(df, -10)
