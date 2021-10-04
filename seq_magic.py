#!/usr/bin/env python
# coding: utf-8

# In[2]:


def transcribe(seq, nucleo):
    if nucleo == "dna":
        d = dna_rnadict
    else:
        d = rna_dnadict
        print("In fact it's a reverse transcription, seq is RNA")
    return "".join([d[seq[i]] for i in range(len(seq))])


def reverse(seq):
    return seq[::-1]


def complement(seq, nucleo):
    if nucleo == "dna":
        d = dna_dnadict
    else:
        d = rna_rnadict
    return "".join([d[seq[i]] for i in range(len(seq))])


command = ""
rna_dnadict = {"A": "T", "U": "A", "G": "C", "C": "G"}
rna_rnadict = {"A": "U", "U": "A", "G": "C", "C": "G"}
dna_dnadict = {"A": "T", "T": "A", "G": "C", "C": "G"}
dna_rnadict = {"A": "U", "T": "A", "G": "C", "C": "G"}

while command != 'exit':
    command = input('Do: ')
    if command == 'exit':
        print("NOOOOOOOO!!!")
        break
    raw_sequence = input("Seq: ")
    mask = [char.islower() for char in raw_sequence]
    sequence = raw_sequence.upper()
    dna, rna = True, True
    nucleo = ""
    for char in sequence:
        if char not in dna_dnadict:
            dna = False
        if char not in rna_rnadict:
            rna = False
    if dna == True:
        nucleo = 'dna'
    elif rna == True:
        nucleo = 'rna'

    else:
        print("not a nucleic acid")
        continue

    res = ''
    if command == 'transcribe':
        res = transcribe(sequence, nucleo)
        res = ''.join([res[i].lower() if mask[i] else res[i] for i in range(len(res))])
    elif command == 'reverse':
        res = reverse(raw_sequence)
    elif command == 'complement':
        res = complement(sequence, nucleo)
        res = ''.join([res[i].lower() if mask[i] else res[i] for i in range(len(res))])
    elif command == "reverse complement":
        res = complement(sequence, nucleo)
        res = ''.join([res[i].lower() if mask[i] else res[i] for i in range(len(res))])
        res = reverse(res)
    else:
        print("Unknown command")
    print(res)

