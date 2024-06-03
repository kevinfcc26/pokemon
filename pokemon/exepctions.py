class ProviderException(Exception):
    """Custom exception to external requests"""

    def __init__(self, message="") -> None:
        self.message = message
