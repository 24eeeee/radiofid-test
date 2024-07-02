from src.utils import ExecutableUtil


class Beautifier(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.beautify(*args)
    
    def beautify(self, word):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement beautify in %s.' % (self.__class__.__name__))
