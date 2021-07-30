# my-cdkworkshop-python

Learning AWS CDK for python

### Prerequisites

- Set ```aws configure```
- Install ```pip & virtualenv```
- Install CDK ```npm install -g aws-cdk```

  Reference: https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_prerequisites

### CDK Init

```cdk init sample-app --language python```

```source .venv/bin/activate```

```pip install -r requirements.txt```

### CDK Deploy

```cdk bootstrap --profile aws_profile_name```

```cdk diff --profile aws_profile_name```

```cdk deploy --profile aws_profile_name```

### CDK Destroy

```cdk destroy cdk_stack_name --profile aws_profile_name```