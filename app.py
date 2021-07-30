#!/usr/bin/env python3

from aws_cdk import core

from my_cdkworkshop_python.my_cdkworkshop_python_stack import MyCdkworkshopPythonStack


app = core.App()
MyCdkworkshopPythonStack(app, "my-cdkworkshop-python")

app.synth()
