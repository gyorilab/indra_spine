#adding in adverbs and directions

noun_inputs = ("(medial|lateral|superior|posterior|dorsal|ipsilateral|efferent|outer|central|caudal|afferent|contralateral|ventral|frontal|"
	       "terminal|rostral|inner|anterior|ascending|peripheral|Descending|adjacent|secondary|afferent|auditory ascending|Afferent|"
	       "cortical|spinal|primary|sensory|motor|projection|visual|auditory|sensorimotor|basal|periaqueductal|limbic|tectal|dentate|"
	       "entorhinal|subcortical|somatosensory|olfactory|isthmic|cingulate|orbitofrontal|Intrahemispheric|geniculocortical|associational|"
	       "primary mechanosensory|organum|septal|Tectal|dense cortical|Cortical|mesopontine tegmental|primary trigeminal|hypoglossal|"
	       "occipital|parahippocampal|cerebellar|major|intramedullary|corticofugal|suprageniculate|parvocellular|paraventricular|"
	       "cortico/-/cortical|temporal|lateral nuclei|centralis|sympatho/-/excitatory reticulospinal|vestibulospinal|neocortical|"
	       "reticulospinal|retinofugal|subthalamic|contralateral homologous|neural|trigeminal|vagus|glossopharyngeal|preganglionic|"
	       "ophthalmic|vestibular primary|perirhinal|maxillar|postrhinal|intrahemispheric|pretectal|hypothalamic|Auditory|rubro/-/spinal|"
	       "posterolateral|reticulata|pre/-/frontal|preoptic|Pretectal|rubral|cortico/-/|mossy|Spinal|Retinal|amygdalostriatal|"
	       "interhemispheric|intercollicular|locus|Associational|lateralis|vestibular|caudolateral|multipolar|retinogeniculocortical)")


#add all noun cases to set, loop through, do either nouncase with np, np with nouncase, or nouncase with nouncase
#{}* ensures that advb or direction inserted is optional, includes cases where neither is found


noun_case_f = ["{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "both {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "both {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",              
	      "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])"]



phenotype_f = ["(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "both (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "both ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
              "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])"]

lemmas_br_br = "[lemma=project]|[lemma=connect]|[lemma=pathway]"
lemmas_br_ph = "[lemma=implicate]|[lemma=play]|[lemma=develop]|[lemma=involve]|[lemma=regulate]|[lemma=control]"
damage = "damage|loss of function|impairs|impairment|defect"
from_to_ph = "(>nmod_from)|(>nmod_of)|(>nmod_to)|(>nmod_in)|(>nmod_with)"
fromto = "(>nmod_from)|(>nmod_of)|(>nmod_to)"

#rule generation
def create_br_br_rules(br_rule1,br_rule2):

#    if br_rule1 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
#        entity1 = br_rule1.format(noun_inputs)
#    else:
#        entity1 = br_rule1.format(noun_inputs,noun_inputs)
#        
#    if br_rule2 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
#        entity2 = br_rule2.format(noun_inputs)
#    else:
#        entity2 = br_rule2.format(noun_inputs,noun_inputs)

    entity1 = br_rule1
    entity2 = br_rule2

    #create rules with whatever the current case is of each entity
    rule_set = ["{} {} {} {}".format(entity1,lemmas_br_br,fromto,entity2),
                "{} [] [] [] {} {} {}".format(entity1,lemmas_br_br,fromto,entity2),
                "{} >nmod_from {} >nmod_to {}".format(lemmas_br_br,entity1,entity2),
                "{} >nmod_of {} >nmod_with {}".format(lemmas_br_br,entity1,entity2),
                "{} [] [] [] [] {} >nmod_to {}".format(lemmas_br_br,entity1,entity2),
                "{} >nmod_to {} >nmod_from [] [] {}".format(lemmas_br_br,entity1,entity2),
                "{} [] [] [] {} {} {}".format(entity1,lemmas_br_br,fromto,entity2),
                "{} [lemma=afferent] {} {}".format(entity1,fromto,entity2),
                "{} which [] [] {} >nmod_to {}".format(entity1,lemmas_br_br,entity2)]
    return rule_set
     
def create_br_ph_rules(br_rule,ph_rule):

    if br_rule == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
        entity1 = br_rule.format(noun_inputs)
    else:
        entity1 = br_rule.format(noun_inputs,noun_inputs)

    entity2 = ph_rule

    #create rules with whatever the current case is of each entity
    rule_set = ["{}|{} [{}] {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,entity1,entity2),
                "{}|{} [] [] [] [{}] {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,entity1,entity2),
                "{}|{} [{}] {} {} {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,damage,from_to_ph,entity1,entity2),
                "{}|{} [] [] [] [{}] {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,entity1,entity2),
		"{}|{} [{}] [] [] [] {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,entity1,entity2),
		"{}|{} [] [] [] [{}] {} {} {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,damage,from_to_ph,entity1,entity2),    
                "{}|{} [{}] [] [] [] {} {} {} {}|{}".format(entity1,entity2,lemmas_br_ph,from_to_ph,damage,from_to_ph,entity1,entity2)]
    return rule_set
    

