# synteny-mapper
These python scripts generate synteny maps based on genbank files or user-specified start/stop coordinates using the Bio.Graphics.GenomeDiagram module, which you can read about [here](https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html). 

Dependencies: [biopython](https://biopython.org/)
![biopython-logo](https://biopython.org/assets/images/biopython_logo_white.png)

synteny_mapping_simple.py
------------
To use this script, you upload a Genbank file containing whatever section you are interested in mapping (must be located in the same file where the python script is stored), and just enter its filename when prompted after running the script. You can actually take Ape files too! Just make sure that the areas you want to show up on this graph are designated as "gene" instead of "misc_feature" when you save the file in the Ape GUI. Only include the area you want mapped in the Ape file- cut everything else out. 

![NC_001133.9.gb_map.png](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/NC_001133.9.gb_map.png)

synteny_mapping_coord.py
------------
This script lets you add an extra gene on there manually by specifying start and stop positions, if you're interested. Otherwise, it seems easier to just annotate everything in Ape, and then have the script draw that. The output file will appear in the same folder with the python script.

![ToxinSeq.gb_map.png](https://raw.githubusercontent.com/amcrabtree/synteny-mapper/master/images/ToxinSeq.gb_map.png)
