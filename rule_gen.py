#adding in adverbs and directions
directions = ("(medial|lateral|superior|posterior|dorsal|ipsilateral|efferent|outer|central|caudal|afferent|contralateral|ventral|frontal|"              
"terminal|rostral|inner|anterior|ascending|peripheral|Descending|adjacent|secondary|afferent|auditory ascending|Afferent)")

advb = ("(cortical|spinal|primary|sensory|motor|projection|visual|auditory|sensorimotor|basal|periaqueductal|limbic|tectal|dentate|"
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

noun_case_f = ["{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "both {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "both {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType]) and (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType]) and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])/,/ {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])/,/ {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])/,/ and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])",
              "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])/,/ and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])"]


phenotype_f = ["(?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "both (?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease]) and ([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "both ([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease]) and (?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "(?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease]) and ([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease]) and (?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "(?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])/,/ ([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])/,/ (?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "(?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])/,/ and ([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])",
              "([chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])/,/ and (?<phenotype> [chunk=B-Disease]|[chunk=I-Disease]|[chunk=B-Disease][chunk=I-Disease])"]

#namedx_np_f = "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP])"
lemmas_br_br = ["project","connect","pathway"]
lemmas_br_ph = ["implicate","play","develop","involve","regulate","control"]
damage = ["damage","loss of function","impairs","impairment","defect"]
from_to_ph = [">nmod_from",">nmod_of",">nmod_to",">nmod_in",">nmod_with"]
fromto = [">nmod_from",">nmod_of",">nmod_to"]
#rule_combos = [namedx_np_f,noun_case_f]
noun_inputs = [directions,advb]


#rule generation
def create_br_br_rules(noun_type1,noun_input1,lemma,word,noun_type2,noun_input2):

    #fromto_portion = [">nmod_{}".format(word) for word in fromto]
    #lemma_portion = ["[lemma={}]".format(term) for term in lemmas]
    #entity_types = ['namedx','case']
    #create two word cases for BRs with noun_input of either advb or direction
    #entity1 = noun_type1
    #entity2 = noun_type2
   
    #if noun_type1 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP])":
    if noun_type1 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
        entity1 = noun_type1.format(noun_input1)
    else:
        entity1 = noun_type1.format(noun_input1,noun_input1)
        
    #if noun_type2 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP])":
    if noun_type2 == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
        entity2 = noun_type2.format(noun_input2)
    else:
        entity2 = noun_type2.format(noun_input2,noun_input2)

    #create rules with whatever the current case is of each entity
    rule_set = ["{} [lemma={}] {} {}".format(entity1,lemma,word,entity2),
                "{} [] [] [] [lemma={}] {} {}".format(entity1,lemma,word,entity2),
                "[lemma={}] >nmod_from {} >nmod_to {}".format(lemma,entity1,entity2),
                "[lemma={}] >nmod_of {} >nmod_with {}".format(lemma,entity1,entity2),
                "[lemma={}] [] [] [] [] {} >nmod_to {}".format(lemma,entity1,entity2),
                "[lemma={}] >nmod_to {} >nmod_from [] [] {}".format(lemma,entity1,entity2),
                "{} [] [] [] [lemma={}] {} {}".format(entity1,lemma,word,entity2),
                "{} [lemma=afferent] {} {}".format(entity1,word,entity2),
                "{} which [] [] [lemma={}] >nmod_to {}".format(entity1,lemma,entity2)]
    return rule_set
     
def create_br_ph_rules(region,noun_input,lemma,damage,word,phenotype):

    if region == "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[chunk=B-Organ]|[chunk=I-Organ]|[chunk=B-Organ][chunk=I-Organ]|[chunk=B-TissueType]|[chunk=I-TissueType]|[chunk=B-TissueType][chunk=I-TissueType])":
        entity1 = region.format(noun_input)
    else:
        entity1 = region.format(noun_input,noun_input)

    entity2 = phenotype

    #create rules with whatever the current case is of each entity
    rule_set = ["{}|{} [lemma={}] {} {}|{}".format(entity1,entity2,lemma,word,entity1,entity2),
                "{}|{} [] [] [] [lemma={}] {} {}|{}".format(entity1,entity2,lemma,word,entity1,entity2),
                "{}|{} [lemma={}] {} {} {} {}|{}".format(entity1,entity2,lemma,word,damage,word,entity1,entity2),
                "{}|{} [] [] [] [lemma={}] {} {}|{}".format(entity1,entity2,lemma,word,entity1,entity2),
		"{}|{} [lemma={}] [] [] [] {} {}|{}".format(entity1,entity2,lemma,word,entity1,entity2),
		"{}|{} [] [] [] [lemma={}] {} {} {} {}|{}".format(entity1,entity2,lemma,word,damage,word,entity1,entity2),    
                "{}|{} [lemma={}] [] [] [] {} {} {} {}|{}".format(entity1,entity2,lemma,word,damage,word,entity1,entity2)]
    return rule_set
    

