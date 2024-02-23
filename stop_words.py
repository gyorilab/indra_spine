import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#add in stopwords
sw_nltk = stopwords.words('english')
#print(sw_nltk)

false_phrases = [',','(','II','40%',')','2','MXII','IV','60','60%','20%','6','e.g','7','3','non','65','7-Mar','17','%','29','25','Ts2)']

exclude_words = ['normal','eminence','diurnal','targets','red','several','one','visceral','individual','principal','norepinephrine',
                 'parvalbumin-immunoreactive','peptidergic','cytoarchitecture','dopamine','24b received','homotopic locations','specific',
                 'indirect','parallel','acid','glutamatergic','Lobules IXa-receive','widespread','gastrocnemius-soleus','Group II',
                 'quadriceps','hamstring','facial','source','hair','several areas','factors','muscle','lack','diffuse','ancestral',
                 'balance','sensilla','subdivisions','higher','relatively minor','Many','input','restricted regions','combination',
                 'detailed','different','proportion','multiple','several nuclei','certain','terminals','rat','large','spatial orientation',
                 'mouse','also','accessory','part','one side','origin','separation','neurochemical','retrogradely','groupings','network',
                 'organization','light','precursor','target','incidence','bank','characteristic','Epsilon','lengthy','hydroxylase',
                 'tyrosine','existence','crossed','project','specific areas','medium','Relative','blobs','many','distributions','patch',
                 'neck','injections','pancreas','studies','environment','labeling','receptor','pole','fewer','dark reared','nonvisual',
                 'lid','deep','Monoaminergic','functionally','rodents','aspartergic','components','relationship','aorta','neuropeptide',
                 'higher order','pharynx','lumbar','two','compartment','Clarke','presumptive glutamergic','gracile','sensory related',
                 '1,760 micron','former','gamma-amino','2nd','origins','Cytoarchitecture','connections','neurotensin','whiskers','trunk',
                 'analog','songbird','general','component','nociceptive information','differentiation','vice','relationships','direct',
                 'output','binaural','segregated','activity','functions','bulb','lungs','toadfish','hand','separate regions','nonhomologous',
                 'parvalbumin','serotonergic','forelimb','pelvic visceral','agranular','antennae','asymmetry','larger','low-threshold',
                 'lineage','honeybees','nonspiking','laterality','Thin','GABAergic','6a beta','presumed','6a alpha','morphology',
                 'neurosecretory','Distribution','projects','example','turn','Synaptic','development','hypothesis','immunoreactive granule',
                 'Taste','anterograde','tall','Morphology','line','cap','Area','vesicle','existing reports','distinct','similar',
                 'compartments','homotopic','populations','corresponding','axonal tracers','budgerigars','redial','retrograde','small',
                 'semicircular canal','group','shell','number','rotated','expression','marsupial','discrete','study','somatostatin',
                 'outflow','Retinal fibers','anatomical','ocular segregation','Major','unique connections','neurophysin',
                 'definitive evidence','synaptic transmission','possible sites','markers','differentially','laminar distribution',
                 'previously described','division','higher-order','degradative','topographically','dividing','third','four','additional',
                 'levels','stage','projections','link','plotter','ganglion cells','skeleton','ranging areas','monkey','horseshoe bats',
                 'dendrite','addition','distinct regions','fastest','nonreciprocal','monaural','unidentified','non-5-HT-containing','Direct',
                 'microiontophoretic','immunohistochemical','vertebrates','locations','system','7 also','migratory','extrinsic','fates',
                 'dendrites','Major intrinsic','mouse embryos','maturity','contrast','location','monkeys','retrograde labeling',
                 'radioactivity','wider','carp','Autonomic responses','interposed','second','Feedback','pyramidal','monosynaptic',
                 'olfactory axons','bear','horseshoe','index','thumb','mustached','population','branches','wallaby','cats','insect',
                 'trunk-tail branches','particular','lateral parts','barbel']

