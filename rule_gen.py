# adding in adverbs and directions
'''
noun_inputs_raw = (
    "medial|lateral|superior|posterior|dorsal|ipsilateral|efferent|outer|central|caudal|afferent|contralateral|ventral|frontal|"
    "terminal|rostral|inner|anterior|ascending|peripheral|Descending|adjacent|secondary|afferent|auditory ascending|Afferent|"
    "cortical|spinal|primary|sensory|motor|projection|visual|auditory|sensorimotor|basal|periaqueductal|limbic|tectal|dentate|"
    "entorhinal|subcortical|somatosensory|olfactory|isthmic|cingulate|orbitofrontal|Intrahemispheric|geniculocortical|associational|"
    "primary mechanosensory|organum|Tectal|dense cortical|Cortical|mesopontine tegmental|primary trigeminal|hypoglossal|"
    "occipital|parahippocampal|cerebellar|major|intramedullary|corticofugal|suprageniculate|parvocellular|paraventricular|"
    "cortico/-/cortical|temporal|lateral nuclei|centralis|sympatho/-/excitatory reticulospinal|vestibulospinal|neocortical|"
    "reticulospinal|retinofugal|subthalamic|contralateral homologous|neural|trigeminal|vagus|glossopharyngeal|preganglionic|"
    "ophthalmic|vestibular primary|perirhinal|maxillar|postrhinal|intrahemispheric|pretectal|hypothalamic|Auditory|rubro/-/spinal|"
    "posterolateral|reticulata|pre/-/frontal|preoptic|Pretectal|rubral|cortico/-/|mossy|Spinal|Retinal|amygdalostriatal|"
    "interhemispheric|intercollicular|locus|Associational|lateralis|vestibular|caudolateral|multipolar|retinogeniculocortical|thalamic|"
    "facial|caudal|septal|medial septal|dorsal septal|olfactory|gustatory|frontal|frontostriatal|central|posterior|central posterior|mediodorsal|"
    "mediodorsal thalamic|geniculate|medio/-/|thalamo/-/|tegmental")


'''
# add all noun cases to set, loop through, do either nouncase with np, np with nouncase, or nouncase with nouncase
# {}* ensures that advb or direction inserted is optional, includes cases where neither is found

'''
noun_case_f = [
    "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and {}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* ([chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and {}* (?<region> [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> {}* [])",
    "(?<region> {}* [] [])",
    "(?<region> {}* [chunk=B-NP]|[chunk=I-NP]|[chunk=B-NP][chunk=I-NP])"]
'''
'''
noun_case_f = [
    "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both (?<region>  {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both {}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and {}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ {}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ (?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and {}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "{}* {}* {}* ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and (?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> {}+ {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])"]
'''
'''
noun_case_f = [
    "(?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both (?<region>  [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "both ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and ([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "([entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
    "(?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])"]
'''

'''
noun_case_f = [
    "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "both (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "both ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
    "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])"]
'''

'''
noun_case_f = ["(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "both (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "both ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType]) and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "(?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and ([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])",
               "([entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])/,/ and (?<region> [entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])"]
'''
'''
noun_case_f = ["(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "both (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "both ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])/,/ and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]|[entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])"]
'''

