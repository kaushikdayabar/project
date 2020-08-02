def ddes():
    from sklearn.metrics import mean_squared_error,mean_absolute_error
    from pandas_ods_reader import read_ods
    import numpy as np

    df=read_ods("dataset1_part2.ods",1)
    y=list(df["price"].dropna().values)
    rc,l,t,f=[],[y[0]],[y[1]-y[0]],[np.nan]

    def double_exp(a,b,p):
        if p==0:
            f.append(l[0]+t[0])
            return f[1]
        else:
            l.append(a*y[p]+(1-a)*f[p])
            t.append(b*(l[p]-l[p-1])+(1-b)*t[p-1])
            f.append(l[p]+t[p])
            return f[-1]

    mrmse,mmae,oa,ob=np.inf,np.inf,np.nan,np.nan
    yhatc=[np.nan]
    for i in np.arange(0.1,1,0.01).round(2):
        for j in np.arange(0.1,1,0.01).round(2):
            for k in range(1094):
                yhatc.append(double_exp(i,j,k))
            maec=mean_absolute_error(y[1:],yhatc[1:])
            rmsec=np.sqrt(mean_squared_error(y[1:],yhatc[1:]))
            yhatc=[np.nan]
            l,t,f=[y[0]],[y[1]-y[0]],[np.nan]
            if rmsec<mrmse:
                oa=i
                ob=j
                mrmse=rmsec
                mmae=maec
            rc.append([i,j,maec,rmsec])


    return [np.nan,np.nan,round(mrmse,3)]
