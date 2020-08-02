def sma():
    from pandas_ods_reader import read_ods
    from sklearn.metrics import mean_squared_error,mean_absolute_error
    import numpy as np

    df=read_ods("dataset_monthly.ods",1)

    data=df["usd/ton5"].values
    x=[data[i] for i in range(355)]


# simple moving average
    r=[]                             #result list
    mn,owdw=np.inf,np.nan            #mn=minimum rmse, owdw=optimal window
    for wdw in range(3,100):
        yhat1=df["usd/ton5"].rolling(window=wdw).mean()
        mae=mean_absolute_error(x[wdw:],yhat1[wdw:]).round(2)
        rmse=np.sqrt(mean_squared_error(x[wdw:],yhat1[wdw:])).round(2)
        if rmse<mn:
            owdw=wdw
            mn=rmse
        r.append([wdw,mae,rmse])


    return [np.nan,np.nan,round(mn,2)]
