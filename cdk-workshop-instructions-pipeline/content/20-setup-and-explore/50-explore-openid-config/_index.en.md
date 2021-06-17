+++
title = "Explore OpenId Config"
weight = 50
+++

Lets explore the published configureation and it's format.  This confuguration follows a convention

https://cognito-idp.{region}.amazonaws.com/{userpoolid}/.well-known/openid-configuration

On the console, on the left menu click on **general settings**, here you will find the user pool id:

![](/20-setup-and-explore/50-explore-openid-config/poolid.en.png)

Copy this to construct your openid config URL and open this in your broswer.  This is public information and is safley exposed.  <--- word this better

![](/20-setup-and-explore/50-explore-openid-config/example-config.en.png)

