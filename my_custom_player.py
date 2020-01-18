#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sample_players import DataPlayer



#from sample_players import RandomPlayer, GreedyPlayer, MinimaxPlayer



import random



#import minimax



#from mcts import mcts







class CustomPlayer_Baseline(DataPlayer):



    """ Implement your own agent to play knight's Isolation







    The get_action() method is the only required method for this project.



    You can modify the interface for get_action by adding named parameters



    with default values, but the function MUST remain compatible with the



    default interface.







    **********************************************************************



    NOTES:



    - The test cases will NOT be run on a machine with GPU access, nor be



      suitable for using any other machine learning techniques.







    - You can pass state forward to your agent on the next turn by assigning



      any pickleable object to the self.context attribute.



    **********************************************************************



    """



    def get_action(self, state):



        """ Employ an adversarial search technique to choose an action



        available in the current state calls self.queue.put(ACTION) at least







        This method must call self.queue.put(ACTION) at least once, and may



        call it as many times as you want; the caller will be responsible



        for cutting off the function after the search time limit has expired.







        See RandomPlayer and GreedyPlayer in sample_players for more examples.







        **********************************************************************



        NOTE: 



        - The caller is responsible for cutting off search, so calling



          get_action() from your own code will create an infinite loop!



          Refer to (and use!) the Isolation.play() function to run games.



        **********************************************************************



        """



        # TODO: Replace the example implementation below with your own search



        #       method by combining techniques from lecture



        #



        # EXAMPLE: choose a random move without any search--this function MUST



        #          call self.queue.put(ACTION) at least once before time expires



        #          (the timer is automatically managed for you)



        



        #import random



        #self.queue.put(random.choice(state.actions()))



        #self.queue.put(max(state.actions(), key=lambda x: self.score(state.result(x))))  



        #MinimaxPlayer.get_action(self, state)



        """



        Using Minmax from lecture notes as baseline



        """



        if state.ply_count < 2:



            self.queue.put(random.choice(state.actions()))



        else:



            self.queue.put(self.minimax(state, depth=3))







    def minimax(self, state, depth):







        def min_value(state, depth):



            if state.terminal_test(): return state.utility(self.player_id)



            if depth <= 0: return self.score(state)



            value = float("inf")



            for action in state.actions():



                value = min(value, max_value(state.result(action), depth - 1))



            return value







        def max_value(state, depth):



            if state.terminal_test(): return state.utility(self.player_id)



            if depth <= 0: return self.score(state)



            value = float("-inf")



            for action in state.actions():



                value = max(value, min_value(state.result(action), depth - 1))



            return value







        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1))







    def score(self, state):



        own_loc = state.locs[self.player_id]



        opp_loc = state.locs[1 - self.player_id]



        own_liberties = state.liberties(own_loc)



        opp_liberties = state.liberties(opp_loc)



        return len(own_liberties) - len(opp_liberties)







class CustomPlayer_MCTS(DataPlayer):



    """ 



    **********************************************************************



    This MCTS Agent was NOT used and is NOT working.



    **********************************************************************



    """



    def getPossibleActions(self):  



        return state.actions()



    



    def takeAction(self, action):



        return state.result(action)



        



    def isTerminal(self):



        return state.terminal_test()       



  



    def score(self, state):



        own_loc = state.locs[self.player_id]



        opp_loc = state.locs[1 - self.player_id]



        own_liberties = state.liberties(own_loc)



        opp_liberties = state.liberties(opp_loc)



        return len(own_liberties) - len(opp_liberties)







    def getReward(self):



        #return self.utility(self.player_id)



        return self.score(state)



    



    def get_action(self, state):



        """ Employ an adversarial search technique to choose an action



        available in the current state calls self.queue.put(ACTION) at least







        This method must call self.queue.put(ACTION) at least once, and may



        call it as many times as you want; the caller will be responsible



        for cutting off the function after the search time limit has expired.









        **********************************************************************



        NOTE: 



        - The caller is responsible for cutting off search, so calling



          get_action() from your own code will create an infinite loop!



          Refer to (and use!) the Isolation.play() function to run games.



        **********************************************************************



        """



        # TODO: Replace the example implementation below with your own search



        #       method by combining techniques from lecture



        #



        # EXAMPLE: choose a random move without any search--this function MUST



        #          call self.queue.put(ACTION) at least once before time expires



        #          (the timer is automatically managed for you)



        



        #import random



        #self.queue.put(random.choice(state.actions()))



        #self.queue.put(max(state.actions(), key=lambda x: self.score(state.result(x))))  



        #MinimaxPlayer.get_action(self, state)            







            



            



        mcts_root = mcts(self)



        bestAction = mcts_root.search(state)



        self.queue.put(bestAction)







C = 1.0



iter_limit = 80







class CustomPlayer_MCTS2(DataPlayer):



    """



    Implementing Monte Carlo Tree Search from algorithm in notes



    """



    



    def uct_search(self, state):



        root = MCTS_Node(state)



        if root.state.terminal_test():



            return random.choice(state.actions())



        for _ in range(iter_limit):



            child = tree_policy(root)



            if not child:



                continue



            reward = default_policy(child.state)



            backup_negamax(child, reward)







        idx = root.children.index(best_child(root))



        return root.children_actions[idx]







    def get_action(self, state):



        if state.ply_count < 2:



            self.queue.put(random.choice(state.actions()))



        else:



            self.queue.put(self.uct_search(state))











import random, math, copy











class MCTS_Node():



    def __init__(self, state, parent=None):



        self.visits = 1



        self.reward = 0.0



        self.state = state



        self.children = []



        self.children_actions = []



        self.parent = parent







    def add_child(self, child_state, action):



        child = MCTS_Node(child_state, self)



        self.children.append(child)



        self.children_actions.append(action)







    def update(self, reward):



        self.reward += reward



        self.visits += 1







    def fully_expanded(self):



        return len(self.children_actions) == len(self.state.actions())







def tree_policy(node):



    while not node.state.terminal_test():



        if not node.fully_expanded():



            return expand(node)



        node = best_child(node)



    return node











def expand(node):



    tried_actions = node.children_actions



    legal_actions = node.state.actions()



    untried_actions = [action for action in legal_actions if action not in tried_actions]



    for action in untried_actions:



        new_state = node.state.result(action)



        node.add_child(new_state, action)



        return node.children[-1]











def best_child(node):



    best_score = float("-inf")



    best_children = []



    for child in node.children:



        QoN = child.reward / child.visits



        sample = math.sqrt(2.0 * math.log(node.visits) / child.visits)



        score = QoN + C * sample



        if score == best_score:



            best_children.append(child)



        elif score > best_score:



            best_children = [child]



            best_score = score



    return random.choice(best_children)











def default_policy(state):



    init_state = copy.deepcopy(state)



    while not state.terminal_test():



        action = random.choice(state.actions())



        state = state.result(action)



    if state._has_liberties(init_state.player()):



        return -1



    else:



        return 1











def backup_negamax(node, reward):



    while node != None:



        node.update(reward)



        node = node.parent



        reward *= -1







#CustomPlayer = CustomPlayer_Baseline



CustomPlayer = CustomPlayer_MCTS2 

