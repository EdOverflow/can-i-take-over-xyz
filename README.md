![image](https://user-images.githubusercontent.com/18099289/45263787-a4bbc880-b430-11e8-9cff-eb6e4c796050.png)

## Disclaimer :warning:

**The authors of this document take no responsibility for correctness. This project is merely here to help guide security researchers towards determining whether something is vulnerable or not, but does not guarantee accuracy. This project heavily relies on contributions from the public; therefore, proving that something is vulnerable is the security researcher and bug bounty program's sole discretion. On top of that, it is worth noting that some bug bounty programs may accept dangling DNS record reports without requiring proof of compromise.**

## What is a subdomain takeover?

> Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.

You can read up more about subdomain takeovers here:

- <https://labs.detectify.com/2014/10/21/hostile-subdomain-takeover-using-herokugithubdesk-more/>
- <https://www.hackerone.com/blog/Guide-Subdomain-Takeovers>
- <https://0xpatrik.com/subdomain-takeover-ns/>

## Safely demonstrating a subdomain takeover

Based on personal experience, claiming the subdomain discreetly and serving a harmless file on a hidden page is usually enough to demonstrate the security vulnerability. Do not serve content on the index page. A good proof of concept could consist of an HTML comment served via a random path:

```
$ cat aelfjj1or81uegj9ea8z31zro.html
<!-- PoC by username -->
```

Please be advised that this depends on what bug bounty program you are targeting. When in doubt, please refer to the bug bounty program's security policy and/or request clarifications from the team behind the program.

## How to contribute

You can submit new services here: https://github.com/EdOverflow/can-i-take-over-xyz/issues/new?template=new-entry.md.

A list of services that can be checked (although check for duplicates against this list first) can be found here: https://github.com/EdOverflow/can-i-take-over-xyz/issues/26.

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
Github                             | Vulnerable     | `There isn't a Github Pages site here.`                                 | [Issue #37](https://github.com/EdOverflow/can-i-take-over-xyz/issues/37) [Issue #68](https://github.com/EdOverflow/can-i-take-over-xyz/issues/68)
Gitlab                             | Not vulnerable |                                                                         | [HackerOne #312118](https://hackerone.com/reports/312118)
Google Cloud Storage | Not vulnerable |                                                                         |
Help Juice                     | Vulnerable     | `We could not find what you're looking for.`                            |                                                               | [Help Juice Support Page](https://help.helpjuice.com/34339-getting-started/custom-domain)
Help Scout                     | Vulnerable     | `No settings were found for this company:`                              |                                                               | [HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)
Heroku                             | Edge case     | `No such app`                                                           | [Issue #38](https://github.com/EdOverflow/can-i-take-over-xyz/issues/38)
Intercom                          | Vulnerable     | `Uh oh. That page doesn't exist.`                                         | [Issue #69](https://github.com/EdOverflow/can-i-take-over-xyz/issues/69) | [Help center](https://www.intercom.com/help/)
JetBrains                       | Vulnerable     | `is not a registered InCloud YouTrack`                                  |
Kinsta                           | Vulnerable     | `No Site For Domain`                                                 |[Issue #48](https://github.com/EdOverflow/can-i-take-over-xyz/issues/48) | [kinsta-add-domain](https://kinsta.com/knowledgebase/add-domain/)
LaunchRock                         | Vulnerable     | `It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.`                                                 |[Issue #74](https://github.com/EdOverflow/can-i-take-over-xyz/issues/74) | 
Mashery                           | Edge Case | `Unrecognized domain`                                                   | [HackerOne #275714](https://hackerone.com/reports/275714), [Issue #14](https://github.com/EdOverflow/can-i-take-over-xyz/issues/14)
Microsoft Azure           | Vulnerable     |  | [Issue #35](https://github.com/EdOverflow/can-i-take-over-xyz/issues/35) |
Netlify | Edge Case | | [Issue #40](https://github.com/EdOverflow/can-i-take-over-xyz/issues/40) |
Pantheon                           | Vulnerable     | `404 error unknown site!`                                                 |[Issue #24](https://github.com/EdOverflow/can-i-take-over-xyz/issues/24) | [Pantheon-Sub-takeover](https://medium.com/@hussain_0x3c/hostile-subdomain-takeover-using-pantheon-ebf4ab813111)
Readme.io | Vulnerable | `Project doesnt exist... yet!` | [Issue #41](https://github.com/EdOverflow/can-i-take-over-xyz/issues/41)
Sendgrid                         | Not vulnerable |                                                                         |
Shopify                           | Edge Case     | `Sorry, this shop is currently unavailable.`                            |[Issue #32](https://github.com/EdOverflow/can-i-take-over-xyz/issues/32), [Issue #46](https://github.com/EdOverflow/can-i-take-over-xyz/issues/46)| [Medium Article](https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75) 
Squarespace                   | Not vulnerable |                                                                         |
Statuspage                     | Not vulnerable |                                                                         | [PR #65](https://github.com/EdOverflow/can-i-take-over-xyz/pull/65)
Strikingly                           | Vulnerable     | `page not found`                                                 |[Issue #58](https://github.com/EdOverflow/can-i-take-over-xyz/issues/58) | [Strikingly-Sub-takeover](https://medium.com/@sherif0x00/takeover-subdomains-pointing-to-strikingly-5e67df80cdfd)
Surge.sh                         | Vulnerable     | `project not found`                                                     || [Surge Documentation](https://surge.sh/help/adding-a-custom-domain)
Tumblr                             | Vulnerable     | `Whatever you were looking for doesn't currently exist at this address` |
Tilda                               | Edge Case | `Please renew your subscription`                                        | [PR #20](https://github.com/EdOverflow/can-i-take-over-xyz/pull/20)
Unbounce                         | Not vulnerable | `The requested URL was not found on this server.`                       | [Issue #11](https://github.com/EdOverflow/can-i-take-over-xyz/issues/11)
Uptimerobot                           | Vulnerable     | `page not found`                                                 |[Issue #45](https://github.com/EdOverflow/can-i-take-over-xyz/issues/45) | [Uptimerobot-Sub-takeover](https://exploit.linuxsec.org/uptimerobot-com-custom-domain-subdomain-takeover/)
UserVoice                       | Vulnerable     | `This UserVoice subdomain is currently available!`                      |
Webflow                           | Vulnerable     | `404 Page Not Found`                                                |[Issue #44](https://github.com/EdOverflow/can-i-take-over-xyz/issues/44) |[forum webflow](https://forum.webflow.com/t/hosting-a-subdomain-on-webflow/59201)
Wordpress                       | Vulnerable     | `Do you want to register *.wordpress.com?`                              |
WP Engine                       | Not vulnerable |                                                                         |
Zendesk                           | Not Vulnerable     | `Help Center Closed`                                                    | [Issue #23](https://github.com/EdOverflow/can-i-take-over-xyz/issues/23) | [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)
