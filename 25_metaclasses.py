# Lesson 25: Metaclasses

"""
This lesson covers:
- What are metaclasses
- Understanding class creation
- Creating custom metaclasses
- Metaclass methods and attributes
- Metaclass inheritance
- Practical metaclass examples
- When to use metaclasses
- Best practices and alternatives
"""

# 1. What are Metaclasses
print("=== What are Metaclasses ===")

# A metaclass is a class whose instances are classes
# In Python, everything is an object, including classes
# Classes are instances of metaclasses

# The default metaclass is 'type'
class MyClass:
    pass

print(f"MyClass is an instance of: {type(MyClass)}")
print(f"type is: {type(type)}")

# All classes are instances of 'type' by default
print(f"int is an instance of: {type(int)}")
print(f"str is an instance of: {type(str)}")
print(f"list is an instance of: {type(list)}")

# 2. Understanding Class Creation
print("\n=== Understanding Class Creation ===")

# Class creation using type()
# type(name, bases, dict)
def __init__(self, name):
    self.name = name

def say_hello(self):
    return f"Hello, I'm {self.name}"

# Create a class using type()
Person = type('Person', (), {
    '__init__': __init__,
    'say_hello': say_hello
})

# Use the dynamically created class
person = Person("Alice")
print(f"Person created: {person.say_hello()}")

# Equivalent class definition
class Person2:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return f"Hello, I'm {self.name}"

person2 = Person2("Bob")
print(f"Person2 created: {person2.say_hello()}")

# 3. Creating Custom Metaclasses
print("\n=== Creating Custom Metaclasses ===")

# Basic metaclass
class MyMeta(type):
    """A simple metaclass"""
    
    def __new__(cls, name, bases, attrs):
        print(f"Creating class: {name}")
        print(f"Bases: {bases}")
        print(f"Attributes: {list(attrs.keys())}")
        
        # Add a class attribute
        attrs['created_by'] = 'MyMeta'
        
        return super().__new__(cls, name, bases, attrs)

# Use the metaclass
class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

print(f"MyClass created_by: {MyClass.created_by}")

# 4. Metaclass Methods and Attributes
print("\n=== Metaclass Methods and Attributes ===")

