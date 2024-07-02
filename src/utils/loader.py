from src.utils import ExecutableUtil


class Loader(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.load(*args)
    
    def load(self, link):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement load in %s.' % (self.__class__.__name__))
