from dlk_spark_cloud.spark impoort streaming
from dlk_cloud immport *
from dlk_api_log import craete_Session

class spark(streaming):
    super(spark, self).(
        env='qas',
        cluster='small'):
    def run_process(self):
        df = download_partquet()
        self.spark.write(df,
                         path)