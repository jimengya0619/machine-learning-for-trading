""""""  		  	   		 	 	 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
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
  		  	   		 	 	 		  		  		    	 		 		   		 		  
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
	  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def author():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return "mji49"  # replace tb34 with your Georgia Tech username.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def gtid():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return 904058393  # replace with your GT ID number  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		 	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		 	 	 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    result = False  		  	   		 	 	 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		 	 	 		  		  		    	 		 		   		 		  
        result = True  		  	   		 	 	 		  		  		    	 		 		   		 		  
    return result  		  	   		 	 	 		  		  		    	 		 		   		 		  

def play_without_limit(df, win_prob, episode_spins, times):
    
    for i in range(times):
        episode_winnings = 0
        spins = 0
        df.iloc[i,0] = episode_winnings
        while episode_winnings < 80 and spins < episode_spins:
            won = False
            bet_amount = 1
            while not won and spins < episode_spins:
                won = get_spin_result(win_prob)
                if won:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                spins += 1
                df.iloc[i, spins] = episode_winnings

def play_with_limit(df, win_prob, episode_spins, times):
    for i in range(times):
        episode_winnings = 0
        spins = 0
        df.iloc[i,0] = episode_winnings
        while -256 < episode_winnings < 80 and spins < episode_spins:
            won = False
            bet_amount = 1
            while not won and spins < episode_spins and -256 < episode_winnings < 80:
                won = get_spin_result(win_prob)
                if won:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = min(bet_amount*2, episode_winnings+256)
                spins += 1
                df.iloc[i, spins] = episode_winnings          

def save_fig(fig, fname):
    fig.savefig(fname, dpi=150, bbox_inches="tight")
    plt.close(fig)	 	 		  		  		    	 		 		   		 		  
  		  	   		 	 	 		  		  		    	 		 		   		 		  
def test_code():  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		 	 	 		  		  		    	 		 		   		 		  
    """  		  	   		 	 	 		  		  		    	 		 		   		 		  
    win_prob = 18/38  # set appropriately to the probability of a win  		  	   		 	 	 		  		  		    	 		 		   		 		  
    np.random.seed(gtid())  # do this only once  		  	   		 	 	 		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  		  	   		 	 	 		  		  		    	 		 		   		 		  
    # add your code here to implement the experiments
    
    episode_spins = 1000
    x = np.arange(0, 301)
    
    #Expriment 1, Figure 1
    times_1 = 10
    df1 = pd.DataFrame(np.nan, index=range(times_1), columns=range(episode_spins + 1), dtype=float)
    play_without_limit(df1, win_prob, episode_spins, times_1)
    df1 = df1.ffill(axis = 1)
    
    fig, ax = plt.subplots()
    ax.plot(x, df1.iloc[:, :301].T.values, linewidth = 1 )
    ax.set_title("Winnings for 10 Episodes")
    ax.set_xlabel("Spin Number")
    ax.set_ylabel("Winnings ($)")
    ax.set_xlim(0, 300)
    ax.set_ylim(-256, 100)
    plt.tight_layout()
    save_fig(fig, "E1F1.png")
 
    #Experiment 1, Figure 2
    times_2 = 1000
    df2 = pd.DataFrame(np.nan, index=range(times_2), columns=range(episode_spins + 1), dtype=float)
    play_without_limit(df2, win_prob, episode_spins, times_2)
    df2 = df2.ffill(axis = 1)
    
    mean = df2.mean(axis=0, skipna=True).values[:301]
    std = df2.std(axis=0, ddof=0, skipna=True).values[:301]
    median = df2.median(axis=0, skipna=True).values[:301]
    
    fig1, ax1 = plt.subplots()
    ax1.plot(x, mean, linewidth=2, label="Mean")
    ax1.plot(x, mean + std, "--", linewidth=1, label="Mean + 1σ")
    ax1.plot(x, mean - std, "--", linewidth=1, label="Mean - 1σ")
    ax1.set_title("Winnings without bankroll limit — Mean ± 1σ")
    ax1.set_xlabel("Spin Number")
    ax1.set_ylabel("Winnings ($)")
    ax1.set_xlim(0, 300)
    ax1.set_ylim(-256, 100)
    plt.tight_layout()
    ax1.legend()
    save_fig(fig1, "E1F2.png")
    

    #Experiment 1, Figure 3
    fig2, ax2 = plt.subplots()
    ax2.plot(x, median, linewidth=2, label="median")
    ax2.plot(x, median + std, "--", label="median + 1σ")
    ax2.plot(x, median - std, "--", label="median - 1σ")
    ax2.set_title("Winnings without bankroll limit — Median ± 1σ")
    ax2.set_xlabel("Spin Number")
    ax2.set_ylabel("Winnings ($)")
    ax2.set_xlim(0, 300)
    ax2.set_ylim(-256, 100)
    ax2.legend()
    save_fig(fig2, "E1F3.png")
      		 
       	   		 	 	 		  		  		    	 		 		   		 		  
  	#Expriment 2, Figure 1
    times = 1000
    df3 = pd.DataFrame(np.nan, index=range(times), columns=range(episode_spins + 1), dtype=float)
    play_with_limit(df3, win_prob, episode_spins, times)
    df3 = df3.ffill(axis = 1)
    mean = df3.mean(axis=0, skipna=True).values[:301]
    std = df3.std(axis=0, ddof=0, skipna=True).values[:301]
    median = df3.median(axis=0, skipna=True).values[:301]

    fig3, ax3 = plt.subplots()
    ax3.plot(x, mean, linewidth=1, label="Mean")
    ax3.plot(x, mean + std, "--", label="Mean + 1σ")
    ax3.plot(x, mean - std, "--", label="Mean - 1σ")
    ax3.set_title("Winnings with bankroll limit — Mean ± 1σ")
    ax3.set_xlabel("Spin Number")
    ax3.set_ylabel("Winnings ($)")
    ax3.set_xlim(0, 300)
    ax3.set_ylim(-256, 100)
    ax3.legend()
    plt.tight_layout()
    save_fig(fig3, "E2F1.png")

    
    #Experiment 2, Figure 2
    fig4, ax4 = plt.subplots()
    ax4.plot(x, median, linewidth=2, label="Median")
    ax4.plot(x, median + std, "--", label="Median + 1σ")
    ax4.plot(x, median - std, "--", label="Median - 1σ")
    ax4.set_title("Winnings with bankroll limit — Median ± 1σ")
    ax4.set_xlabel("Spin Number")
    ax4.set_ylabel("Winnings ($)")
    ax4.set_xlim(0, 300)
    ax4.set_ylim(-256, 100)
    ax4.legend()
    plt.tight_layout()
    save_fig(fig4, "E2F2.png")
 	   		 	 	 		  		  		    	 		 		   		 		  
	#questions
    p_1 = (df2.iloc[:, -1] == 80).mean()
    p_2 = (df3.iloc[:, -1] == 80).mean()
    ev_2 = df3.iloc[:, -1].mean()   
    print(p_1)
    print(p_2, ev_2)
    
    
if __name__ == "__main__":  		  	   		 	 	 		  		  		    	 		 		   		 		  
    test_code()  		  	   		 	 	 		  		  		    	 		 		   		 		  
