# Chalice with CDK

Chalice with CDK. This application is deployed using the AWS CDK.

For more information, see the [Deploying with the AWS CDK] tutorial.

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/chalice-with-cdk.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
pip install -r requirements.txt
```

## Quickstart

First, you'll need to install the AWS CDK if you haven't already. The
CDK requires Node.js and npm to run. See the [Getting started with the
AWS CDK] for more details.

    $ npm install -g aws-cdk

There's also separate requirements files in the `infrastructure` and
`runtime` directories if you'd prefer to have separate virtual
environments for your CDK and Chalice app.

To deploy the application, `cd` to the `infrastructure` directory. If
this is your first time using the CDK you'll need to bootstrap your
environment.

    $ cdk bootstrap

Then you can deploy your application using the CDK.

    $ cdk deploy --require-approval never

To delete the stack:

    $ cdk destroy

# Extra commands

## Deploy to different stages/environments

    $ cdk deploy chalice-with-cdk-dev
    $ cdk deploy chalice-with-cdk-staging

## Project layout

This project template combines a CDK application and a Chalice
application. These correspond to the `infrastructure` and `runtime`
directory respectively. To run any CDK CLI commands, ensure you're in
the `infrastructure` directory, and to run any Chalice CLI commands
ensure you're in the `runtime` directory.

  [Deploying with the AWS CDK]: https://aws.github.io/chalice/tutorials/cdk.html
  [Getting started with the AWS CDK]: https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html
