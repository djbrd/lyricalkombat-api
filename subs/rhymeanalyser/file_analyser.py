from .analyser import Analyser

class FileAnalyser():

    def __init__(self, file_name):
        self.file_name = file_name
        self.analysers = []
        lines = []
        with open(self.file_name, 'r') as file:
            for line in file:
                if line == '\n':
                    if len(lines):
                        self.analysers.append(Analyser(''.join(lines)))
                        lines = []
                else:
                    lines.append(line)

        if len(lines):
            self.analysers.append(Analyser(''.join(lines)))


    def process(self):
        for analyser in self.analysers:
            analyser.process()
        self.create_html()


    def create_html(self):
        f = open('verses.html', 'w')
        f.write('<html>'
                '\t<head></head>'
                '\t<body style="font-size:150%">')

        for analyser in self.analysers:
            f.write('\t\t<p>')
            f.write(analyser.marked_up)
            f.write('\t\t</p>')

        f.write('\t</body>'
                '</html>')
        f.close()

