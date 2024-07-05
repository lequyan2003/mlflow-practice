import dagshub
import mlflow

dagshub.init(
  repo_owner='lequyan2003',
  repo_name='mlflow-practice',
  mlflow=True
)


with mlflow.start_run():
    mlflow.log_param('parameter name', 'value')
    mlflow.log_metric('metric name', 1)
