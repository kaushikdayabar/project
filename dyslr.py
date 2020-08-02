def dyslr():
    import pandas_ods_reader as pds
    import sklearn as sk
    from sklearn.model_selection import train_test_split
    import scipy.stats as sc
    import statsmodels.api as sm
    import numpy as np


    df=pds.read_ods("dataset1_part2.ods",1)


    x=list(df["pr2"])
    n=len(x)


    y=list(df["P2"])
    random_list=[i for i in range(1129)]


    xstd,ystd=sc.tstd(x,ddof=1),sc.tstd(y,ddof=1)
    xm,ym=np.mean(x),np.mean(y)
    xn=sc.zscore(x,axis=0,ddof=2)
    yn=sc.zscore(y,axis=0,ddof=2)


    x_tr,x_te,y_trr,y_tre=train_test_split(xn,random_list,random_state=5,test_size=0.34)


    x_tr=np.array(x_tr)
    y_tr=np.array([yn[i] for i in y_trr])
    model=sm.OLS(x_tr.reshape(-1,1),y_tr).fit()
    model.summary()


    pre=model.predict(x_te)


    def z_inv(l):
        r=[i*(ystd-2)+ym for i in l]
        return r


    act_pre=z_inv(pre)


    act_te=[y[i] for i in y_tre]


    rmse=np.sqrt(sk.metrics.mean_squared_error(act_te,act_pre))


    y_ins=[y[i] for i in y_trr]
    x_ins=[x[i] for i in y_trr ]

    ins=sc.pearsonr(y_ins,x_ins)[0]**2

    oos=sc.pearsonr(act_pre,x_te)[0]**2

    return [round(ins,3),round(oos,3),round(rmse,3)]
