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

## How to use this project

I recommend searching for the name of the service you are targeting in the issues tab. That way you can see the on-going discussion and more detailed steps on how to claim the subdomain you are after.

## How to contribute

You can submit new services here: https://github.com/EdOverflow/can-i-take-over-xyz/issues/new?template=new-entry.md.

A list of services that can be checked (although check for duplicates against this list first) can be found here: https://github.com/EdOverflow/can-i-take-over-xyz/issues/26.

# All entries

Engine                                        | Status         | Fingerprint                                                             | Discussion                                                    | Documentation
--------------------------------------------- | -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------
Acquia | Not vulnerable | `Web Site Not Found` |[Issue #103](https://github.com/EdOverflow/can-i-take-over-xyz/issues/103)
Agile CRM | Vulnerable | `Sorry, this page is no longer available.` |[Issue #145](https://github.com/EdOverflow/can-i-take-over-xyz/issues/145)
Airee.ru                             | Vulnerable     | | [Issue #104](https://github.com/EdOverflow/can-i-take-over-xyz/issues/104) |
Anima | Vulnerable | `If this is your website and you've just created it, try refreshing in a minute` | [Issue #126](https://github.com/EdOverflow/can-i-take-over-xyz/issues/126) | [Anima Documentation](https://docs.animaapp.com/v1/launchpad/08-custom-domain.html)
Akamai                                        | Not vulnerable | | [Issue #13](https://github.com/EdOverflow/can-i-take-over-xyz/issues/13) |
AWS/S3                             | Vulnerable     | `The specified bucket does not exist`                                   | [Issue #36](https://github.com/EdOverflow/can-i-take-over-xyz/issues/36)
AWS/Load Balancer (ELB)                             | Not Vulnerable     | status NXDOMAIN and CNAME pointing to XYZ.elb.amazonaws.com                                 | [Issue #137](https://github.com/EdOverflow/can-i-take-over-xyz/issues/137)
Bitbucket                       | Vulnerable     | `Repository not found`                                                  |
Campaign Monitor         | Vulnerable     |               `Trying to access your account?`                                                          |                                                               | [Support Page](https://help.campaignmonitor.com/custom-domain-names)
Cargo Collective         | Vulnerable     | `404 Not Found`                                                         |                                                               | [Cargo Support Page](https://support.2.cargocollective.com/Using-a-Third-Party-Domain)
Cloudfront                     | Not vulnerable      | ViewerCertificateException            | [Issue #29](https://github.com/EdOverflow/can-i-take-over-xyz/issues/29) | [Domain Security on Amazon CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/continually-enhancing-domain-security-on-amazon-cloudfront/)
Desk                                 | Not vulnerable     | `Please try again or try Desk.com free for 14 days.`                    | [Issue #9](https://github.com/EdOverflow/can-i-take-over-xyz/issues/9)
Digital Ocean | Vulnerable | Domain uses DO name serves with no records in DO. |   |   |
Discourse | Vulnerable | | | [Hackerone](https://hackerone.com/reports/264494)
Fastly                             | Edge case     | `Fastly error: unknown domain:`                                         | [Issue #22](https://github.com/EdOverflow/can-i-take-over-xyz/issues/22)
Feedpress                       | Not vulnerable     | `The feed has not been found.`                                          | [Issue #80](https://github.com/EdOverflow/can-i-take-over-xyz/issues/80)
Firebase | Not vulnerable | | [Issue #128](https://github.com/EdOverflow/can-i-take-over-xyz/issues/128) |
Fly.io                             | Vulnerable     | `404 Not Found`                                         | [Issue #101](https://github.com/EdOverflow/can-i-take-over-xyz/issues/101)
Freshdesk                       | Not vulnerable |                                                                         || [Freshdesk Support Page](https://support.freshdesk.com/support/solutions/articles/37590-using-a-vanity-support-url-and-pointing-the-cname)
Gemfury | Vulnerable | `404: This page could not be found.` | [Issue #154](https://github.com/EdOverflow/can-i-take-over-xyz/issues/154) | [Article](https://khaledibnalwalid.wordpress.com/2020/06/25/gemfury-subdomain-takeover/)
Ghost                               | Vulnerable     | `The thing you were looking for is no longer here, or never was`        |
Github                             | Vulnerable     | `There isn't a Github Pages site here.`                                 | [Issue #37](https://github.com/EdOverflow/can-i-take-over-xyz/issues/37) [Issue #68](https://github.com/EdOverflow/can-i-take-over-xyz/issues/68)
Gitlab                             | Not vulnerable |                                                                         | [HackerOne #312118](https://hackerone.com/reports/312118)
Google Cloud Storage | Not vulnerable |   <?xml version='1.0' encoding='UTF-8'?><Error><Code>NoSuchBucket</Code><Message>The specified bucket does not exist.</Message></Error>                                                                      |
HatenaBlog | vulnerable | `404 Blog is not found`                                                                         |
Help Juice                     | Vulnerable     | `We could not find what you're looking for.`                            |                                                               | [Help Juice Support Page](https://help.helpjuice.com/en_US/using-your-custom-domain/how-to-set-up-a-custom-domain)
Help Scout                     | Vulnerable     | `No settings were found for this company:`                              |                                                               | [HelpScout Docs](https://docs.helpscout.net/article/42-setup-custom-domain)
Heroku                             | Edge case     | `No such app`                                                           | [Issue #38](https://github.com/EdOverflow/can-i-take-over-xyz/issues/38)
HubSpot                            | Not vulnerable | `This page isn’t available`
Instapage | Not vulnerable | | [Issue #73](https://github.com/EdOverflow/can-i-take-over-xyz/issues/73) | |
Intercom                          | Vulnerable     | `Uh oh. That page doesn't exist.`                                         | [Issue #69](https://github.com/EdOverflow/can-i-take-over-xyz/issues/69) | [Help center](https://www.intercom.com/help/)
JetBrains                       | Vulnerable     | `is not a registered InCloud YouTrack`                                  | | [YouTrack InCloud Help Page](https://www.jetbrains.com/help/youtrack/incloud/Domain-Settings.html)
Key CDN                             | Not vulnerable     | | [Issue #112](https://github.com/EdOverflow/can-i-take-over-xyz/issues/112) |
Kinsta                           | Vulnerable     | `No Site For Domain`                                                 |[Issue #48](https://github.com/EdOverflow/can-i-take-over-xyz/issues/48) | [kinsta-add-domain](https://kinsta.com/knowledgebase/add-domain/)
Landingi  | Edge case     | `It looks like you’re lost...` | [Issue #117](https://github.com/EdOverflow/can-i-take-over-xyz/issues/117)
LaunchRock                         | Vulnerable     | `It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.`                                                 |[Issue #74](https://github.com/EdOverflow/can-i-take-over-xyz/issues/74) | 
Mashery                           | Edge Case | `Unrecognized domain`                                                   | [HackerOne #275714](https://hackerone.com/reports/275714), [Issue #14](https://github.com/EdOverflow/can-i-take-over-xyz/issues/14)
Microsoft Azure           | Vulnerable     |  | [Issue #35](https://github.com/EdOverflow/can-i-take-over-xyz/issues/35) |
Netlify | Edge Case | | [Issue #40](https://github.com/EdOverflow/can-i-take-over-xyz/issues/40) |
Ngrok | Vulnerable | `Tunnel *.ngrok.io not found` | [Issue #92](https://github.com/EdOverflow/can-i-take-over-xyz/issues/92) | [Ngrok Documentation](https://ngrok.com/docs#http-custom-domains)
Pantheon                           | Vulnerable     | `404 error unknown site!`                                                 |[Issue #24](https://github.com/EdOverflow/can-i-take-over-xyz/issues/24) | [Pantheon-Sub-takeover](https://medium.com/@hussain_0x3c/hostile-subdomain-takeover-using-pantheon-ebf4ab813111)
Pingdom | Vulnerable | `Sorry, couldn't find the status page` | [Issue #144](https://github.com/EdOverflow/can-i-take-over-xyz/issues/144) | [Support Page](https://help.pingdom.com/hc/en-us/articles/205386171-Public-Status-Page)
Readme.io | Vulnerable | `Project doesnt exist... yet!` | [Issue #41](https://github.com/EdOverflow/can-i-take-over-xyz/issues/41)
Sendgrid                         | Not vulnerable |                                                                         |
Shopify                           | Edge Case     | `Sorry, this shop is currently unavailable.`                            |[Issue #32](https://github.com/EdOverflow/can-i-take-over-xyz/issues/32), [Issue #46](https://github.com/EdOverflow/can-i-take-over-xyz/issues/46)| [Medium Article](https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75) 
SmartJobBoard | Vulnerable | `This job board website is either expired or its domain name is invalid.` | [Issue #139](https://github.com/EdOverflow/can-i-take-over-xyz/issues/139) | [Support Page](https://help.smartjobboard.com/en/articles/1269655-connecting-a-custom-domain-name)
Smartling| Edge Case|`Domain is not configured`  | [Issue #67](https://github.com/EdOverflow/can-i-take-over-xyz/issues/67)
Squarespace                   | Not vulnerable |                                                                         |
Statuspage | Not Vulnerable | `Status page pushed a DNS verification in order to prevent malicious takeovers what they mentioned in` [This Doc](https://support.atlassian.com/statuspage/docs/configure-your-dns/) | [PR #105](https://github.com/EdOverflow/can-i-take-over-xyz/pull/105) and [PR #171](https://github.com/EdOverflow/can-i-take-over-xyz/pull/171) | [Statuspage documentation](https://help.statuspage.io/knowledge_base/topics/domain-ownership) |          
Strikingly                           | Vulnerable     | `page not found`                                                 |[Issue #58](https://github.com/EdOverflow/can-i-take-over-xyz/issues/58) | [Strikingly-Sub-takeover](https://medium.com/@sherif0x00/takeover-subdomains-pointing-to-strikingly-5e67df80cdfd)
Surge.sh                         | Vulnerable     | `project not found`                                                     || [Surge Documentation](https://surge.sh/help/adding-a-custom-domain)
Tumblr                             | Edge Case     | `Whatever you were looking for doesn't currently exist at this address` |
Tilda                               | Edge Case | `Please renew your subscription`                                        | [Issue #155](https://github.com/EdOverflow/can-i-take-over-xyz/issues/155)[PR #20](https://github.com/EdOverflow/can-i-take-over-xyz/pull/20)
Uberflip | Vulnerable | `Non-hub domain, The URL you've accessed does not provide a hub.` | [Issue #150](https://github.com/EdOverflow/can-i-take-over-xyz/issues/150) | [Uberflip Documentation](https://help.uberflip.com/hc/en-us/articles/360018786372-Custom-Domain-Set-up-Your-Hub-on-a-Subdomain)
Unbounce                         | Edge Case | `The requested URL was not found on this server.`                       | [Issue #11](https://github.com/EdOverflow/can-i-take-over-xyz/issues/11)
Uptimerobot                           | Vulnerable     | `page not found`                                                 |[Issue #45](https://github.com/EdOverflow/can-i-take-over-xyz/issues/45) | [Uptimerobot-Sub-takeover](https://exploit.linuxsec.org/uptimerobot-com-custom-domain-subdomain-takeover/)
UserVoice                       | Vulnerable     | `This UserVoice subdomain is currently available!`                      |
Webflow                           | Edge Case     | `The page you are looking for doesn't exist or has been moved.` |[Issue #44](https://github.com/EdOverflow/can-i-take-over-xyz/issues/44) |[forum webflow](https://forum.webflow.com/t/hosting-a-subdomain-on-webflow/59201)
Wordpress                       | Vulnerable     | `Do you want to register *.wordpress.com?`                              |
Worksites | Vulnerable | `Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist.` | [Issue #142](https://github.com/EdOverflow/can-i-take-over-xyz/issues/142) | 
WP Engine                       | Not vulnerable |                                                                         |
Zendesk                           | Not vulnerable     | `Help Center Closed`                                                    | [Issue #23](https://github.com/EdOverflow/can-i-take-over-xyz/issues/23) | [Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203664356-Changing-the-address-of-your-Help-Center-subdomain-host-mapping-)
