import re

from .ProgrammingLanguage import ProgrammingLanguage


class SwiftPL(ProgrammingLanguage):
    def get_code_quality(self):
        pass

    def get_code_lifetime(self):
        pass

    def extract_imports(self, lines):
        pattern = r'import\s+([\w.]+)'
        libraries = []
        for line in lines:
            matches = re.findall(pattern, line)
            library_names = [match for match in matches]
            libraries.extend(library_names)
        return libraries
