import rule_run
import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as plt

def interaction_network():

    relations = rule_run.br_rules()
    ph_relations = rule_run.br_ph_rules()

    G = nx.Graph()
    plt.figure(figsize=(50, 50))
    G.add_edges_from(relations, len=4, color='red')
    G.add_edges_from(ph_relations, len=4, color='blue')

    edge_colors = [G.edges[edge]['color'] for edge in G.edges]

    pos = nx.nx_agraph.graphviz_layout(G, prog='neato')
    labels = {}
    for k in pos.keys():
        labels[k] = k[1]

    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='white',
                           node_shape='o')
    nx.draw_networkx_edges(G, pos, width=1.0, edge_color=edge_colors,
                           style='solid')
    labels = nx.draw_networkx_labels(G, pos, labels=labels, font_size=8,
                                     font_color='k', font_family='sans-serif',
                                     font_weight='normal')

def main():
    interaction_network()
    print()
    plt.savefig("X.pdf")

if __name__ == "__main__":
    main()