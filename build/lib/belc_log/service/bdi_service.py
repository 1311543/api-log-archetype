from belc_log.domain.logger import LoggerBDI
from belc_log.repository.apilog_session_repository import ApiLogSessionRepository


class BdiService:
    def __init__(self,
                 apilog_session: ApiLogSessionRepository,
                 logger: LoggerBDI):
        self.apilog_session = apilog_session
        self.logger = logger

    def create_bdi_session(self):
        return self.apilog_session.createSession(self.logger)

    def update_session(self):
        return self.apilog_session.update_session(self.logger)

    def done_session(self):
        return self.apilog_session.done_session(self.logger)

    def failed_session(self, message):
        setattr(self.logger, 'message', message)
        return self.apilog_session.failed_session(self.logger)

    def add_event(self, type_event, event, initial_datetime, final_datetime, message):
        setattr(self.logger, 'type_event', type_event)
        setattr(self.logger, 'event', event)
        setattr(self.logger, 'initial_datetime', initial_datetime)
        setattr(self.logger, 'final_datetime', final_datetime)
        setattr(self.logger, 'message', message)
        return self.apilog_session.add_event(self.logger)
