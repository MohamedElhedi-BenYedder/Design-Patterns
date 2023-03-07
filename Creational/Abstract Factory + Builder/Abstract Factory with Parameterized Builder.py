from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self, param):
        pass

# Concrete Factory
class ConcreteFactory(AbstractFactory):
    def create_product(self, param):
        builder = ConcreteBuilder(param)
        return builder.get_result()

# Builder
class Builder(ABC):
    @abstractmethod
    def build_part_a(self, param):
        pass
    
    @abstractmethod
    def build_part_b(self, param):
        pass
    
    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class ConcreteBuilder(Builder):
    def __init__(self, param):
        self.product = Product()
        self.build_part_a(param)
        self.build_part_b(param)
    
    def build_part_a(self, param):
        self.product.part_a = f'Part A with {param}'
    
    def build_part_b(self, param):
        self.product.part_b = f'Part B with {param}'
    
    def get_result(self):
        return self.product

# Product
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

# Client code
factory = ConcreteFactory()
product = factory.create_product('param')
print(product.part_a, product.part_b)
