from itertools import product

def load_sentence_pieces(file_path):
    pieces = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line by the '=' character to get name and string
            if '=' in line:
                name, string = line.strip().split('=', 1)
                pieces[name] = string.strip()
    return pieces

def load_entities(file_path):
    lists = {}
    current_list_name = None

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                # Start of a new list
                current_list_name = line[1:-1]
                lists[current_list_name] = []
            elif current_list_name:
                # Add item to the current list
                lists[current_list_name].append(line)

    return lists

def load_rules(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def assemble_rules(entity1, entity2):

    #Generate all variables
    pieces = load_sentence_pieces('sentence_pieces.txt')

    lemmas_br_br = pieces['lemmas_br_br']
    lemmas_br_ph = pieces['lemmas_br_ph']
    damage = pieces['damage']
    fromto = pieces['fromto']
    connection = pieces['connection']

    br_template = load_rules('br_br.txt')
    ph_template = load_rules('br_ph.txt')

    br_br = [
        rule.format(entity1=entity1, lemmas_br_br=lemmas_br_br,
                                    fromto=fromto, entity2=entity2,
                                    damage=damage, connection=connection)
        for rule in br_template]

    br_ph = [
        rule.format(entity1=entity1, lemmas_br_ph=lemmas_br_ph,
                                    fromto=fromto, entity2=entity2,
                                    damage=damage, connection=connection)
        for rule in ph_template]
    return br_br, br_ph
def permutations():
    entities = load_entities('entities.txt')

    brain_regions = entities['brain_regions']
    phenotypes = entities['phenotypes']

    rules = {'br': [], 'ph': []}

    for br_1, br_2 in product(brain_regions, brain_regions):
        br_version = assemble_rules(br_1, br_2)[0]
        for rule in br_version:
            rules['br'].append(rule)

    for br, ph in product(brain_regions, phenotypes):
        ph_version = assemble_rules(br, ph)[1]
        for rule in ph_version:
            rules['ph'].append(rule)

    return rules

def main():

   print(permutations()['br'][0:30])
   print(len(permutations()['br']))
   print(permutations()['ph'][0:30])
   print(len(permutations()['ph']))

if __name__ == "__main__":
    main()