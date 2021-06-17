+++
title = "Attach Authorizer to the API"
description = "Attach Authorizer to the API"
weight = 30
+++

We now have all the parts to add authentication to the API.  In this section we will restrict access to the /pets end point.

To confirm this is all working as expeced return to Postman and open a new tab, take the API URL ( you shoudl still have this in a broser tab, if not navigate back to API Gateway, click **Stages** in the left menu and copy the URl from the highlighted blud section at the top next to Invoke URL  ) and paste this in, click send to see the result.

![](/40-restricting-api-access/30-attach-authorizer-to-the-api/new-tab.en.png)

Return to the AWS Console, Navigate to API Gteway and select you API.  In the left hand menu click **Resources**, in the Resources colum, clic/expant **/pets** then click on **GET** we will add authentication to only this resource which is the http GET verb on the sample api resource.  

![](/40-restricting-api-access/30-attach-authorizer-to-the-api/request.en.png)

Click on the **Aurthorization** combo box
![](/40-restricting-api-access/30-attach-authorizer-to-the-api/combo-1.en.png)

select **Builder-class* 
![](/40-restricting-api-access/30-attach-authorizer-to-the-api/combo-2.en.png)

then click the little tick to save.
![](/40-restricting-api-access/30-attach-authorizer-to-the-api/combo-3.en.png)

This will dplay a new option **OAuth Scopes**, click the little pencole next the the default value which is NONE and type in **petstore/read** this is the OAuth scope we defined in Cognito earlier.  Click the small tick to save.

![](/40-restricting-api-access/30-attach-authorizer-to-the-api/tick.en.png)

You screen should look like below:

![](/40-restricting-api-access/30-attach-authorizer-to-the-api/should.en.png)

The settings are now ready but we have to deploy our API changes, click on **Actions** then **Deploy API**
![](/40-restricting-api-access/30-attach-authorizer-to-the-api/actions-1.en.png)
 for the deployment stage select **Prod** and click deploy
![](/40-restricting-api-access/30-attach-authorizer-to-the-api/actions-2.en.png)

