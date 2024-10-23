import os

import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as plt

from rule_run import br_rules, br_ph_rules


def interaction_network(term):
    """Returns a network of brain region-brain region and brain region-phenotype"""

    relations = br_rules()
    ph_relations = br_ph_rules()

    # TODO: configurable file path for this?
    os.makedirs(term + '_network', exist_ok=True)
    os.chdir(term + '_network')

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

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # TODO: configurable file path for this file?
    with open('relation_information.txt', 'w') as file:
        file.write('Number of brain region-brain region relations: ' +
                   str(len(relations)))
        file.write('Number of brain region-phenotype relations: ' +
                   str(len(ph_relations)))
        file.write('Number of nodes: ' + str(num_nodes))
        file.write('Number of edges: ' + str(num_edges))

    plt.savefig(f'{term}_network.png', format='PNG')
    plt.close()

    plt.savefig(f'{term}_network.pdf', format='PDF')
    plt.close()


# TODO: is the main needed?
def main():
    interaction_network()
    print()
    # TODO: can X.pdf be something customizable?
    plt.savefig("X.pdf")


if __name__ == "__main__":
    main()
