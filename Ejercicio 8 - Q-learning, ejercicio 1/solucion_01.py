import random

ROWS = 4
COLS = 12
S = (3, 0)
G = (3, 11)
ACTIONS = ["N", "E", "S", "W"]
DIR = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

ALPHA = 0.5
GAMMA = 1.0
EPSILON = 0.1
EPISODES = 500
MAX_STEPS = 200
SEED = 42


def init_q_table():
    q_table = {}
    for r in range(ROWS):
        for c in range(COLS):
            q_table[(r, c)] = {a: 0.0 for a in ACTIONS}
    return q_table


def get_next_state_and_reward(state, action):
    dr, dc = DIR[action]
    next_r, next_c = state[0] + dr, state[1] + dc

    if next_r < 0 or next_r >= ROWS or next_c < 0 or next_c >= COLS:
        return state, -1, False
    if next_r == 3 and 1 <= next_c <= 10:
        return S, -100, False
    if (next_r, next_c) == G:
        return G, -1, True

    return (next_r, next_c), -1, False


def choose_action(state, q_table, epsilon):
    if random.random() < epsilon:
        return random.choice(ACTIONS)
    max_q = max(q_table[state].values())
    best_actions = [a for a in ACTIONS if q_table[state][a] == max_q]
    return best_actions[0]


def train():
    random.seed(SEED)
    q_table = init_q_table()
    rewards_per_episode = []

    for ep in range(EPISODES):
        state = S
        total_reward = 0

        for step in range(MAX_STEPS):
            action = choose_action(state, q_table, EPSILON)
            next_state, reward, is_terminal = get_next_state_and_reward(state, action)
            total_reward += reward

            if is_terminal:
                max_next_q = 0.0
            else:
                max_next_q = max(q_table[next_state].values())

            q_table[state][action] += ALPHA * (
                reward + GAMMA * max_next_q - q_table[state][action]
            )
            state = next_state

            if is_terminal:
                break

        rewards_per_episode.append(total_reward)

    return q_table, rewards_per_episode


def evaluate(q_table):
    greedy_path = []
    state = S
    greedy_return = 0

    while state != G and len(greedy_path) < 20:
        action = choose_action(state, q_table, 0.0)
        greedy_path.append(action)
        state, reward, is_terminal = get_next_state_and_reward(state, action)
        greedy_return += reward

    return greedy_return, greedy_path


def build_policy_grid(q_table):
    policy_grid = []
    for r in range(ROWS):
        row_str = []
        for c in range(COLS):
            if (r, c) == S:
                row_str.append("S")
            elif (r, c) == G:
                row_str.append("G")
            elif r == 3 and 1 <= c <= 10:
                row_str.append("C")
            else:
                action = choose_action((r, c), q_table, 0.0)
                row_str.append(action)
        policy_grid.append(" ".join(row_str))
    return policy_grid


def calculate_moving_average(rewards, window=10):
    moving_avg = []
    for i in range(len(rewards)):
        if i < window:
            moving_avg.append(sum(rewards[: i + 1]) / (i + 1))
        else:
            moving_avg.append(sum(rewards[i - window + 1 : i + 1]) / window)
    return moving_avg


def main():
    q_table, rewards_per_episode = train()

    moving_avg = calculate_moving_average(rewards_per_episode)

    greedy_return, greedy_path = evaluate(q_table)
    policy_grid = build_policy_grid(q_table)

    print("Retorno Greedy:", greedy_return)
    print("Camino S -> G:", greedy_path)
    for row in policy_grid:
        print(row)


if __name__ == "__main__":
    main()
