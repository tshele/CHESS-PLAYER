# CHESS-PLAYER

#GETTING STARTED

  
Introduction  
In this project, we use adversarial search techniques to build an agent to play knights Isolation.  In this Isolation Game, tokens move in L-shapes like Knights on chess game.   
   
 I have selected Option 3, using the Advanced Search Techniques.  The Baseline technique uses the MiniMax search algorithm and the advanced search algorithm it is compared to, is the Monte Carlo Tree Search algorithm.  
  
Baseline Results  
  
In the Baseline technique we used the MiniMax algorithm against a MiniMax opponent for a total of 100 games.  We used the fair game option for a fair comparison between the agents.  The Baseline MiniMax Custom player had a 50% success rate against the opponent MiniMax algorithm.  This result is expected because both algorithms were the same in this case.  
The charts below show the win counts and number of actions distribution for Baseline algorithm.  
   
  
The Monte Carlo Tree Search Algorithm  
  
The Monte Carlo Tree Search (MCTS) was implemented based on the pseudocode from the notes.  The opponent player used the MiniMax Algorithm as before.  
   
The charts below show the win counts and number of actions distribution for MCTS algorithm.  The MCTS algorithm had a 64% win ratio against the MiniMax algorithm.  This rate can be improved if more iterations were allowed, but it comes at the cost of increased processing time.  
   
Discussion on MCTS vs Baseline  
  
The MCTS algorithm had a 14% improvement over the MiniMax algorithm and this can be improved further by allowing more iterations.  What’s interesting about looking at the actions taken, the Baseline MiniMax algorithm seems to be more normally distributed, but the MCTS algorithm was able to win the game more often with fewer actions.  This shows that it has a more efficient exploration of the tree compared to the MiniMax algorithm.  The strength of the MCTS algorithm is that it simulates the remaining game based on a default policy.  Using the Upper Confidence Bound for Trees (UCT)as a sampling strategy we can avoid doing an exhaustive search of the search tree.  This allows us to sample more promising actions more often than other actions, thus producing a more efficient search result.  
