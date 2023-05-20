import pandas as pd
def main():
    data = [[1000,25],[280,120],[900,30]]
    df = pd.DataFrame(data,columns=['unit price','number'],index=['store1','store2','store3'])
    print(df)
    df['total price'] = df['unit price']*df['number']
    print(df)
    df = df.sort_values(by='total price',ascending=False)
    print(df.head(2))
if __name__ == "__main__":
    main()