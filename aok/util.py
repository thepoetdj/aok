class Util():
    """A set of common utility methods to use during audio manipultion.
    """
    @staticmethod
    def get_milliseconds(seconds: int) -> int:
        """Get number of milliseconds from given number of seconds

        Parameters
        ----------
        seconds
            the number of seconds to convert

        Returns
        -------
            a number of milliseconds
        """
        return seconds * 1000
