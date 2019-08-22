import random
from aa import aa

random.seed(2019)

lys = aa('Lysine','lys', 'K','pos')
arg = aa('Arginine','arg', 'R', 'pos')
his = aa('Histidine', 'his', 'H', 'pos')
asp = aa('Asparatic Acid', 'asp', 'D', 'neg')
glu = aa('Glutamic Acid', 'glu', 'E', 'neg')
asn = aa('Asparagine', 'asn', 'N', 'polar')
gln = aa('Glutamine', 'gln', 'Q', 'polar')
ser = aa('Serine', 'ser', 'S', 'polar')
thr = aa('Threonine','thr', 'T', 'polar')
tyr = aa('Tyrosine', 'tyr', 'Y','polar')
gly = aa('Glycine', 'gly', 'G', 'nonpolar')
ala = aa('Alanine','ala', 'A','nonpolar')
cys = aa('Cysteine','cys', 'C', 'nonpolar')
val = aa('Valine','val','V','nonpolar')
leu = aa('Leucine', 'leu', 'L', 'nonpolar')
isl = aa('Isoleucine', 'ile', 'I', 'nonpolar')
TRY = aa('Tryptophan','try', 'W','nonpolar')
pro = aa('Proline','pro','P','nonpolar')
phe = aa('Phenylalanine','phe','F','nonpolar')
met = aa('Methionine','met','M','nonpolar')

aas = [lys,arg,his,asp,glu,asn,gln,ser,thr,tyr,gly,ala,cys,val,leu,isl,TRY,pro,phe,met]
print "Let's start!"
num_runs = int(raw_input("How many runs do you want to play?\n"))
correct = 0
for i in range(num_runs):
	amino_acid = aas[random.randint(0,19)]
	name = amino_acid.name
	print 'The amino acid to be tested is: %s.\n' %name
	three_letter = str(raw_input('what\'s the three letter of this amino acid?\n'))
	one_letter = str(raw_input('what\'s the one letter of this amino acid?\n'))
	bold = '\033[1m'
	reg = '\033[0m'
	polarity = str(raw_input('what\'s the property of this amino acid? {} Please choose from nonpolar, polar, pos, neg.\n'.format(bold)))
	while polarity not in ['nonpolar','polar','pos','neg']:
		polarity = str(raw_input('what\'s the property of this amino acid? {} Please choose from nonpolar, polar, pos, neg.\n'.format(bold)))
	print '\n%s' %reg
	if amino_acid.test(three_letter,one_letter,polarity):
		correct += 1
if correct > num_runs / 2:
	print "\nYou got %d correct, great job!" %correct
else:
	print "\nYou got %d correct, cheers up!" %correct
