brain_regions = ["(?<region> ([entity=B-Spine] [entity=I-Spine]*))",
                "both (?<region> ([entity=B-Spine] [entity=I-Spine]*)) and"
                "[entity=B-Spine] [entity=I-Spine]*",
                "both [entity=B-Spine] [entity=I-Spine]* and (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*))",
                "(?<region> ([entity=B-Spine] [entity=I-Spine]*)) and "
                "[entity=B-Spine] [entity=I-Spine]*",
                "[entity=B-Spine] [entity=I-Spine]* and (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*))",
                "(?<region> ([entity=B-Spine] [entity=I-Spine]*))/,/ "
                "[entity=B-Spine] [entity=I-Spine]*",
                "[entity=B-Spine] [entity=I-Spine]*/,/ (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*))",
                "(?<region> ([entity=B-Spine] [entity=I-Spine]*))/,/ and "
                "[entity=B-Spine] [entity=I-Spine]*",
                "[entity=B-Spine] [entity=I-Spine]*/,/ and (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*))",
                "(?<region> [tag=JJ] [tag=JJ]* "
                "bank|formation|division|segment|half|portion|region of the "
                "[entity=B-Spine] [entity=I-Spine]*)",
                "(?<region> [tag=RB] [tag=RB]* "
                "bank|formation|division|segment|half|portion|region of the "
                "[entity=B-Spine] [entity=I-Spine]*)",
                "(?<region> ([entity=B-Spine] [entity=I-Spine]*))/,/ "
                "[entity=B-Spine] [entity=I-Spine]* and [entity=B-Spine] "
                "[entity=I-Spine]*",
                "(?<region> ([entity=B-Spine] [entity=I-Spine]*))/,/ "
                "[entity=B-Spine] [entity=I-Spine]*/,/ and [entity=B-Spine] "
                "[entity=I-Spine]*",
                "[entity=B-Spine] [entity=I-Spine]*/,/ [entity=B-Spine] "
                "[entity=I-Spine]* and (?<region> ([entity=B-Spine] "
                "[entity=I-Spine]*))",
                "[entity=B-Spine] [entity=I-Spine]*/,/ (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*)) and [entity=B-Spine] "
                "[entity=I-Spine]*",
                "[entity=B-Spine] [entity=I-Spine]*/,/ [entity=B-Spine] "
                "[entity=I-Spine]*/,/ and (?<region> ([entity=B-Spine] "
                "[entity=I-Spine]*))",
                "[entity=B-Spine] [entity=I-Spine]*/,/ (?<region> "
                "([entity=B-Spine] [entity=I-Spine]*))/,/ and [entity=B-Spine]"
                " [entity=I-Spine]*",
                "(?<region> area [entity=B-Spine] [entity=I-Spine]*)",
                "(?<region> Area [entity=B-Spine] [entity=I-Spine]*)"]

