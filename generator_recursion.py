def gen_rec(value):
	if value == 1:
		yield value
	else:
		yield from gen_rec(value - 1)
	
for item in gen_rec(5):
	print(item) 