def dsma():
    from pandas_ods_reader import read_ods
    from sklearn.metrics import mean_squared_error,mean_absolute_error
    import numpy as np

    df=read_ods("dataset1_part2.ods",1)

    data=df["price"].values
    x=[data[i] for i in range(1095)]


# simple moving average
    r=[]                             #result list
    mn,owdw=np.inf,np.nan            #mn=minimum rmse, owdw=optimal window
    for wdw in range(3,100):
        yhat=df["price"].dropna().rolling(window=wdw).mean()
        mae=mean_absolute_error(x[wdw:],yhat[wdw:]).round(3)
        rmse=np.sqrt(mean_squared_error(x[wdw:],yhat[wdw:])).round(3)
        if rmse<mn:
            owdw=wdw
            mn=rmse
        r.append([wdw,mae,rmse])


    return [np.nan,np.nan,round(mn,3)]
