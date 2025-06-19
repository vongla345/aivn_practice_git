class Dataloader:
    def __init__(self, data):
        self.data = data
        
    def __call__(self):
        print(self.data)
        
    def add_child(self, child):
        self.data.append(child)
        
def main():
    dataloader = Dataloader([])
    dataloader.add_child(1)
    
if __name__ == '__main__':
    main()