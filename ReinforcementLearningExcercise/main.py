import numpy as np
import gym
import random
import matplotlib as mt
import pandas as pd
import plotly.express as px


def qlearning(learning_rate, discount_rate_set):
    # create Taxi environment
    env = gym.make("Taxi-v3", render_mode='ansi')

    # initialize q-table
    state_size = env.observation_space.n
    action_size = env.action_space.n
    qtable = np.zeros((state_size, action_size))

    # hyperparameters
    discount_rate = discount_rate_set
    epsilon = 1.0
    decay_rate = 0.005

    # training variables
    max_steps = 99  # per episode
    convergence_threshold = 1e-6
    episodes = 0
    has_converged = False

    while not has_converged:

        # reset the environment
        state, test = env.reset()
        done = False

        old_qtable = qtable.copy()

        for s in range(max_steps):

            # exploration-exploitation tradeoff
            if random.uniform(0, 1) < epsilon:
                # explore
                action = env.action_space.sample()
            else:
                # exploit
                action = np.argmax(qtable[state, :])

            # take action and observe reward
            new_state, reward, done, truncated, info = env.step(action)

            # Q-learning algorithm
            qtable[state, action] = qtable[state, action] + learning_rate * (
                    reward + discount_rate * np.max(qtable[new_state, :]) - qtable[state, action])

            # Update to our new state
            state = new_state

            # if done, finish episode
            if done == True:
                break

        # Decrease epsilon
        epsilon = np.exp(-decay_rate * episodes)

        # if the maximum difference between the old and new q-tables is less than the convergence threshold, we have converged
        max_difference = np.max(np.abs(old_qtable - qtable))
        if max_difference < convergence_threshold:
            has_converged = True

        episodes += 1

    # print(f"Q-table rows: {len(qtable)}")
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in qtable]))

    print(f"Training completed over {episodes} episodes")
    # input("Press Enter to watch trained agent...")

    # watch trained agent
    state, test = env.reset()
    done = False
    rewards = 0

    total_eps = 0
    for s in range(max_steps):

        # print(f"TRAINED AGENT")
        # print("Step {}".format(s + 1))

        action = np.argmax(qtable[state, :])
        new_state, reward, done, truncated, info = env.step(action)
        rewards += reward
        # print(env.render())  # print the new state
        # print(f"score: {rewards}")
        state = new_state

        total_eps = s
        if done == True:
            break

    env.close()
    return episodes


def main():
    data = []

    for i in range(1,10):
        print(i, " out of 9")
        for j in range(9):
            episodes = qlearning(0.1 * i, j * 0.1)
            data.append((0.1 * i, j * 0.1, episodes))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=["Learning rate (x)", "Discount rate (y)", "No. of Eps (z)"])

    # Export the DataFrame to a CSV file
    df.to_csv("qlearning_results.csv", index=False)

    df = pd.read_csv("qlearning_results.csv")

    # Create a 3D scatter plot
    fig = px.scatter_3d(df, x="Learning rate (x)", y="Discount rate (y)", z="No. of Eps (z)")

    # Show the plot
    fig.show()


if __name__ == "__main__":
    main()
