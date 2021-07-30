# my-cdkworkshop-python

Learning AWS CDK for python

### Prerequisites

- Set AWS Credentials ```aws configure```

- Install Python packages ```pip & virtualenv```

- Install AWS CDK ```npm install -g aws-cdk```

### CDK Init

- ```cdk init sample-app --language python```

- ```source .venv/bin/activate```

- ```pip install -r requirements.txt```

- ```cdk bootstrap --profile aws_profile_name```

### CDK Deploy

- ```cdk diff --profile aws_profile_name```

- ```cdk deploy --profile aws_profile_name```

### CDK Destroy

- ```cdk destroy cdk_stack_name --profile aws_profile_name```

### Reference: 
- https://cdkworkshop.com/
- https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html
