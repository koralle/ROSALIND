import re
class Transcription():

    def transctiprion(self, dna_string):
        self.rna_string = re.sub("T", "U", dna_string)
        return (self.rna_string)