phenotypes = ["(?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)",
               "both (?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*) and [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*",
               "both [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]* and (?<phenotype> "
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*) and [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*",
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]* and (?<phenotype> "
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)/,/ [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*",
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*/,/ (?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)",
               "(?<phenotype> [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)/,/ and [entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*",
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*/,/ and (?<phenotype> "
               "[entity=B-NeuroBehavior] "
               "[entity=I-NeuroBehavior]*|[entity=B-Disease] "
               "[entity=I-Disease]*)",
               "(?<phenotype> [] disease)",
               "(?<phenotype> [] disorder)",
               "(?<phenotype> [] syndrome)",
               "(?<phenotype> []/'/s disease)"
               "(?<phenotype> [] /'/s disease)"]

lemmas_br_br = ("[lemma=project]|[lemma=connect]|[lemma=pathway]|"
                "[lemma=receive]|[lemma=innervate]|[lemma=originate]|"
                "[lemma=connection]|[lemma=projection]|[lemma=connectivity]")
lemmas_br_ph = ("[lemma=implicate]|[lemma=play]|[lemma=develop]|"
                "[lemma=involve]|[lemma=regulate]|[lemma=control]|"
                "[lemma=produce]")
damage = ("([lemma=damage]|loss of function|[lemma=impair]|[lemma=defect]"
             "|[lemma=destroy]|[lemma=destruct])")
fromto = "(>nmod_from)|(>nmod_of)|(>nmod_to)|(>nmod_in)|(>nmod_with)"
connection = ("cortical fibers|fiber|fibers|afferent|afferents|efferent"
                 "|efferents|neuron|neurons")


# Rule generation
def create_br_br_rules(br_rule1, br_rule2):
    """

    Parameters
    ----------
    br_rule1
    br_rule2

    This is called in the Rules notebook, which finds each permutation of the
    rules and plugs them back into this function
    Returns
    -------
    A set of rules for sentences describing brain region-brain region relations
    """

    entity1 = br_rule1
    entity2 = br_rule2

    # Create rules with whatever the current case is of each entity
    rule_set = ["{} {} {} {}".format(entity1, lemmas_br_br, fromto,
                                     entity2),
                "{} [] [] [] {} {} {}".format(entity1, lemmas_br_br,
                                              fromto, entity2),
                "{} >nmod_from {} >nmod_to {}".format(lemmas_br_br,
                                                      entity1, entity2),
                "{} >nmod_of {} >nmod_with {}".format(lemmas_br_br,
                                                      entity1, entity2),
                "{} [] [] [] [] {} >nmod_to {}".format(lemmas_br_br,
                                                       entity1, entity2),
                "{} >nmod_to {} >nmod_from [] [] {}".format(lemmas_br_br,
                                                            entity1, entity2),
                "{} [] [] [] {} {} {}".format(entity1, lemmas_br_br,
                                              fromto, entity2),
                "{} [lemma=afferent] {} {}".format(entity1, fromto,
                                                   entity2),
                "{} which [] [] {} >nmod_to {}".format(entity1,
                                                       lemmas_br_br, entity2),
                "{} []* [lemma=efferent] {} []* (?<region> [entity=B-Organ] "
                "[entity=I-Organ]*)".format(entity1, fromto),
                "[] (?<region> [entity=B-Organ] [entity=I-Organ]*) "
                "[lemma=afferent] {} {}".format(fromto, entity1),
                "{} []* [lemma=efferent] {} []* {}".format(entity1,
                                                           fromto, entity2),
                "[] {} [lemma=afferent] {} {}".format(entity1, fromto,
                                                      entity2),
                "{} {} {} [] [] {} {}".format(entity1, lemmas_br_br,
                                              fromto, fromto, entity2),
                "{} {} [] {} {}".format(entity1, lemmas_br_br, fromto,
                                        entity2),
                "{} {} input {} {}".format(entity1, lemmas_br_br, fromto,
                                           entity2),
                "{} has {} {} {}".format(entity1, lemmas_br_br, fromto,
                                         entity2),
                "{} {} {} {}".format(connection, lemmas_br_br, fromto,
                                     entity1, lemmas_br_br, fromto, entity2),
                "{} {} {} {} {}".format(entity1, lemmas_br_br,
                                        lemmas_br_br, fromto, entity2),
                "{} {} {} {} {}".format(lemmas_br_br, fromto, entity1,
                                        fromto, entity2),
                "{} {} {} {} {}".format(connection, fromto, entity1,
                                        fromto, entity2),
                "{} {} {} were {}".format(lemmas_br_br, fromto, entity1,
                                          entity2),
                "{} [lemma=show]|[lemma=demonstrate]|[lemma=display]|"
                "[lemma=suggest] {} {} {}".format(entity1, lemmas_br_br,
                                                  fromto, entity2),
                "{} {} {} [] and {}".format(entity1, lemmas_br_br,
                                            fromto, entity2),
                "{} {} {} {} [] []* and {}".format(lemmas_br_br, fromto,
                                                   entity1, fromto, entity2),
                "{} {} {} {} {}".format(entity1, lemmas_br_br,
                                        lemmas_br_br, fromto, entity2),
                "{} {} {} were {}".format(lemmas_br_br, fromto, entity1,
                                          entity2),
                "{} {} {} is|was|{} {}".format(connection, fromto,
                                               entity1, lemmas_br_br, entity2),
                "{} input {} {}".format(entity1, fromto, entity2)]
    return rule_set


def create_br_ph_rules(br_rule, ph_rule):
    """

    Parameters
    ----------
    br_rule
    ph_rule

    This is called in the Rules notebook, which finds each permutation of the
    rules and plugs them back into this function
    Returns
    -------
    A set of rules for sentences describing brain region-phenotype relations
    """

    entity1 = br_rule
    entity2 = ph_rule

    # Create rules with whatever the current case is of each entity
    rule_set = ["{} {} {} {}".format(entity1, lemmas_br_ph, fromto, entity2),
                "{} [] [] [] {} {} {}".format(entity1, lemmas_br_ph,
                                              fromto, entity2),
                "{} {} {} {}".format(entity1, lemmas_br_ph, fromto,
                                     entity2),
                "{} {} {} {}".format(entity2, lemmas_br_ph, fromto,
                                     entity1),
                "{} {} [] [] [] {} {}".format(entity1, lemmas_br_ph,
                                              fromto, entity2),
                "{} {} [] [] [] {} {}".format(entity2, lemmas_br_ph,
                                              fromto, entity1),
                "{} {} {} [] [] [] {}".format(entity1, lemmas_br_ph,
                                              fromto, entity2),
                "{} {} {} [] [] [] {}".format(entity2, lemmas_br_ph,
                                              fromto, entity1),
                "{} [] responsible for {}".format(entity1, entity2),
                "{}/,/ [] [] [] responsible for {}".format(entity1,
                                                           entity2),
                "{} is a structure {} {} {}".format(entity1,
                                                    lemmas_br_ph, fromto,
                                                    entity2),
                "{} is a region {} {} {}".format(entity1, lemmas_br_ph,
                                                 fromto, entity2),
                "{} {} {} {} {} {}".format(entity1, lemmas_br_ph, fromto,
                                           damage, fromto, entity2),
                "{} {} {} {} {} {}".format(entity2, lemmas_br_ph, fromto,
                                           damage, fromto, entity1),
                "{} {} {} {} {} {} {} {}".format(damage, fromto,
                                                 entity2, lemmas_br_ph, fromto,
                                                 damage, fromto,
                                                 entity1),
                "{} {} {} {} {} {} {} {}".format(damage, fromto,
                                                 entity1, lemmas_br_ph, fromto,
                                                 damage, fromto,
                                                 entity2),
                "{} [] [] [] {} {} {} {} {}".format(entity1,
                                                    lemmas_br_ph, fromto,
                                                    damage, fromto,
                                                    entity2),
                "{} [] [] [] {} {} {} {} {}".format(entity2, lemmas_br_ph,
                                                    fromto, damage, fromto,
                                                    entity1),
                "{} {} [] [] [] {} {} {} {}".format(entity1,
                                                    lemmas_br_ph, fromto,
                                                    damage, fromto,
                                                    entity2),
                "{} {} [] [] [] {} {} {} {}".format(entity2,
                                                    lemmas_br_ph, fromto,
                                                    damage, fromto,
                                                    entity1),
                "{} {} [] by {}".format(entity1, damage, entity2),
                "Brain {} {} {}".format(damage, fromto, entity1,
                                        lemmas_br_ph, fromto, entity2)]

    return rule_set
