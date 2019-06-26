class Person(object):

	# 限定Person 对象只能绑定_name, _age 和_gender 属性
	__slots__ = ('_name', '_age', '_gender')

	def __init__(self, name, age):
		self._name = name
		self._age = age

	# 访问器 - getter 方法
	@property
	def name(self):
		return self._name
	
	# 访问器 - getter 方法
	@property
	def age(self):
		return self._age
	
	# 修改器 - setter方法
	@age.setter
	def age(self, age):
		self._age = age

	def play(self):
		if self._age <= 16:
			print('%s 正在玩飞行棋.' % self._name)
		else:
			print('%s 正在玩斗地主.' % self._name)

def main():
	person = Person('王大锤', 12)
	person.play()
	person.age = 22
	person.play()
	person._gender = '男'
	# person.name = '白元芳'

if __name__ == '__main__':
	main()