import json
import pytest

from aws_cdk import core
from my-cdkworkshop-python.my_cdkworkshop_python_stack import MyCdkworkshopPythonStack


def get_template():
    app = core.App()
    MyCdkworkshopPythonStack(app, "my-cdkworkshop-python")
    return json.dumps(app.synth().get_stack("my-cdkworkshop-python").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
