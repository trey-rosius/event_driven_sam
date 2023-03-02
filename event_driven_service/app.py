from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import AppSyncResolver
from aws_lambda_powertools.metrics import MetricUnit

logger = Logger(service="EventDrivenSAMApi")
tracer = Tracer(service="EventDrivenSAMApi")
metrics = Metrics(namespace="MyEventDrivenSAMApi", service="EventDrivenSAMApi")
app = AppSyncResolver()


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPSYNC_RESOLVER, log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    logger.debug(f'event is {event}')
    return app.resolve(event, context)
