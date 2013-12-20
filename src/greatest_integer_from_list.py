import logging 

logger = logging.getLogger('maxinteger')


def getMaxFromList(max, items):

	"""

	Function to return the max integer found in the list. This could be a recursive call where the max value is compared with the items in the list and the if an item greater than max is found then 
	we set max to that item value and return max 

	@param max: Maximum value found in the root array so far 
	@type max: int
	@param items: List of items that includes items and other lists 
	@type items: list

	@rtype: int 
	"""

	if not max:
		raise Exception("No max value found on initial pass")
	# return the current max value if there is a none type in the items list or if the items list is empty
	if not items or len(items) == 0:
		return max

	for item in items:
		if isinstance(item, (int, long)):
			if item > max:
				max = item
		elif isinstance(item, list):
			max = getMaxFromList(max=max, items=item)

	return max

def setInitMax(items):
	
	if not items:
		logger.debug('Empty List: nothing to process!')
		return

	if len(items) == 0:
		return
	# do a pass over this level to look for integers
	for item in items:
		if isinstance(item, (int, long)):
			return item

	# no integers found in this pass. go into the first array that you see. 	
	for item in items:
		if isinstance(item, list):
			setInitMax(item)
	return None


if __name__ == "__main__":

	# get initial max value
	items = []
	a = [[1,["abc",'d','e'],[23,[],[],[334,2345,[2]]]], 1, 4, 10, 16]
	b = [1, 2, 3, 4]
	c = [[], [], []]
	# test case for setInit function.
	d = [[[[[[[[1000]]],300]]]]]
	items.extend(a)
	items.extend(b)
	items.extend(c)
	items.extend(d)
	print "data = %s " % items

	max = setInitMax(items)

	logger.debug("Evaluating maximum integer")
	
	result = getMaxFromList(max, items) 
	if not result:
		print "No integer was found in input..."
	else:
		print "Max integer in the list is = %s" % result





