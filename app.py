#!/usr/bin/env python3

from aws_cdk import core

from going_global_with_serverless.going_global_with_serverless_stack import GoingGlobalWithServerlessStack
from going_global_with_serverless.going_global_with_serverless_dynamo_stack import GoingGlobalWithServerlessDynamoStack


app = core.App()

# --- database ---
global_ddb = GoingGlobalWithServerlessDynamoStack(app, "global-table-stack",
        env=core.Environment(account="824852318651", region="eu-west-1")
        )
# --- regional stacks ---
# Ireland
GoingGlobalWithServerlessStack(app, "ireland-stack",
        table=global_ddb.table, 
        env=core.Environment(account="824852318651", region="eu-west-1")
        )
# Japan
GoingGlobalWithServerlessStack(app, "japan-stack",
        table=global_ddb.table,
        env=core.Environment(account="824852318651", region="ap-northeast-1")
        )
# California
GoingGlobalWithServerlessStack(app, "california-stack", 
        table=global_ddb.table, 
        env=core.Environment(account="824852318651", region="us-west-1")
        )

app.synth()
