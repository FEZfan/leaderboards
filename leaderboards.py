class sllnode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class sll:
	def __init__(self, values = None):
		if values:
			values.reverse()
			self.head = sllnode(values.pop())
			self.last = self.head
			while values:
				v = sllnode(values.pop())
				self.last.next = v
				self.last = v
			return
		self.head = None

	def print(self):
		i = self.head
		while i.next:
			print(i.value)
			i = i.next
		print(i.value)

class Leaderboard:
	def __init__(self, length, comp = lambda a,b: a>b):
		self.length = length
		self.lb = sll([None]*length)
		self.comp = comp

	def add(self, e):
		e = sllnode(e)
		i = self.lb.head
		li = None
		while i and (i.value == None or self.comp(e.value,i.value)):
			li = i
			i = i.next

		if li:
			li.next = e
			e.next = i
			self.lb.head = self.lb.head.next

	def print(self):
		self.lb.print()

	def toList(self):
		a = []
		i = self.lb.head
		while i:
			a.append(i.value)
			i = i.next
		return a
