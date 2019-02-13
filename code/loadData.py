'''
Created on Apr 25, 2016
test code 
@author: Wenqiang Feng 
'''
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from docutils.parsers.rst.directives import path

if __name__ == '__main__':
    path ='~/Dropbox/MachineLearningAlgorithms/python_code/data/Heart.csv' 
    rawdata = pd.read_csv(path)
    
    print "data summary"
    print rawdata.describe()
    
    # summary plot of the data
    scatter_matrix(rawdata,figsize=[15,15])
    plt.show()
    
    # Histogram 
    rawdata.hist()
    plt.show()
    
    # boxplot 
    pd.DataFrame.boxplot(rawdata)
    plt.show()
    
    
    print "Raw data size"
    nrow, ncol = rawdata.shape
    print nrow, ncol
    
    path = ('/home/feng/Dropbox/MachineLearningAlgorithms/python_code/data/'
    'energy_efficiency.xlsx')
    path
            
    rawdataEnergy= pd.read_excel(path,sheetname=0)
    
    nrow=rawdata.shape[0] #gives number of row count
    ncol=rawdata.shape[1] #gives number of col count
    print nrow, ncol
    col_names = rawdata.columns.tolist()
    print "Column names:"
    print col_names
    print "Data Format:"
    print rawdata.dtypes
    
    print "\nSample data:"
    print(rawdata.head(6))
    
    
    print "\n correlation Matrix"
    print rawdata.corr()
    
    # cocorrelation Matrix plot     
    pd.DataFrame.corr(rawdata)
    plt.show()
    
    print "\n covariance Matrix"
    print rawdata.cov()
    
    print rawdata[['Age','Ca']].corr()
    pd.DataFrame.corr(rawdata)
    plt.show()
    

    
    # define colors list, to be used to plot survived either red (=0) or green (=1)
    colors=['red','green']

    # make a scatter plot

#    rawdata.info()

    from scipy import stats
    import seaborn as sns # just a conventional alias, don't know why
    sns.corrplot(rawdata) # compute and plot the pair-wise correlations
    # save to file, remove the big white borders
    #plt.savefig('attribute_correlations.png', tight_layout=True)
    plt.show()
    
    
    attr = rawdata['Age']
    sns.distplot(attr)
    plt.show()
    
    sns.distplot(attr, kde=False, fit=stats.gamma);
    plt.show()
    
    # Two subplots, the axes array is 1-d
    plt.figure(1)
    plt.title('Histogram of Age')
    plt.subplot(211) # 21,1 means first one of 2 rows, 1 col 
    sns.distplot(attr)
    
    plt.subplot(212) #  21,2 means second one of 2 rows, 1 col 
    sns.distplot(attr, kde=False, fit=stats.gamma);

    plt.show()
    
    
    
    
    
    