

class NewFile:
    def __init__(self, file_name, line_iterator, content):
       self.file_name = file_name
       self.line_iterator = line_iterator
       self.content = content

    def get_content(self):
        self.file_name = open(self.file_name, 'r')
        self.content = self.file_name.readlines()

    def get_string(self):
        self.line_iterator += 1
        return self.content[self.line_iterator]
    
    def get_len(self):
        return len(self.content)
        
