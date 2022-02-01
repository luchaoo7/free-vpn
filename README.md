<!--
title: 'Free VPN Setup'
authorLink: 'https://github.com/luchaoo7'
-->

# Your Own Free VPN

This template demonstrates how to create a free VPN running on an AWS EC2 instance using the Serverless Framework and leveraging [OpenVPN](https://openvpn.net/vpn-software-packages/).

### Why do you need your own VPN ?
- Maybe you want to watch content your ISP is blocking.
- Maybe you want to watch content the content provider is blocking in your geographical region e.g. Netflix blocking certain US content for UK customers.
- Maybe you want access to a crypto exchange that blocks people in a certain region. 
- Maybe you don't want to be tracked by ads. 
- Maybe you don't want someone snooping in on your network connection while at Starbucks or Hilton Hotel.
- Maybe you don't want to pay for a VPN that claims not to keep logs (my favorite).
- Maybe you don't want to use one of those free vpns (not this one) that slows down the connection or times you at. 
- Maybe you just want control .
- or Maybe you just want to learn.


## Requirements

- AWS Free Tier
  - Sign up for a 1 year free account [here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).
  - Create an IAM user with Admin privileges.
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

##### Serverless
- Assuming you already signed up [here](https://www.serverless.com/pricing). 
- Register your Access Key ID & Secret Access Key in  Serverless.
  - The most secure way is to create an IAM Access Role but for this guide we will be using our Secret Key and Access ID locally in the next step.

## Deployment

On a terminal download the project from github.
```
$ git clone  git@github.com:luchaoo7/free-vpn.git
```
or at https://github.com/luchaoo7/free-vpn click to download the project to then unzip it. see gif.
.
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/project-download.gif)

```
$ unzip free-vpn-master.zip
```

Once you unzip or clone the project you will see a folder "free-vpn". Change directory into the folder. Every command will be executed from this root folder.
```
$ cd free-vpn 
```
Inside the folder list to see the content.
```
$ ls
```
> <span style="color:blue">images</span> LICENSE README.md <span style="color:blue">resources</span> serverless.yml
├── images\
│   ├── create-key-pair.gif\
│   ├── creating-iam-user.gif\
│   ├── deploying.gif\
│   └── project-download.gif\
├── LICENSE\
├── README.md\
├── resources\
│   ├── ec2.yml\
│   └── securityGroup.yml\
└── serverless.yml\

Assuming you have nodejs installed, install the serverless package globally.

```
$ npm install -g serverless
```

Log into serverless through the terminal. This will open your browser and ask you to log in if you are not already logged in.

```
$ serverless login
```
You should get a similar message in your terminal.
> Logging in the Serverless Dashboard via the browser                                                                                                                                                        
If your browser does not open automatically, please open this URL:                                                                                                                                         
https://app.serverless.com?client=cli&transactionId=kdt5zMTVgA5huEMiCLfb6                                                                                                                                
✔ You are now logged in the Serverless Dashboard 

The next command is to onboard the application. 
```
$ serverless
```
You will be presented with the following options.

> What org do you want to add this service to? ***select the suggested name***
> What application do you want to add this to?
> ✔ Your project has been setup with org "dabrown" and app "free-vpn"
>  No AWS credentials found, what credentials do you want to use?
  ***select the local option***

>  Do you have an AWS account? yes
> ? Press Enter to continue after creating an AWS user with access keys 
  ***Close the browser that opens***

> ? AWS Access Key Id: ***Paste your access key Id***\
>? AWS Secret Access Key: ***Paste your secret access key***\
> ✔ AWS credentials saved on your machine at "~/.aws/credentials". Go there to change them at any time.\
> ? Do you want to deploy your project? Yes\
> ? Do you want to deploy your project? Yes\
> Deploying free-vpn to stage dev (eu-west-2)\
> ✔ Service deployed to stack free-vpn-dev (103s)\

See below
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/deploying.gif)

Once the above is done your VPN will be up and runing in an EC2 instance.
- vpn username: test1
- vpn password: test1

All we need to do now is find the Public IP of where our VPN is running.
We need to go to our AWS account and find the EC2 instance with the name "free-vpn" that was created when we deployed our application.

##### finding our Public IP and download file

![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/ip-login.gif)

The Public IP generated for my vpn was 13.40.28.61. So by going to https://13.40.28.61 I can log in with my username (test1) and password (test1) to download the profile file(s) to log into the vpn. 
One profile allows you to log in without the need of a password and the other requires your password, pick whichever.

><em>note* you can change your test1 user's password and also access the admin page at https://YourEC2IP/admin<em>

##### vpn client download
You can download the vpn client once you login. It's available for Windows, Mac, linux, android and iOS.
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/openvpn-page.png)
 
Once you have downloaded and installed one of the clients, you can import the profile file(s) we downloaded and connect to the VPN.

##### Connection Demo on Ubuntu
see gif
![](https://raw.githubusercontent.com/luchaoo7/free-vpn/master/images/activating-vpn.gif)

And Voilà! you have your VPN Running.

##### Useful info
When you deployed, you deployed 4 free resources:
- An EC2 Instance.
- A security Group.
- An S3 Bucket.
- And a S3 Bucket Policy.

All these resources can be torn down with a simple command from within the "free-vpn" folder.
```
$ serverless remove
```
and re-deploy with:
```
$ serverless deploy
```
### Conclusion

I created this small setup because I was tired of having to manually setup my EC2 instance for VPN purposes and sometimes forgetting commands and sometimes forgetting what resources I had running. With this setup I know when I do ***serverless remove*** I'm not leaving anything running and of course, it's free :).

### Future update

At the moment the VPN deploys to eu-west-2 (London), with a specic image ID for that region.
I will be adding an update to pass what region you want to deploy your VPN to and automatically tear down whatever may be running (don't quote me on adding more updates lol, feel free to fork or make a pull request if you feel like contributing).
>*note: you only get 750 hours of free EC2 usage a month on AWS while using the Free Tier, which amounts to 31.25 days a month, so running more than one EC2 instance will incur charges.