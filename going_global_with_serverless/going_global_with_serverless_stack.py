from aws_cdk import (
        aws_lambda as _lambda,
        aws_dynamodb as dynamodb,
        aws_apigateway as apigw,
        aws_certificatemanager as acm,
        aws_route53 as r53,
        core
        )

class GoingGlobalWithServerlessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,table='', **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        # --- table import ---
        globalddb = dynamodb.Table.from_table_name(self, "global_ddb_import", table)

        # --- zone import ---

        dns_zone = r53.HostedZone.from_lookup(
                self, "dns_zone",
                domain_name="rup12.net"
                )

        cert = acm.Certificate(
                self, "certificate",
                domain_name="openconf.rup12.net",
                validation=acm.CertificateValidation.from_dns(dns_zone)
                )

        # --- lambdas ---
        fn = _lambda.Function(
                self, "main-lambda",
                runtime=_lambda.Runtime.PYTHON_3_8,
                code=_lambda.Code.asset("lambda"),
                handler='index.handler',
                environment={
                        "table": globalddb.table_name
                    }
                )

        hc_fn = _lambda.Function(
                self, "health-lambda",
                runtime=_lambda.Runtime.PYTHON_3_8,
                code=_lambda.Code.asset("lambda"),
                handler='health.handler'
                )

        # --- api gateway ---
        api = apigw.RestApi(
                self, "rest-api",
                rest_api_name="going-global-APIGW",
                domain_name={
                    "domain_name":"openconf.rup12.net",
                    "certificate":cert
                    },
                description="API Gateway to be used during the GoingGlobalWithServerless talk"
                )
        api_hello = api.root.add_resource("hello")
        api_health = api.root.add_resource("health")

        mainfninteg = apigw.LambdaIntegration(fn)
        healthfninteg = apigw.LambdaIntegration(hc_fn)

        api_hello.add_method("GET", mainfninteg)
        api_health.add_method("GET", healthfninteg)

        # --- permissions ----
        globalddb.grant_read_write_data(fn)

