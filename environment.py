import gym


def create_env():
    env = gym.make('CartPole-v0')
    return env