<!--
title: 'AWS NodeJS Example'
description: 'This template demonstrates how to deploy a NodeJS function running on AWS Lambda using the traditional Serverless Framework.'
layout: Doc
framework: v2
platform: AWS
language: nodeJS
priority: 1
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->


# Free VPN

This template demonstrates how to create a free VPN running on an AWS EC2 instance using the Serverless Framework.

## Requirements

- AWS Free Tier
  - Sign up for a 1 year free account [here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
  - Create an IAM user with Admin privileges.
  - Create a key pair and name it "openVPNec2" (if you want access to the ec2 instance at some point).
- Serverless Free Tier 
  - Sign up and use the free plan [here](https://www.serverless.com/pricing)
  - Register your Access Key ID & Secret Access Key from AWS with Serverless.

###### Tools
- nodejs [here](https://nodejs.org/en/)
- Any of: Unix, Linux, WSL (Windows Subsystem for Linux).
- Git (project can be downloaded without git).

## Setup steps

##### AWS
- Assuming you already signed up  [here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
- Creating an IAM user with admin rights in AWS. Follow the below gif.
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/creating-iam-user.gif)
  - Remember to download the .csv file. It will contain your Secret Access Key and Access Key ID, which you will need later. You can also copy and paste it to notepad as soon as you sucessfully create your user. You will not be able to see your Secret Access Key again unless you download it. 
.
- Creating key-pair. Follow the gif.
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/create-key-pair.gif)

##### Serverless
- Assuming you already signed up [here](https://www.serverless.com/pricing). 
- Register your Access Key ID & Secret Access Key in  Serverless.
  - The most secure way it to create an IAM Access Role but for this guide we will be using our Secret Key and Access ID in the next step.

## Usage

On a terminal download the project from github.
```
git clone  git@github.com:luchaoo7/free-vpn.git
```
or at https://github.com/luchaoo7/free-vpn click to download the project. see gif.
.
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/project-download.gif)

Once you unzip or clone the project you will see a the folder "free-vpn". Change directory into the folder. Every command will be executed from this root folder.
```
cd free-vpn 
```
Inside the folder list to see the content.
```
ls
```
>
├── images
│   ├── create-key-pair.gif
│   ├── creating-iam-user.gif
│   └── project-download.gif
├── LICENSE
├── README.md
├── resources
│   ├── ec2.yml
│   └── securityGroup.yml
└── serverless.yml

Assuming you have nodejs installed, install the serverless package globally.

```
npm install -g serverless
```

Log into serverless through the terminal. This will open your browser and ask you to log in if you are not already logged in.

```
serverless login
```
You should get a similar message in your terminal.
> Logging in the Serverless Dashboard via the browser                                                                                                                                                        
If your browser does not open automatically, please open this URL:                                                                                                                                         
https://app.serverless.com?client=cli&transactionId=kdt5zMTVgA5huEMiCLfb6                                                                                                                                
✔ You are now logged in the Serverless Dashboard 

The next command is to onboard the application. 
```
serverless
```


### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-node.zip file to S3 (711.23 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.................................
Serverless: Stack update finished...
Service Information
service: aws-node
stage: dev
region: eu-west-2
stack: aws-node-dev
resources: 4
```

An EC2 instance will have been deployed with a public address

### Future update

At the moment the VPN is deployt in eu-west-2, with a specic image ID for that region.
The below link shows how to make the region and imageID selection more dynamic
[aws-cloudformation-templates](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/solutions/OperatingSystems/ubuntu20.04LTS_cfn-hup.cfn.yaml)