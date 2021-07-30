from aws_cdk import (
    aws_lambda,
    aws_apigateway,
    core
)


class MyCdkworkshopPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = aws_lambda.Function(
            self, 'HelloHandler',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.asset('lambda'),
            handler='hello.handler',
        )
        
        my_apigateway = aws_apigateway.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )