+++
title = "App client settings"
weight = 40
+++

We will now configure the call back URLs, OAuth flows and OAuth scopes.

On the left hand menu under **App intergration** click on **App client settings**

![](/20-setup-and-explore/40-appclient-settings/appclientsettings-menu.en.png)

There are a number of options to enable, ensure yours look the same as the image.

First we enable "Cognito User Pool"

We then input the Callback and Sign out URL(s).  These URL(s) are used to direct the Hosted Cognito UI back to your app after the Authentication process, for this exersize we will use **https://localhost**

Under **Allowed OAuth Flows** select 
- **Authorization code grant** and 
- **Implicit grant**

Under **Allowed OAuth Scopes** select
- **email**
- **openid** and
- **profile**

Under **Allowed Custom Scopes** select
- **petstore/read**

Finally click **Save changes**

![](/20-setup-and-explore/40-appclient-settings/appclient-options.en.png)