#!/usr/bin/env python3
import re
import sys
from Bio import SeqIO

filename = "human_cds.fasta"

fasta_dict = SeqIO.to_dict(SeqIO.parse(filename, 'fasta'))





