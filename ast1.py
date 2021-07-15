import ast
import os

from ast import NodeVisitor

class ForWithoutList(NodeVisitor):
	def __init__(self):
		self.l1 = []
		self.number = 0

	def visit_For(self, node):
		s = str(ast.dump(node))
		self.number+=1
		s.lower()
		#print(s)
		if "call" in s or "list" in s or "tuple" in s or "set" in s:
			x=0
		else:
			self.l1.append(self.number)
	def printfunction(self):
		for i in self.l1:
			print("OPTIMIZATION FOUND: For loop "+str(i)+" without any functions/list/tuple or set: the following optimization might be aplicable: Euler-Maclaurin formula")

class Redundant_Functions(NodeVisitor):
    def __init__(self):
        self.l1 = set()
        self.l2 = set()

    def visit_Call(self, node):	 
    	name = node.func.id
    	try:
    		self.l1.add(name)
    	except:
    		pass

    def visit_FunctionDef(self, node):
    	#print('no')
    	self.l2.add(node.name)

    def printfunction(self):
    	#print(self.l2, self.l1)
    	x = self.l2 - self.l1
    	if len(x)>0:
    		print("REDUNDANT FUNCTIONS FOUND:")
    		print(x)

class PrefixPossibility(NodeVisitor):
	def __init__(self):
		self.l1 = []
		self.number = 0

	def visit_For(self, node):
		s = str(ast.dump(node))
		s = s.lower()
		self.number+=1
		if "sum" in s:
			self.l1.append(number)
	def printfunction(self):
		for i in self.l1:
			print("POSSIBLE_OPTIMIZATION: prefix sum might be aplicable for loop"+str(i))

class BinaryPosibility(NodeVisitor):
    def __init__(self):
    	self.number = 0
    	self.l1 = []

    def visit_Call(self, node):	 
    	self.number+=1
    	if "id" in dir(node.func):
    		if node.func.id=='sorted':
    			self.l1.add(number)
    	elif "value" in dir(node.func):
    		if node.func.value=='sort':
    			self.l1.add(number)

    def printfunction(self):
    	for i in self.l1:
    		print("POSSIBLE_OPTIMIZATION: Binary Sum  some might be aplicable for sorted()/.sort()"+str(i))
class ModularPosibility(NodeVisitor):
    def __init__(self):
    	self.number = 0
    	self.l1 = []

    def visit_BinOp(self, node):
    	self.number+=1
    	if "op" in dir(node.BinOp):
    		if node.BinOp.op=='Mod()':
    			l1.add(self.number)
    def printfunction(self):
    	for i in self.l1:
    		print("POSSIBLE_OPTIMIZATION: Modular Arithimetic some might be aplicable for mod operation"+str(i))
path = "C:/Users/neils/Desktop/Projects/Python/Hackathon/test/test.py"
file = open(path).read()
tree = ast.parse(file)
ForWithoutList1 = ForWithoutList()
ForWithoutList1.visit(tree)
ForWithoutList1.printfunction()

Redundant_Functions1 = Redundant_Functions()
Redundant_Functions1.visit(tree)
Redundant_Functions1.printfunction()

PrefixPossibility1 =  PrefixPossibility()
PrefixPossibility1.visit(tree)
PrefixPossibility1.printfunction()

BinaryPosibility1 =  BinaryPosibility()
BinaryPosibility1.visit(tree)
BinaryPosibility1.printfunction()

ModularPosibility1 =  BinaryPosibility()
ModularPosibility1.visit(tree)
ModularPosibility1.printfunction()
