class aa:
	"""docstring faa"""
	def __init__(self, name, three_letter, one_letter, polarity):
		self.name = name
		self.three_letter = three_letter
		self.one_letter = one_letter
		self.polarity = polarity

	def test(self,three_letter, one_letter,polarity):
		if (self.three_letter == three_letter.lower()) \
			and (self.one_letter == one_letter.upper()) and (self.polarity == polarity.lower()):
			print("Awesome!")
			return True
		else:
			if (self.three_letter != three_letter.lower()):
				print "Wrong three letter!"
			if (self.one_letter != one_letter.upper()):
				print "Wrong one letter!"
			if (self.polarity != polarity.lower()):
				print "Wrong polarity!"
			print "### For %s\n###\t three letter: %s\n###\t one letter: %s\n### \tpolarity: %s\nYou have a good day!\n" \
				%(self.name,self.three_letter,self.one_letter,self.polarity)
			return False
