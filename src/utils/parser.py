from src.utils import ExecutableUtil


class Parser(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.parse(*args)
    
    def parse(self, data):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement parse in %s.' % (self.__class__.__name__))
