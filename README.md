# SIB_Technical_Assignment
 Coding Exercice
# Project Description
The program prints the 3 most recurrent amino acids for a given protein using the neXtProt API.
The program gets as argument the protein identifier and access programmatically a url of the neXtProt API to retrieve its sequence. From the URL the sequence can be checked.
The program counts all amino acids and order them by frequency.
# Example: 
Url: https://api.nextprot.org/entry/NX_P01308/isoform.json
Sequence:
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDL
QVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN

The amino acid L (Leucine) appears 20 times in the sequence, the amino acid G (Glycine) appears 12 times and the amino acid A
(Alanine) appears 10 times. All other amino acids appear less than 10 times in the sequence.

## Note

The protein identifier have been taken as an argument in the main function: main(Protein_Identifier).

## Running the tests
The program have been tested on three protein identifiers NX_P01308, NX_Q96IX5,NX_O95714.

***Inputs     *** Outputs

*** NX_P01308 *** L  = 20 , G  = 12 , A  = 10
*** NX_Q96IX5 *** A  = 6 , T  = 6 , K  = 6 
*** NX_O95714 *** L  = 547 , S  = 413 , G  = 396


## Authors
**Racha Gouareb**
