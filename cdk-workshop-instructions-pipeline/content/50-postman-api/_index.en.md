+++
title = "Postman API"
chapter = true
weight = 50
pre = "<b>5. </b>"
+++

To confirm this is all working as expeced return to Postman, the same tab from ealerier will be open, click **Send** to call the api again.  This time the resonse will be:

```
{
    "message": "Unauthorized"
}
```

![](/50-postman-api/unauthorized.en.png)

This is expected, the API now require authorization!

The API is expecting a new http header, the header required is:

```
Key:  Authorization
Value:  Bearer token
```

You can manually add this by extracting the token as in earler steps when we tested the Authroizer in the API Gateway console or you can click on the **Authorization** tab, for type select **OAuth 2.0**  This shoudl re-populate the settings we enetered.  Avaliable tokens will be empty, scoll down and click **Get New Token**, put in the username and password of the user created.  Click **Proceed**, this time once the **Manage Access Tokens** diaplog appears click **Use Token**.

![](/50-postman-api/usertoken.en.png)

Click on the **Headers** tab and notice the additional header key and value.

![](/50-postman-api/checkheader.en.png)

Click **Send** and the API will again return data!

![](/50-postman-api/data.en.png)

Well done the end





{
    "message": "The incoming token has expired"
}