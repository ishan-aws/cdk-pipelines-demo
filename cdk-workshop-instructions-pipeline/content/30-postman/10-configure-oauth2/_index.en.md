+++
title = "Configure OAuth 2.0"
description = "Use metadata to catalogue and describe your workshop"
weight = 10
+++

Once we have a new tab, click on the **Authorisation** item, then chanhe the type to **OAuth 2.0**

![](/30-postman/10-configure-oauth2/auth-tab.en.png)

Fill out the settings as per below

![](/30-postman/10-configure-oauth2/settings.en.png)

Then click **Get New Access Token**

![](/30-postman/10-configure-oauth2/get-new-token.en.png)

This will pop up a mini browser requesting your credentials, use the credentials you created earlier to login and click Sign in.

![](/30-postman/10-configure-oauth2/sign-in.en.png)

The mini browser will close and if you have followed all the steps correctly you will see this message:

![](/30-postman/10-configure-oauth2/auth-success.en.png)

Click **Proceed** to view the tokens returned by Cognito.  The token returned can be decoded at https://jwt.io for closer inspection this token is used to sent to our service to authenticate and and provide course level access as defined by the scope.  An example can be seen below.

![](/30-postman/10-configure-oauth2/decode.en.png)

You can click **Get New Access Token** several times for new/additional tokens, try this.  Then Click **Clear cookies** and try again and notice you will have to log back in.

Lastly, if you encounter issues of just want to look at the http calls and redirects at the bottom of postman click **Console** to see the detail.

![](/30-postman/10-configure-oauth2/consol.en.png)