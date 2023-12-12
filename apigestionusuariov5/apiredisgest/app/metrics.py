from prometheus_flask_exporter import PrometheusMetrics

def init_metrics(app):
    metrics = PrometheusMetrics(app)
    metrics.info('app_info', 'Application info', version='1.0.3')
