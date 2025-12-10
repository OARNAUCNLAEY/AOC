
from tqdm import tqdm

def make_bitmask_machine(tok):
    val = 0
    ind = 0
    for i in tok[1:-1]:
        if i == "#":
            val += 2**ind   
        ind += 1
    return val
def make_bitmask_button(tok):
    val = 0
    button_ind = tok[1:-1].split(",")
    for ind in button_ind:
        val += 2**(int(ind))
    return val
import numpy as np
def make_vector_machine(tok):
    val = []
    for i in tok[1:-1].split(","):
        val.append(int(i))   
    return np.array(val)
def make_vector_button(tok, total_len):
    val = [0]*total_len
    button_ind = tok[1:-1].split(",")
    for ind in button_ind:
        val[int(ind)] += 1
    return np.array(val)


def main_1():

    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        total_ans = 0
        for line in lines:
            tokens = line[:-1].split(" ")
            actions = []
            configuration = make_bitmask_machine(tokens[0])
            total_buttons = len(tokens[0]) - 2
            for tok in tokens[1:]:
                if tok[0] == "{":
                    break
                actions.append(make_bitmask_button(tok))
            print(actions)
            ans = 10**8
            for i in range(2**(len(actions))):
                # print(f"Trying combination {i}")
                state = 0
                cnt = 0
                for j in range(len(actions)):
                    if ((2**j) & i) > 0:
                        # print(j, j << 2, "try", actions[j])
                        state = state ^ actions[j]
                        cnt += 1
                # print(state, configuration)
                if state == configuration:
                    ans = min(ans, cnt)
            print(ans)
            total_ans += ans
        print(total_ans)
def main():

    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        total_ans = 0
        for line in lines:
            tokens = line[:-1].split(" ")
            actions = []
            configuration = None
            total_buttons = len(tokens[0]) - 2
            for tok in tokens[1:]:
                if tok[0] == "{":
                    configuration = make_vector_machine(tok)
                    break
                actions.append(make_vector_button(tok, total_buttons))
            A = np.array(actions).transpose()
            from scipy.optimize import milp, LinearConstraint, Bounds
            integrality = np.ones(len(actions), dtype=bool)
            c_obj = np.ones(len(actions), dtype=float)
            bounds = Bounds(np.zeros(len(actions)), np.full(len(actions), np.inf))
            constraints = LinearConstraint(A, configuration, configuration)
            res = milp(
                c=c_obj,
                constraints=constraints,
                integrality=integrality,
                bounds = bounds,
            )
            print("Status:", res.message)
            print("Optimal ci:", res.x)
            total_ans += np.sum(res.x)
        print(total_ans)         
if __name__ == "__main__":
    main()

                
                
                
                
