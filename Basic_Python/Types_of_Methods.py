class Method:
    test="I am Class Method Test"
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
    
    @classmethod
    def class_method(cls):
        return cls.test
    
    @staticmethod
    def static_method():
        return "I am a static method"

    def instance_method(self):
        return f"I am an instance method of {self.name}"

if __name__ == "__main__":
    a=Method("maneesh",23)
    print(a.instance_method())
    print(a.class_method())
    print(a.static_method())
    Method.test = "test"
    print(a.class_method())