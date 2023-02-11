from FileLoader import FileLoader

def howManyMedals(df, name):
    df_athlete = df.loc[df['Name'] == name]
    min_year = df_athlete['Year'].min()
    max_year = df_athlete['Year'].max()
    ret = {}
    for year in range(min_year, max_year + 1):
        df_curr_year = df_athlete.loc[df['Year'] == year]
        if len(df_curr_year):
            g = len(df_curr_year.loc[df['Medal'] == 'Gold'])
            s = len(df_curr_year.loc[df['Medal'] == 'Silver'])
            b = len(df_curr_year.loc[df['Medal'] == 'Bronze'])
            ret[year] = { "G": g, "S": s, "B": b }
    return ret

if __name__ == '__main__':
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    dict = howManyMedals(df, 'Kjetil Andr Aamodt')
    print('\n'.join(f'{key}: {value}' for key, value in dict.items()))
