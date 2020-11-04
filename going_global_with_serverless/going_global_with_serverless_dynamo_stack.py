from aws_cdk import (
        aws_dynamodb as dynamodb,
        core
        )

class GoingGlobalWithServerlessDynamoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        global_table= dynamodb.Table(
                self, "global_table",
                partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
                replication_regions=[ "us-west-1", "ap-northeast-1"],
                table_name="openit_globalddb_demo"
                )

        self.table = global_table.table_name


