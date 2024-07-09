import itertools
import pandas as pd

adjectives = ['medial','lateral','superior','posterior','dorsal','ipsilateral','efferent','outer','central','caudal',
              'afferent','contralateral','ventral','frontal','terminal','rostral','inner','anterior','ascending',
              'peripheral','Descending','adjacent','secondary','afferent','auditory ascending','Afferent','cortical',
              'spinal','primary','sensory','motor','projection','visual','auditory','sensorimotor','basal',
              'periaqueductal','limbic','tectal','dentate','entorhinal','subcortical','somatosensory','olfactory',
              'isthmic','cingulate','orbitofrontal','Intrahemispheric','geniculocortical','associational',
              'primary mechanosensory','organum','Tectal','dense cortical','Cortical','mesopontine tegmental',
              'primary trigeminal','hypoglossal','occipital','parahippocampal','cerebellar','major','intramedullary',
              'corticofugal','suprageniculate','parvocellular','paraventricular','cortico/-/cortical','temporal',
              'lateral nuclei','centralis','sympatho/-/excitatory reticulospinal','vestibulospinal','neocortical|',
              'reticulospinal','retinofugal','subthalamic','contralateral homologous','neural','trigeminal','vagus',
              'glossopharyngeal','preganglionic','ophthalmic','vestibular primary','perirhinal','maxillar','postrhinal',
              'intrahemispheric','pretectal','hypothalamic','Auditory','rubro/-/spinal|','posterolateral','reticulata',
              'pre/-/frontal','preoptic','Pretectal','rubral','cortico/-/','mossy','Spinal','Retinal','amygdalostriatal',
              'interhemispheric','intercollicular','locus','Associational','lateralis','vestibular','caudolateral',
              'multipolar','retinogeniculocortical','thalamic','facial','caudal','septal','medial septal','dorsal septal',
              'olfactory','gustatory','frontal','frontostriatal','central','posterior','central posterior','mediodorsal|',
              'mediodorsal thalamic','geniculate','medio/-/','thalamo/-/','tegmental']

data = pd.read_csv('orig_spine.tsv',sep='\t')

combinations = []

for word in adjectives:
    for _, br in data.iterrows():
        new_row = br.copy()
        new_row.iloc[0] = f"{word} {br.iloc[0]}"
        combinations.append(new_row)
print('combinations')
two_combinations = []
print(two_combinations)

adj_2 = list(itertools.combinations(adjectives, 2))
print(f"2 combos: {adj_2[0:5]}")
counter =0

for str1, str2 in adj_2:
    for _, br in data.iterrows():
        counter += 1
        print(counter)
        new_row = br.copy()
        new_row.iloc[0] = f"{str1} {str2} {br.iloc[0]}"
        two_combinations.append(new_row)
        print('in loop')
        new_row2 = br.copy()
        new_row2.iloc[0] = f"{str2} {str1} {br.iloc[0]}"
        two_combinations.append(new_row2)

print('done with 2 combos')
expanded_terms = pd.DataFrame(combinations)
expanded_terms2 = pd.DataFrame(two_combinations)

expanded_terms.to_csv('expanded_terms.tsv',sep='\t',index=False)

expanded_terms2.to_csv('expanded_terms2.tsv',sep='\t',index=False)

