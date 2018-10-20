# Azure For Students Workshop
Demonstration of Microsoft Azure ML/AI capabilities - Azure Notebooks, Cognitive Services, Azure ML

*The content and code on this repo is intended for Microsoft ML/AI workshop under the [MIT license](LICENSE). Please check back regularly for updated versions.*

This repo provides technical resources to help students and faculty learn about Azure and teach others. The content covers cross-platform scenarios in AI and machine learning, data science, web development, mobile app dev, internet of things, and devops.

Students can get free Azure credits to explore these resources here:

* [Azure For Students ($100 in Azure - no credit card required)](https://azure.microsoft.com/en-us/free/students/?WT.mc_id=workshop-github-vakarpus)
* [Azure For Students Starter (use free Azure products with no credit card)](https://azure.microsoft.com/en-us/free/students-starter-faq/?WT.mc_id=workshop-github-vakarpus)
* [Azure Free Account](https://azure.microsoft.com/en-us/free/?WT.mc_id=workshop-github-vakarpus)

Your feedback is appreciated - please fork this repo and contribute!

To report any issues, please [log a GitHub issue](https://github.com/vakarpus/workshop-notebooks/issues). Include the content section, module number and title, along with any error messages and screenshots.

## Instructions
### Free Azure Student Account and Computer Vision Cognitive Service
1. Create free account using links above
2. Visit [Microsoft Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=workshop-github-vakarpus) webpage to learn about Cognitive Services functionality.
3. Try different demos on [Computer Vision](https://azure.microsoft.com/services/cognitive-services/directory/vision/?WT.mc_id=workshop-github-vakarpus) page of Cognitive Services.
4. Press "Try for free" under Computer Vision section and choose "Guest" - 7-day trial or "Exis*i*ting Azure account" and log in into your free Student account created previously.
    * If you selected "Guest" - 7-day trial: Sign-in using Microsoft, Facebook, LinkedIn, or Github account to proceed.
    * If you used Student Azure account: 
        * Search for "Computer Vision" using search bar at the top of the page, 
        * select "Marketplace: Computer Vision" and proceed to creating Computer Vision service instance
        * Specify unique name for the service (e.g. "CompVision1234")
        * Use "Azure for Students" Subscription
        * Location - "West Central US"
        * Pricing tier - use free F0 (20 Calls per minuter, 5k Calls per month) or if you plan to use the service more agressively - switch to S1 Standard tier (10 Calls per second, $1.00 per 1k Calls - remember you have a budget of $100 on your free Student Azure account)
        * Create a new Resource group
        * Press "Create"
        * Wait for notification "Deployment succeeded" to show up or check Bell icon at the top of the Azure Portal page
        * Click "Go to resource" button
5. Leave this page open for the reference. We will need API call endpoint (e.g. https://westcentralus.api.cognitive.microsoft.com/) and 32-symbol key. You will need only Key 1.

### Running code on Azure Notebooks
6. Click the following link to open [Azure Notebooks](https://notebooks.azure.com/Vadi/libraries/Workshop/?WT.mc_id=workshop-github-vakarpus) and log in usign Free Student Azure account you've created earlier. Click on [Azure Notebooks](https://notebooks.azure.com/Vadi/libraries/Workshop/?WT.mc_id=workshop-github-vakarpus) again if you were navigated away from the workshop files. 
7. Click "Clone" on top of the files to copy them into your own Notebook library.
8. To run Python code in the Azure Jupyter Notebook click on "handwriting.ipynb" file at the top of the page.
9. Change *subscription_key* and *uri_base* to use from instruction 5 in the first code cell
10. To execute the code select cells one by one and run them by pressing *CTRL+Enter*. Or run all cells in order by going into the menu *Kernel / Restart Kernel and Run All Cells...*
11. Wait for code to execute
12. If the result of running last code cell shows *"status": "Running"* - rerun the last code cell by clicking on it (selecting it) and pressing *CTRL+Enter*. This will resubmit GET request to Computer Vision REST API service and you will see the result of handwriten text recognition.

### Extra credit
13. Modify the code above to upload local file "vadim.png" to the Computer Vision Cognitive Services instead of just providing URL of the image.
14. Clone git repository to your local machine using "git clone git@github.com:vakarpus/workshop-notebooks.git" and try running local python script handwriting.py (modify subscription key in *key.py* beforehand).
15. Experiment with other Microsoft Cognitive Services.
 
## Azure Cloud Overview
The Azure cloud is huge (so that’s why they call it the cloud!) and the vast service catalog may appear daunting at first. It doesn’t have to be!

- Learn the browser-based UI of the [Azure Portal](https://azure.microsoft.com/features/azure-portal/?WT.mc_id=workshop-github-vakarpus)
- Continue the journey with the built-in, ready-to-run [Azure Cloud Shell](https://azure.microsoft.com/features/cloud-shell/?WT.mc_id=workshop-github-vakarpus)
- Explore various ways to deploy web apps written in any language, on any platform, from [virtual machines](https://azure.microsoft.com/services/virtual-machines/?WT.mc_id=workshop-github-vakarpus) and [containers](https://azure.microsoft.com/free/kubernetes-service/search/?WT.mc_id=workshop-github-vakarpus) to [serverless technologies](https://azure.microsoft.com/services/functions/?WT.mc_id=workshop-github-vakarpus)
- Add intelligence to your apps using [Microsoft Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=workshop-github-vakarpus)
- Protect your apps by applying Azure’s built-in [security features](https://azure.microsoft.com/services/security-center/?WT.mc_id=workshop-github-vakarpus)
- Diagnose problems and apply automated machine learning analysis with [Application Insights](https://docs.microsoft.com/azure/application-insights/app-insights-overview/?WT.mc_id=workshop-github-vakarpus) 
- Connect your apps with messaging services, load files into [cloud storage](https://azure.microsoft.com/free/storage/?WT.mc_id=workshop-github-vakarpus) and discover managed databases for [SQL](https://azure.microsoft.com/free/sql-database/search/?WT.mc_id=workshop-github-vakarpus) and [NoSQL](https://azure.microsoft.com/free/cosmos-db/search/?WT.mc_id=workshop-github-vakarpus) scenarios
- Tie everything together in a continuous delivery pipeline with [Azure DevOps](https://azure.microsoft.com/services/devops/?WT.mc_id=workshop-github-vakarpus) projects