class VerboseMeta(type):
    """Metaclass that provides verbose class creation"""
    
    def __new__(cls, name, bases, attrs):
        print(f"__new__ called for {name}")
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        print(f"__init__ called for {name}")
        super().__init__(name, bases, attrs)
    
    def __call__(cls, *args, **kwargs):
        print(f"__call__ called for {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        print(f"Instance created: {instance}")
        return instance

class VerboseClass(metaclass=VerboseMeta):
    def __init__(self, value):
        self.value = value

# Create an instance
print("Creating VerboseClass instance:")
verbose_instance = VerboseClass("test")

# 5. Metaclass Inheritance
print("\n=== Metaclass Inheritance ===")

class BaseMeta(type):
    """Base metaclass"""
    
    def __new__(cls, name, bases, attrs):
        print(f"BaseMeta creating: {name}")
        attrs['base_meta'] = True
        return super().__new__(cls, name, bases, attrs)

class DerivedMeta(BaseMeta):
    """Derived metaclass"""
    
    def __new__(cls, name, bases, attrs):
        print(f"DerivedMeta creating: {name}")
        attrs['derived_meta'] = True
        return super().__new__(cls, name, bases, attrs)

class BaseClass(metaclass=BaseMeta):
    pass

class DerivedClass(metaclass=DerivedMeta):
    pass

print(f"BaseClass base_meta: {BaseClass.base_meta}")
print(f"DerivedClass base_meta: {DerivedClass.base_meta}")
print(f"DerivedClass derived_meta: {DerivedClass.derived_meta}")

# 6. Practical Metaclass Examples
print("\n=== Practical Metaclass Examples ===")

# Example 1: Singleton Metaclass
class SingletonMeta(type):
    """Metaclass that creates singleton classes"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Test singleton
s1 = SingletonClass("first")
s2 = SingletonClass("second")
print(f"Same instance: {s1 is s2}")
print(f"s1.value: {s1.value}")
print(f"s2.value: {s2.value}")

# Example 2: Validation Metaclass
class ValidationMeta(type):
    """Metaclass that adds validation to classes"""
    
    def __new__(cls, name, bases, attrs):
        # Add validation method to all classes
        attrs['validate'] = cls._create_validate_method(attrs)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _create_validate_method(attrs):
        def validate(self):
            for attr_name, attr_value in attrs.items():
                if hasattr(attr_value, '__annotations__'):
                    # Check type annotations
                    for param_name, param_type in attr_value.__annotations__.items():
                        if param_name != 'return':
                            # This is a simplified validation
                            pass
            return True
        return validate

class ValidatedClass(metaclass=ValidationMeta):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

validated = ValidatedClass("Alice", 25)
print(f"Validation result: {validated.validate()}")

# Example 3: Registry Metaclass
class RegistryMeta(type):
    """Metaclass that maintains a registry of classes"""
    
    _registry = {}
    
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        cls._registry[name] = new_class
        return new_class
    
    @classmethod
    def get_class(cls, name):
        return cls._registry.get(name)
    
    @classmethod
    def list_classes(cls):
        return list(cls._registry.keys())

class RegisteredClass1(metaclass=RegistryMeta):
    pass

class RegisteredClass2(metaclass=RegistryMeta):
    pass

print(f"Registered classes: {RegistryMeta.list_classes()}")
print(f"Get RegisteredClass1: {RegistryMeta.get_class('RegisteredClass1')}")

# 7. Advanced Metaclass Techniques
print("\n=== Advanced Metaclass Techniques ===")

# Metaclass with method modification
class MethodModificationMeta(type):
    """Metaclass that modifies methods"""
    
    def __new__(cls, name, bases, attrs):
        # Modify all methods to add logging
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                attrs[attr_name] = cls._add_logging(attr_value)
        
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _add_logging(func):
        def wrapper(self, *args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(self, *args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper

class LoggedClass(metaclass=MethodModificationMeta):
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

logged = LoggedClass()
print("Testing logged methods:")
result1 = logged.add(5, 3)
result2 = logged.multiply(4, 6)

# Metaclass with attribute access control
class AttributeControlMeta(type):
    """Metaclass that controls attribute access"""
    
    def __new__(cls, name, bases, attrs):
        # Add property-like behavior to all attributes
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('_') and not callable(attr_value):
                attrs[attr_name] = property(
                    lambda self, name=attr_name: getattr(self, f'_{name}', None),
                    lambda self, value, name=attr_name: setattr(self, f'_{name}', value)
                )
        
        return super().__new__(cls, name, bases, attrs)

class ControlledClass(metaclass=AttributeControlMeta):
    def __init__(self):
        self._value = None

controlled = ControlledClass()
controlled.value = "test"
print(f"Controlled value: {controlled.value}")

# 8. Metaclass Best Practices
print("\n=== Metaclass Best Practices ===")

# Best Practice 1: Use metaclasses sparingly
# Metaclasses are powerful but can make code hard to understand

# Best Practice 2: Document metaclass behavior
class DocumentedMeta(type):
    """
    A well-documented metaclass.
    
    This metaclass provides additional functionality to classes.
    It adds a class attribute 'meta_info' with creation details.
    """
    
    def __new__(cls, name, bases, attrs):
        attrs['meta_info'] = {
            'created_by': cls.__name__,
            'creation_time': '2024-01-15',
            'base_classes': [base.__name__ for base in bases]
        }
        return super().__new__(cls, name, bases, attrs)

class DocumentedClass(metaclass=DocumentedMeta):
    pass

print(f"Documented class meta_info: {DocumentedClass.meta_info}")

# Best Practice 3: Use __init_subclass__ when possible
class BaseClass:
    """Base class using __init_subclass__ instead of metaclass"""
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry_name = cls.__name__
        print(f"Subclass created: {cls.__name__}")

class SubClass(BaseClass):
    pass

print(f"SubClass registry_name: {SubClass.registry_name}")

# Best Practice 4: Consider alternatives to metaclasses
# Use decorators, __init_subclass__, or composition instead

# 9. Real-world Metaclass Examples
print("\n=== Real-world Metaclass Examples ===")

# Example 1: ORM Metaclass
class ORMMeta(type):
    """Metaclass for Object-Relational Mapping"""
    
    def __new__(cls, name, bases, attrs):
        # Collect field definitions
        fields = {}
        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, '_field_type'):
                fields[attr_name] = attr_value
        
        # Create the class
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._fields = fields
        new_class._table_name = name.lower()
        
        return new_class

class Field:
    def __init__(self, field_type):
        self._field_type = field_type

class StringField(Field):
    def __init__(self):
        super().__init__('VARCHAR')

class IntegerField(Field):
    def __init__(self):
        super().__init__('INTEGER')

class User(metaclass=ORMMeta):
    name = StringField()
    age = IntegerField()

print(f"User table name: {User._table_name}")
print(f"User fields: {User._fields}")

# Example 2: API Endpoint Metaclass
class APIEndpointMeta(type):
    """Metaclass for API endpoint classes"""
    
    def __new__(cls, name, bases, attrs):
        # Collect endpoint methods
        endpoints = {}
        for attr_name, attr_value in attrs.items():
            if hasattr(attr_value, '_endpoint_info'):
                endpoints[attr_name] = attr_value._endpoint_info
        
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._endpoints = endpoints
        
        return new_class

def endpoint(method, path):
    """Decorator for API endpoints"""
    def decorator(func):
        func._endpoint_info = {'method': method, 'path': path}
        return func
    return decorator

class UserAPI(metaclass=APIEndpointMeta):
    @endpoint('GET', '/users')
    def get_users(self):
        return "List of users"
    
    @endpoint('POST', '/users')
    def create_user(self):
        return "User created"

print(f"UserAPI endpoints: {UserAPI._endpoints}")

# Example 3: Configuration Metaclass
class ConfigMeta(type):
    """Metaclass for configuration classes"""
    
    def __new__(cls, name, bases, attrs):
        # Collect configuration options
        config_options = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('_') and not callable(attr_value):
                config_options[attr_name] = attr_value
        
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._config_options = config_options
        
        return new_class

class DatabaseConfig(metaclass=ConfigMeta):
    host = 'localhost'
    port = 5432
    database = 'myapp'
    username = 'user'
    password = 'password'

print(f"Database config options: {DatabaseConfig._config_options}")

# 10. Metaclass Alternatives
print("\n=== Metaclass Alternatives ===")

# Alternative 1: Decorators
def singleton(cls):
    """Singleton decorator"""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class SingletonDecorated:
    def __init__(self, value):
        self.value = value

s1 = SingletonDecorated("first")
s2 = SingletonDecorated("second")
print(f"Singleton decorated: {s1 is s2}")

# Alternative 2: __init_subclass__
class BaseWithInitSubclass:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.class_info = f"Created from {cls.__name__}"

class SubWithInitSubclass(BaseWithInitSubclass):
    pass

print(f"Subclass info: {SubWithInitSubclass.class_info}")

# Alternative 3: Composition
class Registry:
    """Registry using composition"""
    
    def __init__(self):
        self._registry = {}
    
    def register(self, name, obj):
        self._registry[name] = obj
    
    def get(self, name):
        return self._registry.get(name)

registry = Registry()
registry.register('test', 'value')
print(f"Registry value: {registry.get('test')}")

# 11. Metaclass Debugging
print("\n=== Metaclass Debugging ===")

class DebugMeta(type):
    """Metaclass with debugging capabilities"""
    
    def __new__(cls, name, bases, attrs):
        print(f"DEBUG: Creating class {name}")
        print(f"DEBUG: Bases: {bases}")
        print(f"DEBUG: Attributes: {list(attrs.keys())}")
        
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(cls, name, bases, attrs):
        print(f"DEBUG: Initializing class {name}")
        super().__init__(name, bases, attrs)
    
    def __call__(cls, *args, **kwargs):
        print(f"DEBUG: Calling class {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        print(f"DEBUG: Instance created: {instance}")
        return instance

class DebugClass(metaclass=DebugMeta):
    def __init__(self, value):
        self.value = value

print("Creating DebugClass instance:")
debug_instance = DebugClass("test")

# 12. Metaclass Performance Considerations
print("\n=== Metaclass Performance Considerations ===")

import time

# Simple metaclass
class SimpleMeta(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)

# Complex metaclass
class ComplexMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add multiple attributes
        attrs['attr1'] = 'value1'
        attrs['attr2'] = 'value2'
        attrs['attr3'] = 'value3'
        
        # Modify methods
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = lambda self, *args, **kwargs: attr_value(self, *args, **kwargs)
        
        return super().__new__(cls, name, bases, attrs)

# Performance test
def test_metaclass_performance():
    start_time = time.time()
    
    for i in range(1000):
        class TestClass(metaclass=SimpleMeta):
            pass
    
    simple_time = time.time() - start_time
    
    start_time = time.time()
    
    for i in range(1000):
        class TestClass(metaclass=ComplexMeta):
            pass
    
    complex_time = time.time() - start_time
    
    print(f"Simple metaclass time: {simple_time:.4f}s")
    print(f"Complex metaclass time: {complex_time:.4f}s")

test_metaclass_performance()

# Exercises:
"""
1. Create a metaclass that automatically adds a 'created_at' attribute to classes
2. Write a metaclass that enforces method naming conventions
3. Create a metaclass that automatically generates getter and setter methods
4. Write a metaclass that tracks all instances of a class
5. Create a metaclass that adds logging to all methods
"""

# Exercise Solutions:
print("\n--- Exercise Solutions ---")

# 1. Created_at metaclass
print("Exercise 1: Created_at Metaclass")
class CreatedAtMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['created_at'] = '2024-01-15'
        return super().__new__(cls, name, bases, attrs)

class TimestampedClass(metaclass=CreatedAtMeta):
    pass

print(f"TimestampedClass created_at: {TimestampedClass.created_at}")

# 2. Method naming convention metaclass
print("\nExercise 2: Method Naming Convention Metaclass")
class NamingConventionMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                if not attr_name.islower():
                    raise ValueError(f"Method '{attr_name}' must be lowercase")
        return super().__new__(cls, name, bases, attrs)

class ConventionClass(metaclass=NamingConventionMeta):
    def valid_method(self):
        return "Valid method"
    
    # This would raise an error:
    # def InvalidMethod(self):
    #     return "Invalid method"

# 3. Getter/setter metaclass
print("\nExercise 3: Getter/Setter Metaclass")
class PropertyMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('_') and not callable(attr_value):
                # Create getter and setter
                getter_name = f'get_{attr_name}'
                setter_name = f'set_{attr_name}'
                
                attrs[getter_name] = property(lambda self, name=attr_name: getattr(self, f'_{name}', None))
                attrs[setter_name] = property(lambda self, value, name=attr_name: setattr(self, f'_{name}', value))
        
        return super().__new__(cls, name, bases, attrs)

class PropertyClass(metaclass=PropertyMeta):
    def __init__(self):
        self._value = None

prop_class = PropertyClass()
prop_class.set_value = "test"
print(f"Property value: {prop_class.get_value}")

# 4. Instance tracking metaclass
print("\nExercise 4: Instance Tracking Metaclass")
class InstanceTrackingMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_instances'] = []
        return super().__new__(cls, name, bases, attrs)
    
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        cls._instances.append(instance)
        return instance

class TrackedClass(metaclass=InstanceTrackingMeta):
    def __init__(self, value):
        self.value = value

t1 = TrackedClass("first")
t2 = TrackedClass("second")
print(f"Tracked instances: {len(TrackedClass._instances)}")

# 5. Logging metaclass
print("\nExercise 5: Logging Metaclass")
class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                attrs[attr_name] = cls._add_logging(attr_value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _add_logging(func):
        def wrapper(self, *args, **kwargs):
            print(f"LOG: Calling {func.__name__}")
            result = func(self, *args, **kwargs)
            print(f"LOG: {func.__name__} returned {result}")
            return result
        return wrapper

class LoggedClass(metaclass=LoggingMeta):
    def add(self, a, b):
        return a + b

logged = LoggedClass()
result = logged.add(5, 3)

print("\n🎉 Congratulations! You've completed Lesson 25!")
print("Next: Lesson 26 - Asynchronous Programming")
