class FastaFile:
    def __init__(self, file):
        self._file = file

    @property
    def file(self):
        return self._file
    
    def get_seq_record(self, sequence_class):
        with open(self.file) as filehandle:
            for line in filehandle:
                if line.startswith('>'):
                    id = line.rstrip().lstrip('>')
                    seq = next(filehandle).rstrip()
                yield sequence_class(id, seq)    