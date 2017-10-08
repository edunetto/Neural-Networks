###### This is my first perceptron ######

###### Classes
class MyClass(object):
    # class variable
    my_CLS_var = 10
    # sets "init'ial" state to objects/instances, use self argument

    def __init__(self):
        # self usage => insta   nce variable (per object)
        self.my_OBJ_var = 15
        # also possible, class name is used => init class variable
        MyClass.my_CLS_var = 20

##### Functions
def run_example_func():
    # PRINTS    10    (class variable)
    print(MyClass.my_CLS_var)
    # executes __init__ for obj1 instance
    # NOTE: __init__ changes class variable above
    obj1 = MyClass()
    # PRINTS    15    (instance variable)
    print(obj1.my_OBJ_var)
    # PRINTS    20    (class variable, changed value)
    print(MyClass.my_CLS_var)
    return

### Executable code
run_example_func()
