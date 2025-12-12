
from tqdm import tqdm

def count_paths(source, dest, edges_mapping, rev_nodes, dp):
    # print(source, dest)
    print(rev_nodes[source], rev_nodes[dest])
    if source == dest:
        return 1
    ans = 0
    key = (source, dest)
    if key in dp:
        return dp[key]
    for edge in edges_mapping[source]:
        if edge != source:
            ans += count_paths(edge, dest, edges_mapping, rev_nodes, dp)
    dp[key] = ans
    return ans
def main_1():

    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        total_ans = 0
        nodes = {}
        edges_mapping = {}
        ind = 0
        for line in lines:
            toks = line[:-1].split(": ")
            source = toks[0]
            if source not in nodes:
                nodes[source] = ind
                edges_mapping[ind] = []
                ind += 1
            for dest in toks[1].split(" "):
                # print(dest)
                if dest not in nodes:
                    nodes[dest] = ind
                    edges_mapping[ind] = []
                    ind += 1
                    
                edges_mapping[nodes[source]].append(nodes[dest])
        
        # print(nodes)
        rev_nodes = {}
        for key in nodes:
            rev_nodes[nodes[key]] = key
        # print(rev_nodes)
        # print(edges_mapping)
        ans = count_paths(nodes["svr"], nodes["fft"], edges_mapping, rev_nodes, {})
        ans *= count_paths(nodes["fft"], nodes["dac"], edges_mapping, rev_nodes, {})
        ans *= count_paths(nodes["dac"], nodes["out"], edges_mapping, rev_nodes, {})
        print(ans)
def main():

    with open('input.txt', 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
if __name__ == "__main__":
    main_1()

                
                
                
                
