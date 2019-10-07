# this is a program that will make a synteny map (genome diagram)
# from a specified genbank file input
# More info: https://biopython-cn.readthedocs.io/zh_CN/latest/en/chr17.html

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
record1 = input("What is your genbank filename? Ex: ""sequence.gb"" \n")
record = SeqIO.read(record1, "genbank")

# create an empty diagram, then add an empty track & empty feature set
gd_diagram = GenomeDiagram.Diagram("S. cerevisiae Chromosome IX")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

#Take each gene SeqFeature object in our SeqRecord, and use it to
# generate a feature on the diagram. 
for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.lightblue
    else:
        color = colors.blue
    gd_feature_set.add_feature(feature, sigil="ARROW", color=color, arrowshaft_height=1.0,
                               label=True, label_size=8, label_angle=30)

# Generate the output file (a PNG)
gd_diagram.draw(format="linear", orientation="landscape", pagesize=(30*cm,10*cm),
                fragments=1, start=0, end=len(record))
gd_diagram.write((record1 + "_map.png"), "PNG")
