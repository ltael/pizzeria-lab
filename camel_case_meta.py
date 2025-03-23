class CamelCaseMeta(type):
    def __new__(cls, name, bases, dct):
        # Split the string by common separators (space, underscore, hyphen)
        words = name.replace("-", " ").replace("_", " ").split()
        capitalized_name = "".join(word.capitalize() for word in words)

        return super().__new__(cls, capitalized_name, bases, dct)