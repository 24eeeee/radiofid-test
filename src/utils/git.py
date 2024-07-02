from src.utils import ExecutableUtil


class Git(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.add(*args)
        self.commit()
    
    def add(self, data):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement add in %s.' % (self.__class__.__name__))
    
    def commit(self):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        raise NotImplementedError('Implement commit in %s.' % (self.__class__.__name__))
