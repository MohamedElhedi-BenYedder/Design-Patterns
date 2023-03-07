from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_builder_a(self):
        pass
    
    @abstractmethod
    def create_builder_b(self):
        pass

# Concrete Factory
class ConcreteFactory(AbstractFactory):
    def create_builder_a(self):
        return ConcreteBuilderA()
    
    def create_builder_b(self):
        return ConcreteBuilderB()

# Builder A
class BuilderA(ABC):
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder A
class ConcreteBuilderA(BuilderA):
    def __init__(self):
        self.product = ProductA()
    
    def build_part_a(self):
        self.product.part_a = 'Part A for Product A'
    
    def build_part_b(self):
        self.product.part_b = 'Part B for Product A'
    
    def get_result(self):
      return self.product

# ProductA
class ProductA:
  def init(self):
    self.part_a = None
    self.part_b = None
   
# BuilderB
class BuilderB(ABC):
  @abstractmethod
  def build_part_c(self):
    pass
  @abstractmethod
  def build_part_d(self):
    pass

  @abstractmethod
  def get_result(self):
    pass
# Concrete Builder B
class ConcreteBuilderB(BuilderB):
  def init(self):
    self.product = ProductB()
  def build_part_c(self):
    self.product.part_c = 'Part C for Product B'

  def build_part_d(self):
    self.product.part_d = 'Part D for Product B'

  def get_result(self):
    return self.product
  
# Product B
class ProductB:
  def init(self):
    self.part_c = None
    self.part_d = None

# Client Code

factory = ConcreteFactory()
builder_a = factory.create_builder_a()
builder_b = factory.create_builder_b()

builder_a.build_part_a()
builder_a.build_part_b()
product_a = builder_a.get_result()
print(product_a.part_a, product_a.part_b)

builder_b.build_part_c()
builder_b.build_part_d()
product_b = builder_b.get_result()
print(product_b.part_c, product_b.part_d)
