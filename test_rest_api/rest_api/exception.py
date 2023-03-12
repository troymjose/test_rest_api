from test_rest_api.utils.error_msg import ErrorMsg


class RestApiConfigException(Exception):
    """
    Exception raised for returning invalid rest api json in @rest_api decorated functions
    """

    def __init__(self, *, name: str, module: str, config: dict, parent_exception: str = ''):
        self.name, self.module, self.config, self.parent_exception = name, module, config, parent_exception
        self.message = f"""
                        {self.name} ({self.module})
                        {self.parent_exception}
                        {ErrorMsg.INVALID_REST_API}
                        """
        super().__init__(self.message)


class RestApiSendException(Exception):
    """
    Exception raised for unexpected errors while sending the api request
    """

    def __init__(self, *, parent_exception: str = ''):
        self.parent_exception = parent_exception
        self.message = f"""
                        {self.parent_exception}
                        {ErrorMsg.SEND_EXCEPTION}
                        """
        super().__init__(self.message)
