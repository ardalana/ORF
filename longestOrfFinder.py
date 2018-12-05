#!/usr/bin/env python3
import sys

# Program to calculate and print the longest Open Reading Frame (ORF) in a given interleaved fasta DNA sequence/genome.
# Run like: python3 longestOrfFinder.py fastaFile
seqFile=sys.argv[1]

lines=[]
compDic={'A':'T','T':'A','C':'G','G':'C'}
stopCodons=['TAG','TGA','TAA']
origStart=[];revComStart=[]
origORF=[];revComORF=[]

# Produce the original and the reverse complement sequences.
with open(seqFile) as infile:
    for line in infile:
        if not line.startswith('>'):
            lines.append(line.rstrip('\n'))
    origSeq=''.join(lines)
    revComSeq=''.join(compDic.get(i) for i in origSeq[::-1])

# Find start codon positions in either of the strands.
def findStart(seqLine,startList):
    offset=0
    while offset<=len(seqLine):
        foundStart=seqLine.find('ATG',offset)
        if foundStart!=-1:
            startList.append(foundStart)
            offset=foundStart+1
        if foundStart==-1: break
    return startList

# Calculate ORFs in each strand.
def findORF(seqLine,startList,ORFList):
    for i in findStart(seqLine,startList):
        j=i+3
        while j<=len(seqLine)-3:
            if seqLine[j:j+3] in stopCodons:
                ORFList.append(j-i); break
            else: j+=3
    return ORFList

# Output the longest ORF.
longestORF=max(findORF(origSeq,origStart,origORF)+findORF(revComSeq,revComStart,revComORF))
print(longestORF)
