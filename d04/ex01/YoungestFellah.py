from FileLoader import FileLoader

def youngestFellah(df, year):
    df1 = df.loc[df['Year'] == year]
    df2 = df1.loc[df1['Sex'] == "M"]
    df3 = df1.loc[df1['Sex'] == "F"]
    return { "f": df3['Age'].min(), "m": df2['Age'].min() }


if __name__ == '__main__':
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    print(youngestFellah(df, 2004))
