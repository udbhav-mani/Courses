class PrinterError(RuntimeError):
    pass

class Printer():
    def __init__(self, pages_pers: int, capacity:int) -> None:
        self.pages_pers = pages_pers
        self.capacity = capacity
    
    def print(self, pages):
        if(pages > self.capacity):
            raise PrinterError("Printer doesnot have enough capacity! ")
        
        self.capacity -= pages
        return f"Printer printed {pages} pages in {pages/self.pages_pers:.2f} seconds."