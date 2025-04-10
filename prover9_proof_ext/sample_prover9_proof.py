
# 
import xml.etree.ElementTree as ET
from prover9_proof_ext.prover9_proof import Proof
from prover9_proof_ext.sample_proof import proof_xml

# Set path to proof xml file.
tree = ET.parse(proof_xml)

root = tree.getroot()
number_of_proofs = root.attrib['number_of_proofs']

proof_node = root.find('proof')

proof = Proof(proof_node=proof_node)

print(proof)