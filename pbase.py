def pbase():
    import pandas_ods_reader as pds
    import sklearn as sk
    from sklearn.model_selection import train_test_split
    import scipy.stats as sc
    import statsmodels.api as sm
    import numpy as np


    df=pds.read_ods("dataset_monthly.ods",1)

    # preparing independent variable
    xn=list(df["Exc_1"])[:-1]
    x1n=xn[:-1]
    x2n=xn[1:]


    xl1n=list(np.log(x1n))
    xl2n=list(np.log(x2n))


    xdl=[]
    lexl1n=len(xl1n)
    for i in range(lexl1n):
        xdl.append(xl2n[i]-xl1n[i])
    #del ln


    x=[]
    for i in range(352):
        x.append(xdl[i+1]+xdl[i])  #clp[t-1]+clp[t-2]

    # preparing dependent variable

    yn=list(df["usd/ton5"][2:])     #p(t)=clp(t-1)+clp(t-2)
    yl=list(np.log(yn))
    leny=len(yn)


    yout,y=[],0
    rem={}
    leny=leny-1
    for i in range(leny):
        y=yl[i+1]-yl[i]
        yout.append(y)
        rem[i]=[y,yl[i]]

    xstd,ystd=sc.tstd(x,ddof=1),sc.tstd(yout,ddof=1)
    xm,ym=np.mean(x),np.mean(yout)

    x=sc.zscore(x,axis=0,ddof=2)
    y=sc.zscore(yout,axis=0,ddof=2)
    test_random=[i for i in range(352)]
    x=[round(i,3) for i in x]
    y=[round(i,3) for i in y]

    x_tr,x_te,y_tr,y_te=train_test_split(x,test_random,random_state=5,test_size=0.3)


    x_tr=np.array(x_tr)
    y_tr=np.array([y[i] for i in y_tr])
    model=sm.OLS(x_tr.reshape(-1,1),y_tr).fit()


    pre=model.predict(x_te)
    pre=list(pre)

    #actual result
    y_test=[yout[i] for i in y_te]

    def z_inv(l):
        r=[i*(ystd-2)+ym for i in l]
        return r



    pre_z_inv=z_inv(pre)

    # del inverse

    def del_inv(l):
        yn_1=[rem[i][1] for i in y_te]
        ylog_predicted=[yn_1[i]+l[i] for i in range(106)]
        return ylog_predicted


    pre_z_del_inv=del_inv(pre_z_inv)


    def log_inv(l):
        r=[np.exp(i) for i in l]
        return r


    act_pre=log_inv(pre_z_del_inv)


    rmse=np.sqrt(sk.metrics.mean_squared_error(y_test,act_pre))


    oos=sc.pearsonr(act_pre,x_te)[0]**2


    ins=sc.pearsonr(y_tr,x_tr)[0]**2

    return [round(ins,3),round(oos,3),round(rmse,3)]
