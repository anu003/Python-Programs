import re
import os
import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.stats import anderson
from statsmodels.stats.diagnostic 
import normal_ad
pd.options.mode.chained_assignment = None  # default='warn'
class DataProfiling(object):
    """Performs data profiling"""
    
    def __init__(self, data, data_type):        
    """  input : pandas series       
    Instantiates the class, initializes the data and makes the function calls"""
    self.data = data        
    self.data_type = data_type        
    if self.data_type == 'numeric':            
        self._completeness_analysis()            
        self._uniqueness_analysis()           
        self._range_analysis()            
        self._distribution_analysis()            
        self._pattern_analysis()        
    else:            
        self._completeness_analysis()            
        self._uniqueness_analysis()            
        self._range_analysis()
    
    def _completeness_analysis(self):        
    """ output : str        
        Outputs how often a value is populated vs null, also provides necessary recommendations"""        
        print("Completeness Analysis")        
        print("----------------------------------------------")
        try:            
              row_count = self.data.shape[0]            
              print("Total number of rows:", row_count)            
              null_count = self.data.isnull().sum()            
              null_count_percent = null_count * 100 / row_count            
              print("Null values:", null_count, ' ', null_count_percent, '%')            
              if null_count_percent >= 50:                
                 print('Recommendation: consider dropping the column')            
              elif 0 < null_count_percent < 50:                
                 print('Recommendation: Check if the value is NaN on purpose,','consider either imputing or dropping the data if needed')
        except ValueError as err:            
                print("An error occurred while performing completeness check: ", err)
                
    def _uniqueness_analysis(self):        
    """ output : str        
        Outputs the number of unique (distinct) values and recommends actions to performed on the data"""        
        print("\nUniqueness Analysis")        
        print("----------------------------------------------")        
        unique_values = len(self.data.unique())        
        print("Number of Unique Values: ", unique_values)        
        if unique_values == 1:            
                print('Recommendation: consider dropping the column, as it has 0 variance')        
        if unique_values == len(self.data) and self.data_type != 'numeric':            
                print('Recommendation: consider dropping the column, as each value is unique')
                
    def _range_analysis(self):        
    """ output : str        
        Outputs the min, max, mean and median values for numeric data and count of each unique category for categorical data"""                  try:            
        if self.data_type == 'numeric':                
        print("\nRange Analysis")                
        
        print("----------------------------------------------")                
        print("Minimum: ", self.data.min())                
        print("Maximum: ", self.data.max())                
        print("Mean:    ", self.data.mean())                
        print("Median:  ", self.data.median())            
        else:               
            print("\nCount of each unique value:")                
            print("----------------------------------------------")                
            col_count = self.data.dropna().value_counts()                
            col_count_percent = self.data.dropna() \                    
                                         .value_counts(normalize=True) \                    
                                         .apply(lambda x: str(round(x * 100, 2)) + '%')                
            print(pd.concat([col_count, col_count_percent], axis=1))
        except ValueError as err:            
            print('An error occurred while performing range analysis: ', err)
            
    def _distribution_analysis(self):        
    """ output : boolean        
        Outputs whether the data follows a normal distribution or not and also plots the histogram and Normal Probability plot"""      
        print("\nDistribution Analysis")        
        print("----------------------------------------------")
        try:            
            ad_test_statistic, pvalue = normal_ad(self.data[~np.isnan(self.data)])
            print('Anderson-Darling Test Coefficient: ', ad_test_statistic)
            if pvalue > 0.05:               
                print('Normal Distribution: ', True)            
            elif pvalue < 0.05:                
                print('Normal Distribution: ', False)            
            else:                
                print('We need to collect more data to check if the data follows a normal distribution')
            plt.figure(1)
            # histogram of the data            
            plt.subplot(2, 1, 1)            
            plt.hist(self.data[~np.isnan(self.data)], bins=30)            
            plt.title('Histogram')            
            plt.xlabel('Values')            
            plt.ylabel('Frequency')
            # Normal Probability Plot            
            plt.subplot(2, 1, 2)            
            sc.stats.probplot(self.data[~np.isnan(self.data)], dist="norm", plot=plt)            
            plt.show()
        except ZeroDivisionError:
            print("The argument does not contain numbers\n")
            
    def _pattern_analysis(self):        
        pass
def get_profiling(df, report_title='Data Profiling Report'):    
    categorical = list(df.select_dtypes(include=['object']).columns)    
    datetime = list(df.select_dtypes(include=['datetime64']).columns)    
    for col in df.columns:        
        print('\nData Profiling for column: ', col, '\n')        
    if col in categorical:            
        column_type = 'categorical'        
    elif col in datetime:            
        column_type = 'datetime'        
    else:            
        column_type = 'numeric'       
    dp = DataProfiling(df[col], column_type)
