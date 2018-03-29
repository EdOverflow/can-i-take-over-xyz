# Can I take over XYZ?

## Created by
[![Twitter](https://img.shields.io/badge/twitter-@jackds1986-blue.svg)](https://twitter.com/jackds1986)
[![Twitter](https://img.shields.io/badge/twitter-@gerben_javado-blue.svg)](https://twitter.com/gerben_javado)
[![Twitter](https://img.shields.io/badge/twitter-@0xibram-blue.svg)](https://twitter.com/0xibram)
[![Twitter](https://img.shields.io/badge/twitter-@EdOverflow-blue.svg)](https://twitter.com/EdOverflow)
[![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_)
[![Twitter](https://img.shields.io/badge/twitter-@now-blue.svg)](https://twitter.com/now)

## What is a sub-domain takeover?
> Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

You can read up more about subdomain takeovers here: https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/.

## Safely Demonstrating  a Subdomain takeover
Claim the subdomain discreetly and serve a harmless file on a hidden page. Do not serve content on the index page. A good proof of concept could consist of an HTML comment served via a random path:

```
$ cat aelfjj1or81uegj9ea8z31zro.html
<!-- PoC by username -->
```

# Summary

|Engine|Possible|Fingerprint|Reference|
|------|--------|-----------|---------|
|[AWS/S3](#aws-s3)|Yes|`The specified bucket does not exist`||
|[Bitbucket](#bitbucket)|Yes|`Repository not found`||
|[Campaign Monitor](#campaign-monitor)|Yes||[Support Page](https://help.campaignmonitor.com/custom-domain-names)|
|[Cargo Collective](#cargo-collective)|Yes|`404 Not Found`|[Cargo Support Page](http://support.2.cargocollective.com/Using-a-Third-Party-Domain)|
|[Cloudfront](#cloudfront)|Yes|`Bad Request: ERROR: The request could not be satisfied`|https://blog.zsec.uk/subdomainhijack/|
|[Desk](#desk)|Yes|`Sorry, We Couldn't Find That Page`||
|[Fastly](#fastly)|Yes|`Fastly error: unknown domain:`||
|[Feedpress](#feedpress)|Yes|`The feed has not been found.`|https://hackerone.com/reports/195350|
|[Freshdesk](#freshdesk)|No||[Freshdesk Support Page](https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname)|
|[Ghost](#ghost)|Yes|`The thing you were looking for is no longer here, or never was`||
|[Github](#github)|Yes|`There isn't a Github Pages site here.`|https://hackerone.com/reports/263902|
|[Gitlab](#gitlab)|No||https://hackerone.com/reports/312118|
|[Google Cloud Storage](#google-cloud-storage)|No|||
|[Help Juice](#help-juice)|Yes|`We could not find what you're looking for.`|[Help Juice Support Page](https://help.helpjuice.com/34339-getting-started/custom-domain)|
|[Help Scout](#help-scout)|Yes|`No settings were found for this company:`|[HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)|
|[Heroku](#heroku)|Yes|`No such app`||
|[JetBrains](#jetbrains)|Yes|`is not a registered InCloud YouTrack`||
|[Mashery](#mashery)|Yes|`Unrecognized domain`|https://hackerone.com/reports/275714|
|[Microsoft Azure](#microsoft-azure)|Yes|||
|[Sendgrid](#sendgrid)|No|||
|[Shopify](#shopify)|Yes|`Sorry, this shop is currently unavailable.`||
|[Squarespace](#squarespace)|No|||
|[Statuspage](#statuspage)|Yes|`You are being redirected`|https://hackerone.com/reports/49663|
|[Surge.sh](#surge.sh)|Yes|`project not found`|https://surge.sh/help/adding-a-custom-domain|
|[Tumblr](#tumblr)|Yes|`Whatever you were looking for doesn't currently exist at this address`||
|[Unbounce](#unbounce)|Yes|`The requested URL was not found on this server.`|https://hackerone.com/reports/202767|
|[UserVoice](#uservoice)|Yes|`This UserVoice subdomain is currently available!`||
|[Wordpress](#wordpress)|Yes|`Do you want to register *.wordpress.com?`||
|[WP Engine](#wp-engine)|No|||
|[Zendesk](#zendesk)|Yes|`Help Center Closed`|[Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)|
# Detail
## Cargo Collective
**Answer:** Yes :heavy_check_mark: 

Look for: `404 Not Found`

Reference: http://support.2.cargocollective.com/Using-a-Third-Party-Domain

## Help Juice
**Answer:** Yes :heavy_check_mark:

Look for: `4o’4! We could not find what you're looking for.`

Reference: https://help.helpjuice.com/34339-getting-started/custom-domain

## GitHub
**Answer:** Yes :heavy_check_mark: 

Look for a 404 page and either an A record pointing to `192.30.252.153` or `192.30.252.154`, or a CNAME record for `username.github.io`. The latter requires owning the GitHub handle so navigate to github.com/username to make sure that the username has not already been registered.

Reference: https://hackerone.com/reports/263902

![](https://user-images.githubusercontent.com/18099289/32145630-3e1b6d6c-bccc-11e7-9ad3-ad4d4a6beb13.png)

## Gitlab
**Answer:** No :negative_squared_cross_mark: 

GitLab require a text record with a verification token in order to set the custom domain. This was fixed as a result of <https://hackerone.com/reports/312118>.

## AWS S3
**Answer:** Yes :heavy_check_mark: 

If a domain has a CNAME record for `*.s3.amazonaws.com` and is returning `NoSuchBucket`, then all you need to do is to create a bucket with that name. You will need an AWS account, however, you can use the [free tier](https://aws.amazon.com/free/) which is more than enough for a PoC. You can then upload a simple txt file at a random path as a proof of concept. 

## Cloudfront
**Answer:** Yes :heavy_check_mark:

When it comes to Cloudfront subdomain takeovers always check both ports 80 and 443. The error message "Bad Request" must be displayed on both ports to ensure that one can claim it on AWS.

If you find a domain that displays this error message, try adding that domain as CNAME to your CloudFront instance on http://aws.amazon.com/ .

Reference: https://blog.zsec.uk/subdomainhijack/

## Statuspage
**Answer:** Yes :heavy_check_mark: 

Reference: https://hackerone.com/reports/49663

## Help Scout
**Answer:** Yes :heavy_check_mark: 

Reference: https://docs.helpscout.net/article/42-setup-custom-domain

## Campaign Monitor
**Answer:** Yes :heavy_check_mark: 

Reference: https://help.campaignmonitor.com/custom-domain-names

## WP Engine
**Answer:** No :negative_squared_cross_mark: 

## Microsoft Azure
**Answer:** Yes :heavy_check_mark:

Azure can host various services: Web Apps (\*.azurewebsites.net), Cloud Services (\*.cloudapp.net), Traffic Manager profiles (\*.trafficmanager.net) or Blob Storages (\*.blob.core.windows.net) to name a few. In general, once a service is removed it's address will become available to others.

_Note: For Web Apps, if the subdomain points to Azure using an A record the takeover might not be possible if the corresponding TXT record is missing (see https://docs.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain.)_

To create a service an account at https://portal.azure.com is needed (a valid CC is required once the trial expires).

## Shopify
**Answer:** Yes :heavy_check_mark: 

## Fastly
**Answer:** Yes :heavy_check_mark:

Subdomains can be taken over if the root domain doesn't already belong to a Fastly account.

## Heroku
**Answer:** Yes :heavy_check_mark: 

Check the CNAME record. If it's pointing at `*.herokuapp.com`, and is returning "No such app", then all you need to do is to create a new app on Heroku with that name.

## Tumblr
**Answer:** Yes :heavy_check_mark: 

Check for an A record pointing to 66.6.44.4 with a subsequent 'Not found.' on the page's title or a 'There's nothing here.' on the page itself.

## Google Cloud Storage
**Answer:** No :negative_squared_cross_mark: 

Google requires domain verification in order to claim domains for Google Cloud Storage.

## Wordpress
**Answer:** Yes :heavy_check_mark: 

Look for the following message:

> "Domain mapping upgrade for this domain not found"

## Feedpress
**Answer:** Yes :heavy_check_mark: 

Look for the following error message and make sure the host has a CNAME pointing to `redirect.feedpress.me`:

> "The feed has not been found"

Reference: https://hackerone.com/reports/195350

## Squarespace
**Answer:** No :negative_squared_cross_mark: 

Squarespace requires domain verification and doesn't allow claiming expired domains.

Reference: https://support.squarespace.com/hc/en-us/articles/205812378-Connecting-a-domain-to-your-Squarespace-site

## UserVoice
**Answer:** Yes :heavy_check_mark:

A vulnerable UserVoice instance will return the error message seen below:

> "This UserVoice subdomain is currently available!"

Reference: <https://hackerone.com/reports/269109>

## Zendesk
**Answer:** Yes :heavy_check_mark:

Look for: `Oops, this help center no longer exists`

Reference: https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-


## Unbounce
**Answer:** Yes :heavy_check_mark:

This one is a little tricky since you need to pay for the service in order to register a custom domain.

Reference: https://hackerone.com/reports/202767

## Surge.sh
**Answer:** Yes :heavy_check_mark:

The host will either have a CNAME record pointing to `na-west1.surge.sh` or an A record for `45.55.110.124`.

Reference: https://surge.sh/help/adding-a-custom-domain

## Freshdesk
**Answer:** No :negative_squared_cross_mark:

Reference: https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname

## Mashery
**Answer:** Yes :heavy_check_mark:

The host should have CNAME record pointing to Mashery.

Reference: https://hackerone.com/reports/275714

## Ghost
**Answer:** Yes :heavy_check_mark:

The host should have CNAME record pointing to `*.ghost.io`, also it costs $20 to host.

## Bitbucket
**Answer:** Yes :heavy_check_mark:

Similar to Github, the CNAME record will be pointing at `*.bitbucket.io`.

## Sendgrid
**Answer:** No :negative_squared_cross_mark:

Sendgrid generates a verification token that mitigates subdomain takeovers. 

Reference: https://sendgrid.com/docs/Classroom/Basics/Whitelabel/setup_domain_whitelabel.html

## Desk
**Answer:** Yes :heavy_check_mark:

CNAME record will be pointing to `*.desk.com`, and will redirect to this page: [http://support.desk.com/system/site_not_found](http://support.desk.com/system/site_not_found)

## JetBrains
**Answer:** Yes :heavy_check_mark:

CNAME record will be pointing to `*.myjetbrains.com`, and will redirect to this page: [https://www.jetbrains.com/youtrack/youtrack-hosted-master/instanceIsNotRegistered/*](https://www.jetbrains.com/youtrack/youtrack-hosted-master/instanceIsNotRegistered/*)
