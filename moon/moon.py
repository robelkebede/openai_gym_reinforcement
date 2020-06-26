import numpy as np
import gym
import torch
from dqn.agent import Agent


ENV_NAME = 'LunarLander-v2'
#ENV_NAME = 'Humanoid-v2'


# Get the environment and extract the number of actions.
env = gym.make(ENV_NAME)
np.random.seed(123)
env.seed(123)
nb_actions = env.action_space.n
agent = Agent(state_size=8, action_size=4, seed=0)

agent.qnetwork_local.load_state_dict(torch.load('checkpoint.pth'))

for i in range(15):
    state = env.reset()
    for j in range(200):
        #action = agent.act(state)
        action = np.random.randint(0,6)
        env.render()
        state, reward, done, _ = env.step(action)
        if done:
            break 
    print("Iteration ",i)
            
env.close()



