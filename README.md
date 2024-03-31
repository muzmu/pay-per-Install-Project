Understanding the Ecosystem and Security Implications of Pay-Per-Install services on Android

Introduction
The pay-per-install distribution model on the web is based on revenue sharing and commission. Malware authors do not have the resources or bandwidth to spread their malware on a large scale. Instead, they rely on a network of affiliates, who distribute the malware, and in return get paid a commission for every install.
Pay-per-install services are also prevalent on the Android platform now. However, they are being used by both malicious parties and by normal developers to get installs for their apps. Malicious parties can spread malware or apps with dangerous permissions using these pay-per-install services whereas shady developers can use them to get a fake boost in ratings for their applications.

Investigating Reward-Based Applications
We found that there were some applications on the Android Play store that were earning money through these pay-per-install services. These reward-based applications integrate offerwalls of these pay-per-install networks in them and offer their users to install these apps for a cash prize which is a fraction of what the pay-per-install network pays them. We are leveraging these applications right now to understand the pay-per-install scenario in the android platform.

Methodology
We have selected seven reward-based applications that are the most popular on google play store and have the most offerwalls integrated into them. We have identified the API calls that these apps are making to retrieve offers for their offerwalls through using them by while the phone was attached to our man-in-the-middle proxy. After that, we automated the interactions with these applications through ADB and appium while the phone was connected to the internet via our proxy and wrote a custom script for a proxy that will catch and save the responses of our interest containing the offers. Now the measurement process is running where these seven apps are navigated by our program each hour and a proxy at Iowa records and saves all JSON responses containing offers. The proxy at Iowa further connects to different proxies in Russia, USA and United Kingdom so that we can get offers from different countries too. We then extract the android application package names through parsing through these responses.

Strategy for Collecting Data of Multiple Countries
In order to extend data collection, we bought a premium subscription of proxies from LUMINATI and directed requests going through our MITM proxy from a second proxy bought from LUMINATI. So, we kept changing this second proxy every two hours to another country and so collected data from a number of different countries.

Android Applications under review
1. https://play.google.com/store/apps/details?id=com.ayet.cashpirate
2. https://play.google.com/store/apps/details?id=proxima.makemoney.android
3. https://play.google.com/store/apps/details?id=com.growrich.makemoney
4. https://play.google.com/store/apps/details?id=eu.makemoney
5. https://play.google.com/store/apps/details?id=com.wMakeMoney 6155214
6. https://play.google.com/store/apps/details?id=proxima.moneyapp.android

Offerwalls under review
1. adgate
2. adscendmedia
3. awesome offerwall
4. ayetstudios
5. fyber
6. rankapp
7. Trialpay
8. ironsource

Google Play Crawlers Setup
We also deployed google play store crawlers to regularly collect data from google play store of the application packages we were receiving from our PPI crawl to see how much were their fake rankings and installs being boosted by the PPI services. A problem with these crawlers was that google actively started blocking them so first we wrote our own crawlers to collect free proxies from the internet and later we bought some paid proxies too. Our strategy was to keep using a proxy until it gets blocked and shift the proxy once google blocks it. We deployed four types of crawlers. They were:
1. Snapshot PPI Crawler
2. Daily PPI Crawler
3. Baseline Snapshot Crawler
4. Baseline Daily Crawlers
They collected the following information about the package-names being propagated by PII services regularly.
1. App Metadata
2. App Reviews
3. App Permissions
4. Keywords that can bring up the app if searched.
5. Top rated apps for different countries and categories.

Progress till now:
Currently, we have been able to successfully identify about 2077 Android Applications that potentially use PPI services. Furthermore, we also collect permission and metadata after every two days of around 1767 Android Applications. Moreover, we have also identified and collecting meta and permission data of about 750 Daily Base Applications which will be used to compare with Android Applications using PPI services. We have also been able to identify about 5000 Android Applications of other developers who have PPI applications. We have also been able to identify and collect data of around 9500 keywords which are used to check rankings of the Android applications on Google Play store and how these are affected when they are using PPI services. To compare and see the presence of PPI Android Applications, as well as other applications, we are crawling rankings of about 3000 different categories from Google play store every two days. We have enough evidence to suggest that there are a large number of Android applications that use PPI services to boost their rankings and are working to do further analysis of to what extent these PPI services help to boost their rankings, as well as increase their installs. For how many days and times, these applications remain on the top categories by using PPI services? We plan to submit a paper to the Internet measurement conference based on our results.

