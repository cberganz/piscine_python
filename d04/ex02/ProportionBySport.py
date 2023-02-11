from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    df_total = df.loc[(df['Sex'] == gender) & (df['Year'] == year)].drop_duplicates(['ID'],keep='first')
    df_sport = df.loc[(df['Sex'] == gender) & (df['Year'] == year) & (df['Sport'] == sport)].drop_duplicates(['ID'],keep='first')
    if len(df_total): return len(df_sport) / len(df_total)
    else: return None

if __name__ == '__main__':
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    print(proportionBySport(df, 2004, 'Tennis', 'F'))
