from nltk.sem.logic import Expression
from nltk.inference.prover9 import *
from nltk.sem import Expression

read_expr = Expression.fromstring

# ∀c (Course(c) → ContainsKnowledge(c))
r1 = read_expr('all x. (Course(x) -> ContainsKnowledge(x) )')

# ∀s, ∀c (Takes(s, c) ∧ Passes(s, c) → AcquiresKnowledge(s))
r2 = read_expr(' all x y. ( Takes(x, y) & Passes(x, y) -> AcquiresKnowledge(x) ) ')

# ∀s (AcquiresKnowledge(s) → GainsUnderstanding(s))
r3 = read_expr (' all x. ( (AcquiresKnowledge(x) -> GainsUnderstanding(x)) ) ')

# Takes(Tuan, NLP) ∧ Passes(Tuan, NLP)
fact1 = read_expr('Takes(Tuan, NLP)')
fact2 = read_expr('Passes(Tuan, NLP)')

# Student(Tuan)
fact3 = read_expr('Student(Tuan)')

# Course(NLP)
fact4 = read_expr('Course(NLP)')

goal = read_expr('ContainsKnowledge(NLP)')
goal2 = read_expr('GainsUnderstanding(Tuan)')
assumptions = [r1, r2, r3, fact1, fact2, fact3, fact4]

prover9 = Prover9()
prover9._prover9_bin = 'D:/Code/ARM_Codes/Prover9_Bin/bin/prover9'
prover9._prooftrans_bin = 'D:/Code/ARM_Codes/Prover9_Bin/bin/prooftrans'

result = prover9._prove(goal = goal2, assumptions = assumptions)
stdout = result[1]
prooftrans_out = prover9._call_prooftrans(stdout, ["xml"])[0]
proof_xml = prooftrans_out[prooftrans_out.find('<proofs'):] # THIS IS PROOF XML FILE. See file sample_proof,py
