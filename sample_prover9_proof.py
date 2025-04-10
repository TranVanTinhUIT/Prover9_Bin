
# 
import xml.etree.ElementTree as ET
from prover9_proof.proof import Proof
from prover9_proof.sample_proof import proof_xml

# Set path to proof xml file.
root = ET.fromstring(proof_xml)

number_of_proofs = root.attrib['number_of_proofs']

proof_node = root.find('proof')

proof = Proof(proof_node=proof_node)

print(proof)