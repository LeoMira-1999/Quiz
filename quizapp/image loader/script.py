import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('images.xlsx', index_col=0)

    dico = df.to_dict()
