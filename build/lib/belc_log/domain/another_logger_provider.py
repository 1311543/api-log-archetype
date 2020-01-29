class LoggerOtherProvider:
    def __init__(self,
                 id,
                 env,
                 app_name,
                 service,
                 time_format,
                 country,
                 type_execution,
                 api_log_address,
                 config):
        self.id = id
        self.env = env
        self.app_name = app_name
        self.service = service
        self.time_format = time_format
        self.country = country
        self.type_execution = type_execution
        self.api_log_address = api_log_address
        self.config = config
