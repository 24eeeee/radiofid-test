import re

from src.utils import ExecutableUtil


class Validator(ExecutableUtil):
    """
    DOCUMENTME
    """
    pattern = re.compile(r"""^[a-zA-Z\d\.]+$""")

    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.validate(*args)
    
    def validate(self, word: str) -> str | bool:
        """
        По переданному слову возвращает True, если слово может быть допущено,
        строку ошибки если слово не допущено.

        Args:
            word: слово для проверки.
        """
        if len(word) < 3:
            return 'Word must be longer then 3 symbols'
        if not re.match(self.pattern, word):
            return 'Only latin letters, digits and dots'
        if '..' in word:
            return 'Two dots in a row'
        return True
