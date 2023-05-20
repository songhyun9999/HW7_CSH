import pandas as pd
def main():
    data = pd.read_csv("gender2.csv",encoding='cp949',index_col='행정구역')
    #print(data.columns)
    df = data.loc[:,['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']]
    df.rename(columns={'2022년_계_총인구수':'Total'},inplace=True)
    df.rename(columns={'2022년_남_총인구수':'Male'},inplace=True)
    df.rename(columns={'2022년_여_총인구수':'Female'},inplace=True)

    print(df)


if __name__ == "__main__":
    main()