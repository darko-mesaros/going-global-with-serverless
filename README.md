# Going Global With Serverless Demo Repository

Hello and welcome to this repository, I hope you have enjoyed the talk (or did
you? 🤔). In any case, this repository contains the required CDK code to deploy
the required elements of a global serverless application. 

If executed succesfully, this will deploy the following:
- DynamoDB table (with Global tables in Ireland, Tokyo, and California)
- 3 REST API Gateways (1 per region)
- 6 Lambda Functions (2 per region)
- Three Certificates in ACM (1 per region)

The only manual part of this demo is the Route53 creation - that was
intentionally left out, as I wanted to demonstrate that during the demo (I may
add that in the future). 

There are a few things you need to change:
- The domain name to be used - currently it is set to `rup12.net`
- The account ID, currently I have it set to my own account.

As this CDK project is written in python, make sure to use `virualenv` to
install all the required modules.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

### Deploying

To deploy the stack, you need to do it in order. After you have made all the
necessary changes to your templates, create your DynamoDB stack first:

```
$ cdk deploy global-table-stack
```

Then You can go ahead and deploy the rest of the stacks (You can do it one by
one, or all at once, your call):

```
$ cdk deploy {ireland,japan,california}-stack -O outputs.json
```
