# this is a program that will make a synteny map (genome diagram)
# from a specified genbank file input

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
record1 = input("What is your genbank filename? Ex: ""sequence.gb"" \n")
record = SeqIO.read(record1, "genbank")
pgene_start = int(input("What is the start location of your putative gene?\n"))
pgene_end = int(input("What is the end location of your putative gene?\n"))
pgene_ori = int(input("Is putative gene forward (""1"") or reverse (""-1"")?\n"))
pgene = str(input("What would you like to name your putative gene?\n"))

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

# add putative gene
feature = SeqFeature(FeatureLocation(pgene_start, pgene_end), strand=pgene_ori)
gd_feature_set.add_feature(feature, name=pgene, sigil="ARROW", color="lightgreen",
                           arrowshaft_height=1.0, label=True, label_size=8, label_angle=30)
 
# Generate the output file (a PNG)
gd_diagram.draw(format="linear", orientation="landscape", pagesize=(30*cm,5*cm),
                fragments=1, start=0, end=len(record))
gd_diagram.write((record1 + "_map.png"), "PNG")
