

def simple_eda(df):
    print('DataFrame Shape:\n', df.shape, '\n\n')
    display('DataFrame Head:', df.head().T)
    print('\n\nDataFrame Statistical Description:\n', df.describe(), '\n\n')
    print('DataFrame Column Types:\n', df.dtypes,'\n\n')
    print('\nDataFrame count: ', '\n', df.count())
    print('\n\nDataFrame Null Value Count:\n', df.isnull().sum())