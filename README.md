# synteny-mapper
These python scripts generate synteny maps based on genbank files or user-specified start/stop coordinates using the Bio.Graphics.GenomeDiagram module, which you can read about [here](https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html). 

Dependencies: [biopython](https://biopython.org/)

![biopython-logo](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/biopython_logo_white.png)


synteny_mapping_simple.py
------------
To use this script:
  1. Create sequence file in the same file where the python script is stored. You can either upload a Genbank file containing whatever section you are interested in mapping or edit an Ape file. 
  2. Run script and follow the prompts. Just make sure that the areas you want to show up on this graph are designated as "gene" instead of "misc_feature" when you save the file in the Ape GUI. Only include the area you want mapped in the Ape file- cut everything else out. 
  
  ![ape_prompt.png](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/ape_prompt.png)

* Resulting Image:
![NC_001133.9.gb_map.png](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/NC_001133.9.gb_map.png)


synteny_mapping_coord.py
------------
This script lets you add an extra gene on there manually by specifying start and stop positions, if you're interested. Otherwise, it seems easier to just annotate everything in Ape, and then have the script draw that. The output file will appear in the same folder with the python script.

![ToxinSeq.gb_map.png](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/ToxinSeq.gb_map.png)