noun_case_f = ["(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "both (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]) and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "both ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]) and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]) and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine]) and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])/,/ ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])/,/ (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "(?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])/,/ and ([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "([entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])/,/ and (?<region> [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])",
               "(?<region> [tag=JJ] formation|division|segment|half|portion of the [entity=B-Spine]|[entity=I-Spine]|[entity=B-Spine][entity=I-Spine])"]


phenotype_f = ["(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "both (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "both ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease]) and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "(?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ and ([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "([entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])/,/ and (?<phenotype> [entity=B-Disease]|[entity=I-Disease]|[entity=B-Disease][entity=I-Disease])",
               "(?<phenotype> [] disease)",
               "(?<phenotype> [] disorder)",
               "(?<phenotype> [] syndrome)",
               "(?<phenotype> [] /'/s disease)"]

lemmas_br_br = "[lemma=project]|[lemma=connect]|[lemma=pathway]"
# lemmas_br_br = r"[lemma=project]|[lemma=connect]|[lemma=pathway]"
lemmas_br_ph = "[lemma=implicate]|[lemma=play]|[lemma=develop]|[lemma=involve]|[lemma=regulate]|[lemma=control]"
damage = "(damage|loss of function|impairs|impairment|defect)+"
from_to_ph = "(>nmod_from)|(>nmod_of)|(>nmod_to)|(>nmod_in)|(>nmod_with)"
fromto = "(>nmod_from)|(>nmod_of)|(>nmod_to)"


# fromto = "(>nmod_from)|(>nmod_of)|(>nmod_to)"

# rule generation
def create_br_br_rules(br_rule1, br_rule2):
    '''
    noun_inputs = "((amod_"
    for char in noun_inputs_raw:
        if char == "|":
            noun_inputs += ")|(amod_"
        else:
            noun_inputs += char
    noun_inputs += ")|"
    noun_inputs += noun_inputs_raw
    noun_inputs += ")"
    if br_rule1 == "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity1 = br_rule1.format(noun_inputs, noun_inputs, noun_inputs)
    elif br_rule1 == "(?<region> {}+ {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity1 = br_rule1.format(noun_inputs, noun_inputs, noun_inputs, noun_inputs)
    else:
        entity1 = br_rule1.format(noun_inputs,noun_inputs,noun_inputs,noun_inputs,noun_inputs,noun_inputs)

    if br_rule2 == "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity2 = br_rule2.format(noun_inputs, noun_inputs, noun_inputs)
    elif br_rule2 == "(?<region> {}+ {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity2 = br_rule2.format(noun_inputs,noun_inputs,noun_inputs,noun_inputs)
    else:
        entity2 = br_rule2.format(noun_inputs,noun_inputs,noun_inputs,noun_inputs,noun_inputs,noun_inputs)
    '''
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
                "{} []* [lemma=efferent] {} []* (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ])".format(entity1, fromto),
                "[] (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]) [lemma=afferent] {} {}".format(fromto, entity1),
                "{} {} {} [] [] {} {}".format(entity1, lemmas_br_br, fromto, fromto, entity2)]
    return rule_set


def create_br_ph_rules(br_rule, ph_rule):
    '''
    noun_inputs = ""
    for char in noun_inputs_raw:
        if char == "|":
            noun_inputs += ")|(amod_"
        else:
            noun_inputs += char
    if br_rule == "{}* {}* {}* (?<region> [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])" or br_rule == "(?<region> {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity1 = br_rule.format(noun_inputs, noun_inputs, noun_inputs)
    elif br_rule == "(?<region> {}+ {}* {}* {}* [entity=B-Organ]|[entity=I-Organ]|[entity=B-Organ][entity=I-Organ]|[entity=B-TissueType]|[entity=I-TissueType]|[entity=B-TissueType][entity=I-TissueType])":
        entity1 = br_rule.format(noun_inputs, noun_inputs, noun_inputs, noun_inputs)
    else:
        entity1 = br_rule.format(noun_inputs, noun_inputs, noun_inputs, noun_inputs, noun_inputs, noun_inputs)
    '''
    entity1 = br_rule
    entity2 = ph_rule

    # create rules with whatever the current case is of each entity
    rule_set_pos = ["{} {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, entity2),
                    "{} [] [] [] {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, entity2),
                    "{} {} {} {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity2),
                    "{} {} {} {} {} {}".format(entity2, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity1),
                    "{} {} {} {} {} {} {} {}".format(damage, from_to_ph,entity2,lemmas_br_ph,from_to_ph,damage,from_to_ph,entity1),
                    "{} {} {} {} {} {} {} {}".format(damage,from_to_ph,entity1,lemmas_br_ph,from_to_ph,damage,from_to_ph,entity2),
                    "{} {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, entity2),
                    "{} {} {} {}".format(entity2, lemmas_br_ph, from_to_ph, entity1),
                    "{} {} [] [] [] {} {}".format(entity1, lemmas_br_ph, from_to_ph, entity2),
                    "{} {} [] [] [] {} {}".format(entity2, lemmas_br_ph, from_to_ph, entity1),
                    "{} {} {} [] [] [] {}".format(entity1, lemmas_br_ph, from_to_ph, entity2),
                    "{} {} {} [] [] [] {}".format(entity2, lemmas_br_ph, from_to_ph, entity1),
                    "{} [] [] [] {} {} {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity2),
                    "{} [] [] [] {} {} {} {} {}".format(entity2, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity1),
                    "{} {} [] [] [] {} {} {} {}".format(entity1, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity2),
                    "{} {} [] [] [] {} {} {} {}".format(entity2, lemmas_br_ph, from_to_ph, damage, from_to_ph, entity1),
                    "{} [] responsible for {}".format(entity1, entity2),
                    "{}/,/ [] [] [] responsible for {}".format(entity1, entity2),
                    "{} is a structure {} {} {}".format(entity1,lemmas_br_ph,from_to_ph,entity2),
                    "{} is a region {} {} {}".format(entity1,lemmas_br_ph,from_to_ph,entity2)]

    return rule_set_pos
