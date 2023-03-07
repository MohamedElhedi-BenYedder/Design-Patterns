from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# Concrete Factory
class ConcreteFactory(AbstractFactory):
    def create_product(self):
        builder = ConcreteBuilder()
        builder.build_part_a()
        builder.build_part_b()
        return builder.get_result()

# Builder
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.part_a = 'Part A'
    
    def build_part_b(self):
        self.product.part_b = 'Part B'
    
    def get_result(self):
        return self.product

# Product
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

# Client code
factory = ConcreteFactory()
product = factory.create_product()
print(product.part_a, product.part_b)
