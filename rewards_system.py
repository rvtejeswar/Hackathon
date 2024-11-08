import random

def reward_offline_engagement():
    rewards = ["Reward 1: Extra Playtime", "Reward 2: Family Game Night"]
    chosen_reward = random.choice(rewards)
    return {"reward": chosen_reward}
