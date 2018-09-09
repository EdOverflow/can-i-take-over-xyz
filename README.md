# Can I take over XYZ?

## Created by

[![Twitter](https://img.shields.io/badge/twitter-@jackds1986-blue.svg)](https://twitter.com/jackds1986) [![Twitter](https://img.shields.io/badge/twitter-@gerben_javado-blue.svg)](https://twitter.com/gerben_javado) [![Twitter](https://img.shields.io/badge/twitter-@0xibram-blue.svg)](https://twitter.com/0xibram) [![Twitter](https://img.shields.io/badge/twitter-@EdOverflow-blue.svg)](https://twitter.com/EdOverflow) [![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_) [![Twitter](https://img.shields.io/badge/twitter-@now-blue.svg)](https://twitter.com/now)

## What is a sub-domain takeover?

> Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

You can read up more about subdomain takeovers here:

- <https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/>
- <https://www.hackerone.com/blog/Guide-Subdomain-Takeovers>
- <https://0xpatrik.com/subdomain-takeover-ns/>

## Safely Demonstrating a Subdomain takeover

Claim the subdomain discreetly and serve a harmless file on a hidden page. Do not serve content on the index page. A good proof of concept could consist of an HTML comment served via a random path:

```
$ cat aelfjj1or81uegj9ea8z31zro.html
<!-- PoC by username -->
```

# Summary

Engine                                        | Status         | Fingerprint                                                             | Discussion                                                    | Documentation
--------------------------------------------- | -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------
[AWS/S3](#aws-s3)                             | Vulnerable     | `The specified bucket does not exist`                                   |
[Bitbucket](#bitbucket)                       | Vulnerable     | `Repository not found`                                                  |
[Campaign Monitor](#campaign-monitor)         | Vulnerable     |                                                                         |                                                               | [Support Page](https://help.campaignmonitor.com/custom-domain-names)
[Cargo Collective](#cargo-collective)         | Vulnerable     | `404 Not Found`                                                         |                                                               | [Cargo Support Page](https://support.2.cargocollective.com/Using-a-Third-Party-Domain)
[Cloudfront](#cloudfront)                     | Edge case      | `Bad Request: ERROR: The request could not be satisfied`                | <https://github.com/EdOverflow/can-i-take-over-xyz/issues/29>
[Desk](#desk)                                 | Vulnerable     | `Please try again or try Desk.com free for 14 days.`                    | <https://github.com/EdOverflow/can-i-take-over-xyz/issues/9>
[Fastly](#fastly)                             | Vulnerable     | `Fastly error: unknown domain:`                                         |
[Feedpress](#feedpress)                       | Vulnerable     | `The feed has not been found.`                                          | <https://hackerone.com/reports/195350>
[Freshdesk](#freshdesk)                       | Not vulnerable |                                                                         |                                                               | [Freshdesk Support Page](https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname)
[Ghost](#ghost)                               | Vulnerable     | `The thing you were looking for is no longer here, or never was`        |
[Github](#github)                             | Vulnerable     | `There isn't a Github Pages site here.`                                 | <https://hackerone.com/reports/263902>
[Gitlab](#gitlab)                             | Not vulnerable |                                                                         | <https://hackerone.com/reports/312118>
[Google Cloud Storage](#google-cloud-storage) | Not vulnerable |                                                                         |
[Help Juice](#help-juice)                     | Vulnerable     | `We could not find what you're looking for.`                            |                                                               | [Help Juice Support Page](https://help.helpjuice.com/34339-getting-started/custom-domain)
[Help Scout](#help-scout)                     | Vulnerable     | `No settings were found for this company:`                              |                                                               | [HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)
[Heroku](#heroku)                             | Vulnerable     | `No such app`                                                           |
[JetBrains](#jetbrains)                       | Vulnerable     | `is not a registered InCloud YouTrack`                                  |
[Mashery](#mashery)                           | Not vulnerable | `Unrecognized domain`                                                   | <https://hackerone.com/reports/275714>
[Microsoft Azure](#microsoft-azure)           | Vulnerable     |                                                                         |
[Sendgrid](#sendgrid)                         | Not vulnerable |                                                                         |
[Shopify](#shopify)                           | Vulnerable     | `Sorry, this shop is currently unavailable.`                            |
[Squarespace](#squarespace)                   | Not vulnerable |                                                                         |
[Statuspage](#statuspage)                     | Vulnerable     | `You are being redirected`                                              | <https://hackerone.com/reports/49663>
[Surge.sh](#surge.sh)                         | Vulnerable     | `project not found`                                                     |                                                               | <https://surge.sh/help/adding-a-custom-domain>
[Tumblr](#tumblr)                             | Vulnerable     | `Whatever you were looking for doesn't currently exist at this address` |
[Tilda](#tilda)                               | Not vulnerable | `Please renew your subscription`                                        |
[Unbounce](#unbounce)                         | Not vulnerable | `The requested URL was not found on this server.`                       | <https://github.com/EdOverflow/can-i-take-over-xyz/issues/11>
[UserVoice](#uservoice)                       | Vulnerable     | `This UserVoice subdomain is currently available!`                      |
[Wordpress](#wordpress)                       | Vulnerable     | `Do you want to register *.wordpress.com?`                              |
[WP Engine](#wp-engine)                       | Not vulnerable |                                                                         |
[Zendesk](#zendesk)                           | Vulnerable     | `Help Center Closed`                                                    | <https://github.com/EdOverflow/can-i-take-over-xyz/issues/23> | [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)
