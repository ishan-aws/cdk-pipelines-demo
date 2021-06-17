+++
title = "Create Cognito Authorizer"
description = "Create Cognito Authorizer"
weight = 20
+++

In API Gateway on the left menu click **Authorizers** , then click **+ Create New Authorizer**  input the name as **Builder-Class**, select **Cognito** and select your Cognito user puul in the drop down ( this should pre-populate when you click in the input field ).  

Additionally add **Authorization** as the Token Source, ( note the spelling is Authorization ).  Finally, click **Create**

![](/40-restricting-api-access/20-create-cognito-authorzier/create.en.png)

You new Authoriser is ready, but before we attach this to the API let's explore the test functionality.  Click **Test**

![](/40-restricting-api-access/20-create-cognito-authorzier/ready.en.png)

This will bring up a dialog, this is expecting what we would sent to the API in an Autorization header.  We will send a Bearer token that was generated earlier in Postman.  Leave this dialog open.

![](/40-restricting-api-access/20-create-cognito-authorzier/test-1.en.png)

Return to Postman and return to the original Tab, Click **Auth** then click on the **Avaliable Tokens** combo box, click **Manage Tokens**.

![](/40-restricting-api-access/20-create-cognito-authorzier/token-manage.en.png)

From Here scroll down untill you see Token Type **Bearer** select and copy this token into your clipboard.  If you double click the token it will select it all, do this carefully as the token is long.

![](/40-restricting-api-access/20-create-cognito-authorzier/select-token.en.png)

Return to the AWS Console and in the input box type **Bearer *** with one space and then paste the token and click test.  Your Authorizer works end to end, now lets test this against the actual API. 

![](/40-restricting-api-access/20-create-cognito-authorzier/test-complete.en.png)