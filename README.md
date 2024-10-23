#INDRA SPINE
INDRA-SPINE is an adaptation of INDRA (Integrated Network and Dynamical Reasoning Assembler), which is an automated knowledge assembly system that can be used to traverse PubMed and read thousands of papers using natural language processing. It can then be used to create executable or graphical representations of biochemical pathways assembled from multiple publications.

INDRA-SPINE searches neuroscience literature for neuroanatomical relations at scale, taking into account context within a sentence.

INDRA-SPINE uses REACH, developed by the CLU lab at the University of Arizona, and Odinson, developed by Lum AI. Both of these repositories can be cloned prior to using INDRA-SPINE.

It requires an Intel installation of Java, which can be found at [this link](https://cdn.azul.com/zulu/bin/zulu11.66.15-ca-jdk11.0.20-macosx_x64.dmg?_gl=1*1emxlls*_ga*MTY2MTQzMDU0My4xNjg5MjgwOTU5*_ga_42DEGWGYD5*MTY4OTg2Nzg4Ny4yLjEuMTY4OTg3MDIxNy41OC4wLjA).

It also requires access to the Odinson web service, which can be found by running this command:
```
docker pull lumai/odinson-rest-api
```

The starting point for using INDRA-SPINE is a corpus of articles or abstracts. It will be stored as a set of text files with the extension `.txt` in a folder called `text` within a larger folder named for the corpus. Easy access to downloading articles from PubMed using INDRA and INDRA DB is available via the CLI provided. The user simply has to run this command in Terminal, substituting in the desired search term:
``` 
python -m indraq_spine.cli corpus searchterm
``` 

The next step is to configure Odinson. The `odinson.dataDir` variable in the `application.conf` file (which is located at `extra/src/main/resources`) should be updated to point to the directory containing the corpus.

Next, the user should use Odinson to annotate and index the corpus. This step requires the Intel version of Java to be installed using the link above. These commands should then be run from within the Odinson directory:

**Step 1:**
```
export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home
```

**Step 2, annotate text:**
```
sbt -java-home $JAVA_HOME "extra/runMain ai.lum.odinson.extra.AnnotateText"
```

**Step 3, generate index:**
```
sbt -java-home $JAVA_HOME "extra/runMain ai.lum.odinson.extra.IndexDocuments"
```

Following this, the docker for the Odinson web service should be run using this command, with the path updated to the directory where the corpus was generated:
```
docker run -v /path_to_corpus:/app/data/odinson -p 9000:9000 lumai/odinson-rest-api
```

The interaction network file can then be used to extract relations from the corpus and generate graphs. This can also be accessed via the CLI. The user simply has to run this command in Terminal, substituting in the desired search term:
``` 
python -m indra_spine.cli 'interaction network' searchterm
```
