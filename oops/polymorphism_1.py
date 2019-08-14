class Document:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'

class Word(Document):
    def show(self):
        return 'Show word contents!'

documents = [Pdf('I am PDF Doc'),Word('I am Word Doc')]

for document in documents:
    print(document.name + ': ' + document.show())