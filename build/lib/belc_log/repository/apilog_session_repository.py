from abc import ABC, abstractmethod
from belc_log.domain.logger import LoggerBDI
from belc_log.utils.constants import ApiLogConstants as alc
from datetime import datetime
import requests
import socket
import json


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

            return requests.post(endpoint,
                                 data=json.dumps(data),
                                 headers=headers,
                                 timeout=5)
        except Exception as e:
            print('\n\n>>> Error Creating Api Session : {}'.format(e))

    def update_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/' + logger.id

            headers = {'Content-type': 'application/json'}

            data = {
                "estadoEjecucion": alc.STARTED
            }

            return requests.put(endpoint,
                                data=json.dumps(data),
                                headers=headers,
                                timeout=5)
        except Exception as e:
            print('\n\n>>> Filed Update session : {}'.format(e))

    def done_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/done/' + logger.id

            timestamp = datetime.utcnow().strftime(logger.time_format)

            headers = {'Content-type': 'application/json'}

            data = {
                "fechaFin": timestamp
            }

            return requests.post(endpoint,
                                 data=json.dumps(data),
                                 headers=headers,
                                 timeout=5)
        except Exception as e:
            print('\n\n>>> Filed Done session : {}'.format(e))

    def failed_session(self, logger: LoggerBDI):
        try:
            endpoint = logger.api_log_address + '/error/' + logger.id

            timestamp = datetime.utcnow().strftime(logger.time_format)

            headers = {'Content-type': 'application/json'}

            data = {
                "fechaFin": timestamp,
                "mensaje": logger.message
            }

            return requests.post(endpoint,
                                 data=json.dumps(data),
                                 headers=headers,
                                 timeout=5)
        except Exception as e:
            print('\n\n>>> Filed Session : {}'.format(e))

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

            return requests.post(endpoint, data=json.dumps(data), headers=headers, timeout=5)
        except Exception as e:
            print('\n\n>>> Filed Add Event : {}'.format(e))


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
