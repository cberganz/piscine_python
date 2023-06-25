class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []
        self.headers = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            lines = self.file.readlines()
            for line in lines:
                row = line.strip().split(self.sep)
                if "" in row:
                    return None
                self.data.append(row)
            if self.header:
                self.headers = self.data[0]
                self.data = self.data[1:]
            self.data = self.data[self.skip_top:]
            if self.skip_bottom > 0:
                self.data = self.data[:-self.skip_bottom]
            for row in self.data:
                if len(row) != len(self.data[0]):
                    return None
            return self
        except FileNotFoundError:
            print("File not found.")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.headers
