""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	 	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		 	 	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	 	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		 	 	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		 	 	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		 	 	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	 	 		  		  		    	 		 		   		 		  
or edited.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		 	 	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		 	 	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
Student Name: Mengya Ji 		  	   		 	 	 		  		  		    	 		 		   		 		  
GT User ID: mji49  		  	   		 	 	 		  		  		    	 		 		   		 		  
GT ID: 904058393  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		 	 	 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		 	 	 		  		  		    	 		 		   		 		  
from util import get_data, plot_data
import scipy.optimize as spo  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		  	   		 	 	 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		  	   		 	 	 		  		  		    	 		 		   		 		  
def optimize_portfolio(  		  	   		 	 	 		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		 	 	 		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		 	 	 		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],
    gen_plot = True  		  	   		 	 	 		  		  		    	 		 		   		 		  		  	   		 	 	 		  		  		    	 		 		   		 		  
):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	 	 		  		  		    	 		 		   		 		  
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	 	 		  		  		    	 		 		   		 		  
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	 	 		  		  		    	 		 		   		 		  
    statistics.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	 	 		  		  		    	 		 		   		 		  
        symbol in the data directory)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	 	 		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	 	 		  		  		    	 		 		   		 		  
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		  	   		 	 	 		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		 	 	 		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		  	   		 	 	 		  		  		    	 		 		   		 		  
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 	 	 		  		  		    	 		 		   		 		  
    
    #calculate statistics for each stock
    dr = prices.copy()
    dr.iloc[1:] = (prices[1:]/prices[:-1].values) - 1
    dr = dr.iloc[1:]
    adr = dr.mean()
    sddr = dr.std()
    cr = prices.iloc[-1]/prices.iloc[0] - 1
    sr = np.sqrt(252)*adr.div(sddr.replace(0, np.nan)).fillna(0)
      	   		 	 	 		  		  		    	 		 		   		 		  
    # find the allocations for the optimal portfolio      
    def f(allocs):
        port_rets = (dr * allocs).sum(axis=1)
        mu = port_rets.mean()
        sigma = port_rets.std()
        if sigma == 0:
            return 1e9  
        return -np.sqrt(252.0)*(mu/sigma)
    
    n = len(syms)
    Xguess = np.ones(n)/n
    bounds = [(0.0, 1.0)] * n
    min_result = spo.minimize(f, Xguess, method='SLSQP', bounds = bounds, options={'disp':True} )
    allocs = min_result.x	 
    allocs = allocs / allocs.sum()	 	 		  		  		    	 		 		   		 		  	  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 	
    # Get daily portfolio value
    normed_prices = prices/prices.iloc[0]  		  	   		 	 	 		  		  		    	 		 		   		 		  		  	   		 	 	 		  		  		    	 		 		   		 		  
    port_val = normed_prices.mul(allocs, axis=1).sum(axis=1)
 	 
    # Compare daily portfolio value with SPY using a normalized plot 
    pv_normed  = port_val / port_val.iloc[0]
    spy_normed = prices_SPY / prices_SPY.iloc[0]  		  	   		 	 	 		  		  		    	 		 		   		 		  
    if gen_plot:  		  	   		 	 	 		  		  		    	 		 		   		 		  		  	   		 	 	 		  		  		    	 		 		   		 		  
        df_temp = pd.concat([pv_normed, spy_normed], keys=["Portfolio", "SPY"], axis=1)  		  	   		 	 	 		  		  		    	 		 		   		 		  
        ax = df_temp.plot(title= "Daily Portfolio Value and SPY", grid = True)	  
        ax.set_xlabel('Date')
        ax.set_ylabel("Price")
        ax.get_figure().savefig("Figure1.png")	   		 	 	 		  		  		    	 		 		   		 		  
          		  	   		 	 	 		  		  		    	 		 		   		 		  
    port_rets = port_val.pct_change().dropna()
    adr_port = port_rets.mean()
    sddr_port = port_rets.std()
    sr_port = np.sqrt(252) * adr_port / sddr_port if sddr_port > 0 else float('nan')     
    cr_port = port_val.iloc[-1]/port_val.iloc[0] - 1 		  	   		 	 	 		  		  		    	 		 		   		 		  		  		  		    	 		 		   		 		  
    return allocs, cr_port, adr_port, sddr_port, sr_port  		  	  	   		 	 	 		  		  		    	 		 		   		 		  
 		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def test_code():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009, 1, 1)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010, 1, 1)  		  	   		 	 	 		  		  		    	 		 		   		 		  
    symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		 	 	 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	 	 		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True 		  	   		 	 	 		  		  		    	 		 		   		 		  
    )  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"End Date: {end_date}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Symbols: {symbols}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Allocations:{allocations}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio: {sr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return: {adr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return: {cr}")  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	 	 		  		  		    	 		 		   		 		  
