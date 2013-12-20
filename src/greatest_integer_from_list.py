import logging 

logger = logging.getLogger('maxinteger')


def getMaxFromList(max, items, trace):

	"""

	Function to return the max integer found in the list. This could be a recursive call where the max value is compared with the items in the list and the if an item greater than max is found then 
	we set max to that item value and return max 

	@param max: Maximum value found in the root array so far 
	@type max: int
	@param items: List of items that includes items and other lists 
	@type items: list

	@rtype: int 
	"""

	# return the current max value if there is a none type in the items list or if the items list is empty
	if not items or len(items) == 0:
		return max

	for item in items:
		if isinstance(item, (int, long)):
			if not max or item > max:
				max = item
		elif isinstance(item, list):
			if trace:
				trace.increment()
			max = getMaxFromList(max=max, items=item, trace=trace)

	return max
	
class RecursionTrace:

	def __init__(self):
		self.count = 0

	def reset(self):
		self.count = 0

	def increment(self):
		self.count = self.count + 1

	def __str__(self):
		return "Total calls : %s" % str(self.count)



if __name__ == "__main__":

	# get initial max value
	items = []
	a = [[1,["abc",'d','e'],[23,[],[],[334,2346,[2]]]], 1, 4, 10, 16]
	b = [1, 2, 3, 4]
	c = [[], [], []]
	# test case for setInit function.
	d = [[[[[[[[1000]]],300]]]]]
	items.extend(a)
	items.extend(b)
	items.extend(c)
	items.extend(d)
	print "data = %s " % items

	logger.debug("Evaluating maximum integer")
	trace = RecursionTrace()
	result = getMaxFromList(None, items, trace) 
	
	if not result:
		print "No integer was found in input..."
	else:
		print "Max integer in the list is = %s" % result
	print "Recursion Trace - %s " % trace





