import time
import matplotlib.pyplot as plt
import numpy as np
import random

class GlobalState:
    sim_days = 4*365 # simulation in a day 
    x=[]#days
    y=[] #create an array with Y 
    
    day_st = 1 
    day_now = 0 # current day 
    tokens_issued = 0 # in general amount of tokens
    tokens_burned = 0
    reward_now = 0
    reward_after_upd = 0
    fee_now = 10000
    tokens_now = 0
    epochs_passed = 0
    tokens_target = 100000000000 #(100 billion)
    
    def __init__(self): #create constructor 
        for i in range(1,self.sim_days): 
            self.x.append(i)  
    
def ref_model_ret(day_l, day, tok_todo,state:GlobalState): #day_f = stat.day_st  return amout of tokens per day
        return get_k(tok_todo, sum_seq(state.day_st, day_l)) / day # return amount of tokens per day 

    
def ref_model(day_l,day,state):#day_f = stat.day_st
    state.reward_after_upd = get_k(state.tokens_target,sum_seq(state.day_st, day_l)) / day #change reward
    state.reward_now = get_k(state.tokens_target,sum_seq(state.day_st, day_l)) / day

def simulation(state:GlobalState): 
    for j in range(1, state.sim_days): # tick days 
        # time.sleep(0.5)
        state.y.append(state.tokens_now) #recal array 
        recal(state,j) 

        print(j)

        print ("Token_issued:", state.tokens_issued)
        print ("Token_burned:", state.tokens_burned)
        print ("Reward_now:", state.reward_now)  
        print ("Reward_after:", state.reward_after_upd)          
        print ("Fee_now:", state.fee_now)
        print ("Epochs_passed:", state.epochs_passed)
        print ("Tokens_now:", state.tokens_now)
        print("todo: ", state.tokens_target)
        print ("-------------------------------")
    
# return sum of  sequence 1/n -> hyberbola
def sum_seq(first, second):
    s = 0  
    while first <= second: 
        hyperbola = 1 / first
        s += hyperbola
        first += 1
    return s 
print(sum_seq)
    
def get_k(tok_todo ,sum_seq):
    return tok_todo / sum_seq # return function of sum series 1/n 

def check_upd_reward(state:GlobalState,day_number):
    s_now = state.tokens_issued + ref_model_ret(state.sim_days, day_number, state.tokens_target, state)
    print(s_now) #amount of tokens should be issued 
    return s_now 

def recal(state:GlobalState,days):
    state.epochs_passed += 1*(60 * 24)
   # Simulate random transactions
    state.day_now +=1
    if state.day_now  > 10:
        burn = state.fee_now * random.randint(0, state.day_st * 1000)*(60*24)
        if (state.tokens_now - burn) < 0: 
            raise Exception("Tokens now reach 0")
        state.tokens_now -= burn
        state.tokens_burned += burn
        state.fee_now = 1

    should_be = check_upd_reward(state,days) # update check_reward

    state.tokens_now += state.reward_after_upd
    state.tokens_issued += state.reward_now
    ref_model(state.sim_days, days, state)

    if should_be > state.tokens_now:
        state.reward_after_upd +=(should_be - state.tokens_now)
        print(">", (should_be - state.tokens_now))
        
    if should_be < state.tokens_now:
        state.reward_after_upd -= (state.tokens_now - should_be)
        print("<", (state.tokens_now - should_be))

    

#create diagram           
st = GlobalState()
simulation(st)
print(recal)

plt.figure(figsize=(12, 7))
plt.title('Token Supply Model', fontsize=20, fontname='Times New Roman')

plt.xlabel('Days',color='gray')
plt.ylabel('Amount of Tokens ',color='gray')

plt.grid(True)#cell

plt.plot(st.x,st.y,'v-.g', label="tokens_now", mec='m', lw=1, mew=0.2, ms=8)
plt.legend()
plt.show()
