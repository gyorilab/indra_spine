# adding in adverbs and directions
noun_case_f = ["(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
               "both (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])) and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
               "both [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine] and (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
               "(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])) and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
               "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine] and (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
               "(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))/,/ [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
               "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
               "(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))/,/ and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
               "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ and (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
               "(?<region> [tag=JJ] [tag=JJ]* bank|formation|division|segment|half|portion|region of the [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])",
	           "(?<region> [tag=RB] [tag=RB]* bank|formation|division|segment|half|portion|region of the [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])",
	           "(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))/,/ [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine] and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
	           "(?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))/,/ [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
	           "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine] and (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
	           "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])) and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
	           "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ and (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))",
	           "[entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]/,/ (?<region> ([entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]))/,/ and [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine]",
	           "(?<region> area [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])",
	           "(?<region> Area [entity=B-Spine] [entity=I-Spine]+ | [entity=B-Spine])"]



phenotype_f = ["(?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)",
               "both (?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*) and [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*",
               "both [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]* and (?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*) and [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*",
               "[entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]* and (?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)/,/ [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*",
               "[entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*/,/ (?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)/,/ and [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*",
               "[entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*/,/ and (?<phenotype> [entity=B-NeuroBehavior] [entity=I-NeuroBehavior]*|[entity=B-Disease] [entity=I-Disease]*)",
               "(?<phenotype> [] disease)",
               "(?<phenotype> [] disorder)",
               "(?<phenotype> [] syndrome)",
               "(?<phenotype> []/'/s disease)"
               "(?<phenotype> [] /'/s disease)"]

lemmas_br_br = "[lemma=project]|[lemma=connect]|[lemma=pathway]|[lemma=receive]|[lemma=innervate]|[lemma=originate]"
lemmas_br_ph = "[lemma=implicate]|[lemma=play]|[lemma=develop]|[lemma=involve]|[lemma=regulate]|[lemma=control]|[lemma=produce]"
damage = "([lemma=damage]|loss of function|[lemma=impair]|[lemma=defect]|[lemma=destroy]|[lemma=destruct])"
fromto = "(>nmod_from)|(>nmod_of)|(>nmod_to)|(>nmod_in)|(>nmod_with)"
connection = "cortical fibers|fiber|fibers|afferent|afferents|efferent|efferents"

# rule generation
def create_br_br_rules(br_rule1, br_rule2):

    entity1 = br_rule1
    entity2 = br_rule2

    # create rules with whatever the current case is of each entity
    rule_set = ["{} {} {} {}".format(entity1, lemmas_br_br, fromto, entity2),
                "{} [] [] [] {} {} {}".format(entity1, lemmas_br_br, fromto, entity2),
                "{} >nmod_from {} >nmod_to {}".format(lemmas_br_br, entity1, entity2),
                "{} >nmod_of {} >nmod_with {}".format(lemmas_br_br, entity1, entity2),
                "{} [] [] [] [] {} >nmod_to {}".format(lemmas_br_br, entity1, entity2),
                "{} >nmod_to {} >nmod_from [] [] {}".format(lemmas_br_br, entity1, entity2),
                "{} [] [] [] {} {} {}".format(entity1, lemmas_br_br, fromto, entity2),
                "{} [lemma=afferent] {} {}".format(entity1, fromto, entity2),
                "{} which [] [] {} >nmod_to {}".format(entity1, lemmas_br_br, entity2),
                "{} []* [lemma=efferent] {} []* (?<region> [entity=B-Organ] [entity=I-Organ]*)".format(entity1, fromto),
                "[] (?<region> [entity=B-Organ] [entity=I-Organ]*) [lemma=afferent] {} {}".format(fromto, entity1),
                "{} []* [lemma=efferent] {} []* {}".format(entity1, fromto,entity2),
                "[] {} [lemma=afferent] {} {}".format(entity1,fromto, entity2),
                "{} {} {} [] [] {} {}".format(entity1, lemmas_br_br, fromto, fromto, entity2),
                "{} {} [] {} {}".format(entity1,lemmas_br_br,fromto, entity2),
		"{} {} input {} {}".format(entity1,lemmas_br_br,fromto,entity2),
		"{} has {} {} {}".format(entity1,lemmas_br_br,fromto,entity2),
		"{} {} {} {}".format(connection,lemmas_br_br,fromto,entity1,lemmas_br_br,fromto,entity2),
		"{} {} {} {} {}".format(entity1,lemmas_br_br,lemmas_br_br,fromto,entity2),
		"{} {} {} {} {}".format(lemmas_br_br,fromto,entity1,fromto,entity2),
		"{} {} {} {} {}".format(connection,fromto,entity1,fromto,entity2)]
    return rule_set


def create_br_ph_rules(br_rule, ph_rule):

    entity1 = br_rule
    entity2 = ph_rule

    # create rules with whatever the current case is of each entity
    rule_set_pos = ["{} {} {} {}".format(entity1, lemmas_br_ph, fromto, entity2),
                    "{} [] [] [] {} {} {}".format(entity1, lemmas_br_ph, fromto, entity2),
                    "{} {} {} {} {} {}".format(entity1, lemmas_br_ph, fromto, damage, fromto, entity2),
                    "{} {} {} {} {} {}".format(entity2, lemmas_br_ph, fromto, damage, fromto, entity1),
                    "{} {} {} {} {} {} {} {}".format(damage, fromto,entity2,lemmas_br_ph,fromto,damage,fromto,entity1),
                    "{} {} {} {} {} {} {} {}".format(damage,fromto,entity1,lemmas_br_ph,fromto,damage,fromto,entity2),
                    "{} {} {} {}".format(entity1, lemmas_br_ph, fromto, entity2),
                    "{} {} {} {}".format(entity2, lemmas_br_ph, fromto, entity1),
                    "{} {} [] [] [] {} {}".format(entity1, lemmas_br_ph, fromto, entity2),
                    "{} {} [] [] [] {} {}".format(entity2, lemmas_br_ph, fromto, entity1),
                    "{} {} {} [] [] [] {}".format(entity1, lemmas_br_ph, fromto, entity2),
                    "{} {} {} [] [] [] {}".format(entity2, lemmas_br_ph, fromto, entity1),
                    "{} [] [] [] {} {} {} {} {}".format(entity1, lemmas_br_ph, fromto, damage, fromto, entity2),
                    "{} [] [] [] {} {} {} {} {}".format(entity2, lemmas_br_ph, fromto, damage, fromto, entity1),
                    "{} {} [] [] [] {} {} {} {}".format(entity1, lemmas_br_ph, fromto, damage, fromto, entity2),
                    "{} {} [] [] [] {} {} {} {}".format(entity2, lemmas_br_ph, fromto, damage, fromto, entity1),
                    "{} [] responsible for {}".format(entity1, entity2),
                    "{}/,/ [] [] [] responsible for {}".format(entity1, entity2),
                    "{} is a structure {} {} {}".format(entity1,lemmas_br_ph,fromto,entity2),
                    "{} is a region {} {} {}".format(entity1,lemmas_br_ph,fromto,entity2),
		            "{} {} [] by {}".format(entity1,damage,entity2),
		            "Brain {} {} {}".format(damage,fromto,entity1,lemmas_br_ph,fromto,entity2)]

    return rule_set_pos
