+++
title = "Explore Hosted UI"
weight = 60
+++

Lets explore the hosted UI and options.

Return to the AWS Console, On the left menu under **App intergration** click on **App client settings** from here click on **Launch Hosted UI** this will open a window/tab with javascript, you cannot right click and copy the URL so ensure you click.

![](/20-setup-and-explore/60-explore-hosted-ui/hostedui-launch.en.png)

In the New tab click **Sign up** we will be registering a new user.

![](/20-setup-and-explore/60-explore-hosted-ui/sighn-up.en.png)

Fill out the registration form and ensure you use a real email adddress as a OPT ( One Time Password ) will be sent to this address to enable account confirmation.  Click **Sign up**

![](/20-setup-and-explore/60-explore-hosted-ui/register.en.png)

Check you email inbox for the OTP and enter the value and click **Confirm Account**.  The email you recieve is minimal and not styles this can all be customised if required.

![](/20-setup-and-explore/60-explore-hosted-ui/confirm.en.png)

Once you account is confirmed you will be redirect bach to your applicaiton, as we configued that url for this excersize to localhost and we are not hosting an applicaiton your browser will display the following.

Take note of the URL it will be:  https://localhost/?code=c4248548-8691-4547-9e66-06d4b64d64ee though will a differnt code. 

![](/20-setup-and-explore/60-explore-hosted-ui/safari.en.png)

Let's now look at the resposne when we chnage to implicit flow sign in.  Close the current tab, you'll be back at the **App client Settings** section of Cognito, again click on **Launch Hosted UI** this will open a new tab, however you are logged in from the prior session, click **Sign in as a different user?** 

![](/20-setup-and-explore/60-explore-hosted-ui/differnt-user.en.png)

Click in the URL section of your browser, the URL will look something like this:

https://example-demo.auth.ap-southeast-2.amazoncognito.com/login?client_id={yourclientId}&response_type=code&scope=email+openid+petstore/read+profile&redirect_uri=https://localhost

Change the response type value to **token** from **code**

https://example-demo.auth.ap-southeast-2.amazoncognito.com/login?client_id={yourclientId}&response_type=token&scope=email+openid+petstore/read+profile&redirect_uri=https://localhost

And press enter to load the new URL, enter the user details you created previosly and click **Sign in**

“https://localhost/#id_token={a-large-id-token}&access_token={a-large-access-token}&expires_in=3600&token_type=Bearer” because Safari can’t connect to the server “localhost”.

![](/images/hostedui/safari.en.png)