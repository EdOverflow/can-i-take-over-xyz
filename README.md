![image](https://user-images.githubusercontent.com/18099289/45263787-a4bbc880-b430-11e8-9cff-eb6e4c796050.png)

## Created by

[![Twitter](https://img.shields.io/badge/twitter-@jackds1986-blue.svg)](https://twitter.com/jackds1986) [![Twitter](https://img.shields.io/badge/twitter-@gerben_javado-blue.svg)](https://twitter.com/gerben_javado) [![Twitter](https://img.shields.io/badge/twitter-@0xibram-blue.svg)](https://twitter.com/0xibram) [![Twitter](https://img.shields.io/badge/twitter-@EdOverflow-blue.svg)](https://twitter.com/EdOverflow) [![Twitter](https://img.shields.io/badge/twitter-@codingo__-blue.svg)](https://twitter.com/codingo_) [![Twitter](https://img.shields.io/badge/twitter-@now-blue.svg)](https://twitter.com/now)

## What is a sub-domain takeover?

> Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

You can read up more about subdomain takeovers here:

- <https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/>
- <https://www.hackerone.com/blog/Guide-Subdomain-Takeovers>
- <https://0xpatrik.com/subdomain-takeover-ns/>

## Safely demonstrating a subdomain takeover

Claim the subdomain discreetly and serve a harmless file on a hidden page. Do not serve content on the index page. A good proof of concept could consist of an HTML comment served via a random path:

```
$ cat aelfjj1or81uegj9ea8z31zro.html
<!-- PoC by username -->
```

## How to contribute

You can submit new services here: https://github.com/EdOverflow/can-i-take-over-xyz/issues/new?template=new-entry.md.

# All entries

Engine                                        | Status         | Fingerprint                                                             | Discussion                                                    | Documentation
--------------------------------------------- | -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------
Akamai                                        | Not vulnerable | | [Issue #13](https://github.com/EdOverflow/can-i-take-over-xyz/issues/13) |
AWS/S3                             | Vulnerable     | `The specified bucket does not exist`                                   | [Issue #36](https://github.com/EdOverflow/can-i-take-over-xyz/issues/36)
Bitbucket                       | Vulnerable     | `Repository not found`                                                  |
Campaign Monitor         | Vulnerable     |                                                                         |                                                               | [Support Page](https://help.campaignmonitor.com/custom-domain-names)
Cargo Collective         | Vulnerable     | `404 Not Found`                                                         |                                                               | [Cargo Support Page](https://support.2.cargocollective.com/Using-a-Third-Party-Domain)
Cloudfront                     | Edge case      | `Bad Request: ERROR: The request could not be satisfied`                | [Issue #29](https://github.com/EdOverflow/can-i-take-over-xyz/issues/29)
Desk                                 | Not vulnerable     | `Please try again or try Desk.com free for 14 days.`                    | [Issue #9](https://github.com/EdOverflow/can-i-take-over-xyz/issues/9)
Fastly                             | Edge case     | `Fastly error: unknown domain:`                                         | [Issue #22](https://github.com/EdOverflow/can-i-take-over-xyz/issues/22)
Feedpress                       | Vulnerable     | `The feed has not been found.`                                          | [HackerOne #195350](https://hackerone.com/reports/195350)
Freshdesk                       | Not vulnerable |                                                                         || [Freshdesk Support Page](https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname)
Ghost                               | Vulnerable     | `The thing you were looking for is no longer here, or never was`        |
Github                             | Vulnerable     | `There isn't a Github Pages site here.`                                 | [Issue #37](https://github.com/EdOverflow/can-i-take-over-xyz/issues/37)
Gitlab                             | Not vulnerable |                                                                         | [HackerOne #312118](https://hackerone.com/reports/312118)
Google Cloud Storage | Not vulnerable |                                                                         |
Help Juice                     | Vulnerable     | `We could not find what you're looking for.`                            |                                                               | [Help Juice Support Page](https://help.helpjuice.com/34339-getting-started/custom-domain)
Help Scout                     | Vulnerable     | `No settings were found for this company:`                              |                                                               | [HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)
Heroku                             | Vulnerable     | `No such app`                                                           | [Issue #38](https://github.com/EdOverflow/can-i-take-over-xyz/issues/38)
JetBrains                       | Vulnerable     | `is not a registered InCloud YouTrack`                                  |
Mashery                           | Not vulnerable | `Unrecognized domain`                                                   | [HackerOne #275714](https://hackerone.com/reports/275714)
Microsoft Azure           | Vulnerable     |  | [Issue #35](https://github.com/EdOverflow/can-i-take-over-xyz/issues/35) |
Sendgrid                         | Not vulnerable |                                                                         |
Shopify                           | Vulnerable     | `Sorry, this shop is currently unavailable.`                            |[Issue #32](https://github.com/EdOverflow/can-i-take-over-xyz/issues/32)| [Medium Article](https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75) 
Squarespace                   | Not vulnerable |                                                                         |
Statuspage                     | Vulnerable     | `You are being redirected`                                              | [HackerOne #49663](https://hackerone.com/reports/49663)
Surge.sh                         | Vulnerable     | `project not found`                                                     || [Surge Documentation](https://surge.sh/help/adding-a-custom-domain)
Tumblr                             | Vulnerable     | `Whatever you were looking for doesn't currently exist at this address` |
Tilda                               | Not vulnerable | `Please renew your subscription`                                        |
Unbounce                         | Not vulnerable | `The requested URL was not found on this server.`                       | [Issue #11](https://github.com/EdOverflow/can-i-take-over-xyz/issues/11)
UserVoice                       | Vulnerable     | `This UserVoice subdomain is currently available!`                      |
Wordpress                       | Vulnerable     | `Do you want to register *.wordpress.com?`                              |
WP Engine                       | Not vulnerable |                                                                         |
Zendesk                           | Vulnerable     | `Help Center Closed`                                                    | [Issue #23](https://github.com/EdOverflow/can-i-take-over-xyz/issues/23) | [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)
