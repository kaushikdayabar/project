def ses():
    from pandas_ods_reader import read_ods
    from sklearn.metrics import mean_squared_error,mean_absolute_error
    import numpy as np

    df=read_ods("dataset_monthly.ods",1)


    y=df["usd/ton5"].values


    rc=[]
    yhatc=[]
    mnc,oac=np.inf,np.nan
    def simple_exp(a,p):
            if p==0:
                return y[0]
            else:
                return yhatc[p-1]+a*(y[p-1]-yhatc[p-1])


    mn,oa=np.inf,np.nan
    yhatc=[]
    for i in np.arange(0.1,1,0.01).round(2):
        for j in range(355):
            yhatc.append(simple_exp(i,j))
        maec=mean_absolute_error(y,yhatc)
        rmsec=np.sqrt(mean_squared_error(y,yhatc))
        yhatc=[]
        if rmsec<mn:
            oa=i
            mn=rmsec
        rc.append([i,maec,rmsec])

    return [np.nan,np.nan,round(rmsec,3)]
