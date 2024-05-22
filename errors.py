class DataPreprocessingError(Exception):
    """Exception raised for errors in data preprocessing.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error occurred during data preprocessing."):
        self.message = message
        super().__init__(self.message)


class ModelTrainingError(Exception):
    """Exception raised for errors in model training.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error occurred during model training."):
        self.message = message
        super().__init__(self.message)


class ModelEvaluationError(Exception):
    """Exception raised for errors in model evaluation.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Error occurred during model evaluation."):
        self.message = message
        super().__init__(self.message)
