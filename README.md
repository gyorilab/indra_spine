# INDRA-SPINE
**INDRA-SPINE** is an adaptation of INDRA (Integrated Network and Dynamical Reasoning Assembler), which is an automated knowledge assembly system that can be used to traverse PubMed and read thousands of papers using natural language processing. It can then be used to create executable or graphical representations of biochemical pathways assembled from multiple publications.

INDRA-SPINE searches neuroscience literature for neuroanatomical relations at scale, taking into account context within a sentence.


## Setup
INDRA-SPINE uses REACH, developed by the CLU lab at the University of Arizona, and Odinson, developed by Lum AI. Both of these repositories can be cloned prior to using INDRA-SPINE. The user should set the REACH_HOME environmental variable with the path to their local copy of the REACH repository.

Using Odinson requires an Intel installation of Java, which can be found at [this link](https://cdn.azul.com/zulu/bin/zulu11.66.15-ca-jdk11.0.20-macosx_x64.dmg?_gl=1*1emxlls*_ga*MTY2MTQzMDU0My4xNjg5MjgwOTU5*_ga_42DEGWGYD5*MTY4OTg2Nzg4Ny4yLjEuMTY4OTg3MDIxNy41OC4wLjA).

## Customizing REACH and Odinson

REACH and Odinson need to be customized prior to using INDRA-SPINE. This can be done following these steps:

### Customizing REACH

**Step One**
INDRA-SPINE's resources folder contains two tsv files: `spine.tsv` and `neuro-behavior.tsv`. These should both be added to the `src/main/resources/org/clulab/reach/kb` folder within the local version of REACH. 
**Step Two**
A new entry for each then needs to be added to `src/main/resources/application.conf` under the `KnowledgeBases` block. 
**Step Three**
Two new entity types need to be added to the taxonomy with REACH at `main/src/main/resources/org/clulab/reach/biogrammar/taxonomy.yml`.
**Step Four**
Two new rules need to be added to `main/src/main/resources/org/clulab/reach/biogrammar/entities/entities.yml`.
**Step Five**
The `version.sbt` file should then be updated with a new version number. 
**Step Six**
The `build.sbt` file contains a line `.aggregate(processors, main, causalAssembly, export)`, which needs to be updated to `.aggregate(processors, main, causalAssembly, export, bioresources)`. 
**Step Seven**
The final step is to run `sbt compile` and `sbt publishLocal` on REACH.

### Customizing Odinson

**Step One**
Within Odinson, in `extra/build.sbt`, the line `"org.clulab" %% "reach-processors" % "1.6.4-SNAPSHOT"` should be added to the `libraryDependencies` block, but with the same version number that was added to `version.sbt` in REACH. 
**Step Two**
In `extra/src/main/resources/application.conf`, the line `processorType    = "CluProcessor"`, should be replaced with the line `processorType    = "BioNLPProcessor"`. 
**Step Three**
In `extra/src/main/scala/ai/lum/odinson/extra/utils/ProcessorsUtils.scala`, the line `import org.clulab.processors.bionlp.BioNLPProcessor` should be added under the line `import org.clulab.processors.fastnlp.FastNLPProcessor` and the block
```
case "BioNLPProcessor" => {
        dynet.Utils.initializeDyNet(autoBatch = false, mem = "1024,1024,1024,1024")
        new BioNLPProcessor
      }
```
should be added within `getProcessor`. 
**Step Four**
In the file at `extra/src/main/scala/ai/lum/odinson/extra/AnnotateText.scala` the line `import org.clulab.processors.bionlp.BioNLPProcessor` should be added, and within `annotateTextFile`, this block should be added:
```
processor match {
      case p:BioNLPProcessor =>
        p.recognizeRuleNamedEntities(doc)
    }
```

## Odinson Web Service
Using INDRA-SPINE also requires access to the Odinson web service, which can be found by running this command:
```
docker pull lumai/odinson-rest-api
```

## Generating a Corpus
The starting point for using INDRA-SPINE is a corpus of articles or abstracts. It will be stored as a set of text files with the extension `.txt` in a folder called `text` within a larger folder named for the corpus. Easy access to downloading articles from PubMed using INDRA and INDRA DB is available via the CLI provided. The user simply has to run this command in Terminal, substituting in the desired search term and path to save the files:
``` 
python -m indra_spine.cli corpus searchterm path
``` 

## Annotating and Indexing the Corpus
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

## Extracting Relations and Generating a Graph
Following this, the docker for the Odinson web service should be run using this command, with the path updated to the directory where the corpus was generated:
```
docker run -v /path_to_corpus:/app/data/odinson -p 9000:9000 lumai/odinson-rest-api
```

The interaction network file can then be used to extract relations from the corpus and generate graphs. This can also be accessed via the CLI. The user simply has to run this command in Terminal, substituting in the desired search term and the path to save results:
``` 
python -m indra_spine.cli 'interaction network' searchterm path
```
