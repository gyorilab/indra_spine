import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Add in stopwords
sw_nltk = stopwords.words('english')

false_phrases = [',', '(', 'II', '40%', ')', '2', 'MXII', 'IV', '60', '60%',
                 '20%', '6', 'e.g', '7', '3', 'non', '65', '7-Mar', '17',
                 '%', '29', '25', 'Ts2)']

exclude_words = ['normal', 'eminence', 'targets', 'individual', 'principal',
                 'facial', 'source', 'hair', 'several areas', 'factors',
                 'muscle','accessory', 'part', 'origin', 'separation',
                 'levels', 'stage', 'projections', 'dendrite', 'addition',
                 'distinct regions', 'locations', 'system', 'brain',
                 ' \'s disease', 'CNS', 'central nervous', 'cholinergic',
                 'projection', 'lobe', 'lobule', 'brain', 'cortex', 'anterior',
                 'posterior', 'lateral', 'medial', 'nucleus', 'superior',
                 'inferior', 'projections', 'lobes', 'lobules', 'cortices',
                 'dorsal', 'ventral', 'rostral', 'caudal', 'segment', 'area',
                 'tract','formation', 'segments', 'areas', 'tracts',
                 'formations', 'basal']
