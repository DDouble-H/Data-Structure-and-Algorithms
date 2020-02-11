class queue():
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		del self.queue[0]
		return

	def isEmpty(self, queue):
		if queue is None:
			return True
		else:
			return False

	def getSize(self):
		return len(self.queue)


if __name__ == '__main__':
	Q = queue()
	print(Q.queue)
	Q.enqueue(10)
	Q.enqueue(20)
	Q.enqueue(30)
	Q.enqueue(40)
	Q.enqueue(50)
	print(Q.queue)
	print(Q.dequeue())
	print(Q.dequeue())
	print(Q.queue)
