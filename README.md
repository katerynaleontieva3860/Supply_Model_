# Token Supply Model 
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Terminology
 * Simulation
 * Techologes
 * Libraries
 * Authors
 * License
 
## Introdoction
This simulation predict issue tokens  as close to a linear function as possible - from 0 to 100 billion, in 4 years.
Our goal release 10 billions tokens for period of 1460 days.


## Why do we need this simulation?

* We have presented a simulation of the release of tokens for 4 years for investors in order to ensure a sufficient number of tokens for payments so that neither side suffers losses
## Terminology
## What is Epoch ?

* Every tick, the "Epoch" event occurs.

## What is TokensNow?

* Amount of tokens in the system in the current moment.

## What is TokenIssued?

* Amount of tokens which must be issued in a certain day 

## What  is TokenBurned?
* Amount of tokens which should burned due to transaction fee

## What is TokenShouldBe
* Amount of tokens which we must have for 4 years 

## Simulation
How is the simulation going ?

## Initial configurable state of simulation: 
Simitation of tokens run with a 1 minute tick of epoch 
Notice, that every tick, the "Epoch" event occurs.
Each Age, 100 transactions occur.
-- Const FEE * amountOfTransactions burned

Futhermore,every Age, tokens are created, equal to the REWARD variable
When tokens are burned and created in the system, we update the GlobalState variables:
* TokensIssued
* TokensBurned
* TokensNow

Every 24 hours (24 * 60 ticks) the REWARD variable is recalculated.
## Visualisation 
We made calculation and present our results in the Token Supply plot.
Also, we used simple mathematic function - hyperbola to made supply simulation.
## Our plot consist of :
* X-axis - Amout of days - 1460 
* Y- axis - Amout of Tokens in the system - 10 bil
Futhermore, we made output of statistics every recalculation:
*Released tokens
*Burned tokens
*Tokens now
*Tokens should be
 
You can familiarize yourself with our conclusions as soon as you run the code and look at the graph of the function
 

## Techologes:
* Let's write down the languages we used, the libraries and its versions:
## Language:
* Python 3.9
## Libraries:
* import time 
---  pip3 install time
* import matplotlib.pyplot as plt
--- pip3 install matplotlib
* import numpy as np
--- pip3 install numpy
* import random
--- pip3 install random



## Authors
Kateryna Leontieva - work on Token Suppply  model simulation 


## License
This project is licensed under the MIT License - see the LICENSE.md file for details





