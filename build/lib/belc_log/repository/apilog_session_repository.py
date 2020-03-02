import json
import socket
from abc import ABC, abstractmethod
from datetime import datetime

import requests
from requests.exceptions import HTTPError

from belc_log.domain.logger import LoggerBDI
from belc_log.utils.constants import ApiLogConstants as alc


class ApiLogSessionRepository(ABC):
    @abstractmethod
    def createSession(self, logger: LoggerBDI) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def update_session(self, logger: LoggerBDI) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def done_session(self, logger: LoggerBDI) -> None:
        """Add method to be implemented."""
        pass

    @abstractmethod
    def failed_session(self, logger: LoggerBDI) -> None:
        """Add method to be implemented."""
        pass

    def add_event(self, logger: LoggerBDI) -> None:
        """Add method to be implemented."""
        pass


class LoggingBDISession(ApiLogSessionRepository):
    def createSession(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/' + logger.id

            timestamp = datetime.utcnow().strftime(logger.time_format)

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            user_execution = s.getsockname()[0]
            s.close()

            headers = {'Content-type': 'application/json'}

            data = {
                "app": logger.app_name,
                "servicio": logger.service,
                "codigoPais": logger.country,
                "estadoEjecucion": alc.PENDING,
                "tipoEjecucion": logger.type_execution,
                "usuarioEjecucion": user_execution,
                "fechaInicio": timestamp,
                "input": {"TiempoEspera": "2000"},
                "output": {}
            }
            response = requests.post(endpoint,
                                     data=json.dumps(data),
                                     headers=headers,
                                     timeout=5)

            response.raise_for_status()
        except HTTPError as http_err:
            print('\n\n>>>HTTP error occurred:'.format(http_err))
        except Exception as err:
            print('\n\n>>>Error Creating Api Session: '.format(err))
        else:
            print('Success!')

    def update_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/' + logger.id

            headers = {'Content-type': 'application/json'}

            data = {
                "estadoEjecucion": alc.STARTED
            }

            response = requests.put(endpoint,
                                    data=json.dumps(data),
                                    headers=headers,
                                    timeout=5)
            response.raise_for_status()
        except HTTPError as http_err:
            print('\n\n>>>HTTP error occurred:'.format(http_err))
        except Exception as err:
            print('\n\n>>> Filed Update session : {}'.format(err))
        else:
            print('Success!')

    def done_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/done/' + logger.id

            timestamp = datetime.utcnow().strftime(logger.time_format)

            headers = {'Content-type': 'application/json'}

            data = {
                "fechaFin": timestamp
            }

            response = requests.post(endpoint,
                                     data=json.dumps(data),
                                     headers=headers,
                                     timeout=5)
            response.raise_for_status()

        except HTTPError as http_err:
            print('\n\n>>>HTTP error occurred:'.format(http_err))
        except Exception as err:
            print('\n\n>>> Filed Done session : {}'.format(err))
        else:
            print('Success!')

    def failed_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/error/' + logger.id

            timestamp = datetime.utcnow().strftime(logger.time_format)

            headers = {'Content-type': 'application/json'}

            data = {
                "fechaFin": timestamp,
                "mensaje": logger.message
            }

            response = requests.post(endpoint,
                                     data=json.dumps(data),
                                     headers=headers,
                                     timeout=5)
            response.raise_for_status()

        except HTTPError as http_err:
            print('\n\n>>>HTTP error occurred:'.format(http_err))
        except Exception as err:
            print('\n\n>>> Filed Session : {}'.format(err))
        else:
            print('Success!')

    def add_event(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/add/' + logger.id

            headers = {'Content-type': 'application/json'}

            data = {
                "fechaEjecucion": logger.initial_datetime.strftime(logger.time_format),
                "fechaInicio": logger.final_datetime.strftime(logger.time_format),
                "tipoEvento": logger.type_event,
                "evento": logger.event,
                "duracion": str(round(
                    (logger.final_datetime - logger.initial_datetime).total_seconds() * 1000)),
                "mensaje": logger.message
            }

            response = requests.post(endpoint,
                                     data=json.dumps(data),
                                     headers=headers,
                                     timeout=5)
            response.raise_for_status()

        except HTTPError as http_err:
            print('\n\n>>>HTTP error occurred:'.format(http_err))
        except Exception as err:
            print('\n\n>>> Filed Add Event : {}'.format(err))
        else:
            print('Success!')


class AnotherApiLogSessionRepository(ApiLogSessionRepository):
    def createSession(self, logger: LoggerBDI) -> None:
        try:
            pass
        except Exception as e:
            print('\n\n>>>Error Creating Api Session'
                  ' : {}'.format(e.message))

    def update_session(self, logger: LoggerBDI) -> None:
        pass

    def done_session(self, logger: LoggerBDI) -> None:
        pass

    def failed_session(self, logger: LoggerBDI):
        pass
