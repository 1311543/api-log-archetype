import configparser
import uuid
import os

from belc_log.domain.logger import LoggerBDI
from belc_log.repository.apilog_session_repository import LoggingBDISession
from belc_log.service.bdi_service import BdiService


class LoggingBDI:
    def __init__(self,
                 env,
                 app_name,
                 service,
                 country,
                 type_execution):
        self.env = env
        self.app_name = app_name
        self.config = configparser.RawConfigParser()
        self.config.read(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'config/config.ini'))
        self.session = self.create_session_bdi(env,
                                               app_name,
                                               service,
                                               country,
                                               type_execution)

    def create_session_bdi(self,
                           env,
                           app_name,
                           service,
                           country,
                           type_execution):
        try:
            looger = LoggerBDI(
                id=str(uuid.uuid4()),
                env=env,
                app_name=app_name,
                service=service,
                time_format='%Y-%m-%dT%H:%M:%SZ',
                country=self.config.get('COUNTRY-EQUIVALENCE',
                                        country),
                type_execution=type_execution,
                api_log_address=self.create_endpoint(),
                config=self.config)
            return BdiService(LoggingBDISession(), looger)
        except Exception as e:
            print('\n\n>>> Error Creating Api BDI Session : {}'.format(e))

    def create_session(self):
        return self.session.create_bdi_session()

    def update_session(self):
        return self.session.update_session()

    def done_session(self):
        return self.session.done_session()

    def failed_session(self, message):
        return self.session.failed_session(message)

    def add_event(self,
                  type_event,
                  event,
                  initial_datetime,
                  final_datetime,
                  message):
        return self.session.add_event(type_event,
                                      event,
                                      initial_datetime,
                                      final_datetime,
                                      message)

    def create_endpoint(self):
        return 'http://{}:{}'.format(self.config.get('API-LOG-ADDRESS-{}'.format(self.env), 'IP'),
                                     self.config.get('API-LOG-ADDRESS-{}'.format(self.env), 'PORT'))
