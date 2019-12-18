# -*- coding: utf-8 -*-
class LoggerSymbols:
    QUANTITY_ASTERISK = 10
    ETL = "etl"
    PREDICT = "predict"
    POST_PROCESS = "post_process"


class ApiLogConstants:
    QAS = "qas"
    PRD = "prd"
    PENDING = "Pendiente"
    FINISHED = "Terminado"
    FAILED = "Fallida"
    STARTED = "Iniciada"

    SUBS_4C_COUNTRIES = "'PE','CR','CO','CL'"
    UNSUBS_DATA_PREP_COUNTRIES = "'CO', 'CL', 'CR', 'PE', 'PA', 'MX', 'SV', 'GT', 'BO', 'DO', 'EC'"
    SUBS_PHYSICAL_DATAPREP_COUNTRIES = "'CR','CO','PE','CL'"
    UNSUBS_PHYSICAL_DATAPREP_COUNTRIES = "'CR','CO','PE','CL','EC','DO','GT','SV','BO','MX','PA'"
    SUB_PRODUCT_AFFINITY_DIGITAL_TRAIN_SEL_COUNTRIES = "'PE','CR','CO','CL'"


class FormatData:
    PARQUET = "parquet"
    CSV = "csv"


class SparkPerformanceData:
    BROADCAST = 1
    CACHE = 2
    DEFAULT = 0
