# Deployment_Helper_Program
This repository contains the source code and the runnable exe file for the Deployment Helper program

                 YOU CAN RUN THE PROGRAM WITH THE deployment_helper.exe in ---> dist folder
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                 THE PROGRAM ONLY WORKS IF YOU HAVE YOUR BROWSERS INSTALLED IN THESE LOCATIONS:



                  MOZILLA FIREFOX   ----> C://Program Files//Mozilla Firefox//firefox.exe")

                  GOOGLE CHROME     ----> C:\Program Files\Google\Chrome\Application\chrome.exe

                  EDGE              ----> C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe

                  INTERNET EXPLORER ----> NOT SUPPORTED


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
WORKFLOW:
1. Open the program
2. Choose the website for which the deployment is ongoing
3. Enter the URL you are testing for in the input field
4. Click on the browser button you want to open the URL-s in.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    IF YOU WANT TO MAKE SOME CHANGES IN THE CODE AND THEN BUILD THE EXE AGAIN THESE ARE THE REQUIRED STEPS:

1. Delete the build folder
2. Delete the .exe from the dist folder
3. Delete the deployment_helper.spec
4. git bash into the folder of the repository (where the deployment_helper.py is located)
5. enter this command: $ pyinstaller --onefile -w deployment_helper.py
6. You can use the new .exe from the dist folder

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
URL-s OPENED:

FOR PPG:

        "/borrow/mortgages/",    
        "/plan/pensions/",
        "/premier/",
        "/privatebanking/welcome-to-private/",
        "/borrow/mortgages/calculators/mortgage-calculator/",
        "/bank/international-payments/foreign-exchange-currency-converter/",
        "/investments-calculator-form/",
        "/investments-goal-saver-calculator/",
        "/investments-regular-saver-calculator/",
        "/children-education-calculator/?accommodationType=rent&childrenAges=6,,,,,,,,,#gf_442",
        "/bank/international-payments/daily-foreign-exchange-rates/?latest=version"
        
        
BB:

        "/business-supports/sectors/",   
        "/credit/business-loans/business-loan/features-benefits-2/",
        "/financial-wellbeing/",
        "/support-centre/business-banking/"
        
        
WWW:

        "/branch-locator/",
        "/help-centre/",
        "/kiosk-application-centre/" (ONLY WORKS WHEN YOU ARE ON VPN)
        
     
BOIUK:

        "/personal/",
        "/business/",
        "/mortgages/existing-customer/",
        "/daily-foreign-exchange-rates/",
        "/mortgages/existing-customer/calculators/",
        "/mortgages/existing-customer/calculators/convert-to-repayment/",
        "/mortgages/existing-customer/calculators/rate-change/",
        "/mortgages/existing-customer/calculators/change-term/",
        "/mortgages/existing-customer/calculators/borrowing-more/",
        "/mortgages/existing-customer/calculators/loan-to-value/",
        "/mortgages/existing-customer/calculators/overpayment/",
        "/personal/financial-wellbeing/",
        "/personal/what-is-youth-financial-wellbeing/",
        "/help-and-support/"
        
     
