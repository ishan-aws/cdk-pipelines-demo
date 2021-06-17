+++
title = "Deploy a mock API"
description = "Deploy a mock API"
weight = 10
+++

In the AWS Console, in the unified search type **Api gateway** and click ont eh **API Gateway** Service icon.

![](/40-restricting-api-access/10-deploy-a-mock-api/search.en.png)

If this is your first visit to **API Gateway** you will see the welcome page, click **Get Started**

![](/40-restricting-api-access/10-deploy-a-mock-api/getstarted.en.png)

You will be prompted with a dialong to deploy a prepolulated mock API, click **OK*

![](/40-restricting-api-access/10-deploy-a-mock-api/firstapi.en.png)

You can peruse the Example API response, whehn you are satisfied, leave all settings as defaults and click **Import**

![](/40-restricting-api-access/10-deploy-a-mock-api/import.en.png)

If you have used API Gateway before, click **Create API**

![](/40-restricting-api-access/10-deploy-a-mock-api/gateway.en.png)

Select **REST API** buy clicking **Build**

![](/40-restricting-api-access/10-deploy-a-mock-api/build.en.png)

Then select **Example API** and click import.

![](/40-restricting-api-access/10-deploy-a-mock-api/import.en.png)

The Mock API and endpoints are ready but we still need to deploy.

Click on **Actions**, under the subsection **API ACTIONS** click **Deploy API**.

![](/40-restricting-api-access/10-deploy-a-mock-api/deploy.en.png)

We will now define a stage, click the deployment stage combobox and select **[New Stage]**

![](/40-restricting-api-access/10-deploy-a-mock-api/deploy-2.en.png)

Provide a **Stage name\***, for this example use **Prod**, then click deploy.

![](/40-restricting-api-access/10-deploy-a-mock-api/deploy-3.en.png)

You will see the API endpoint that has been deployed, you can click on this and see the result of a get request in the browser,

![](/40-restricting-api-access/10-deploy-a-mock-api/base.en.png)

Change the URL and append **/pets** to the end and press enter you will see an example JSON response

![](/40-restricting-api-access/10-deploy-a-mock-api/json.en.png)

We now have a mock API the provides static pet data, next we will add authentication restricted by OAuth scope.