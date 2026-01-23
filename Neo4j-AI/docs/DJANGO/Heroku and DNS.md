## Q:
What level of support for hosting domains does Heroku provide?
## A:
You asked about Heroku’s level of support for hosting domains. Here’s what I found:⸻

✅ What Heroku Provides

- Default Domain: Every Heroku app comes with a built-in Heroku subdomain like appname-identifier.herokuapp.com. This is automatically available and secured with DNSSEC.[1](https://devcenter.heroku.com/articles/custom-domains)
- Custom Domains: You can add custom domains (e.g., www.wisdombook.life) to any Heroku app at no extra cost. This requires:

- Verifying your Heroku account.
- Configuring your DNS provider to point to Heroku’s DNS target.
- Using the Heroku CLI (heroku domains:add) or API for domain management.[1](https://devcenter.heroku.com/articles/custom-domains)[2](https://help.heroku.com/MTG1BIA7/how-do-i-connect-a-domain-to-my-heroku-app)

- SSL Support: Automated Certificate Management (ACM) handles SSL for custom domains by default. For apps with more than 1,000 domains, you may need SAN certificates or third-party solutions like Cloudflare.[3](https://help.heroku.com/TV5IYK1Y/how-can-i-create-subdomains-for-all-my-users)
- Limits: Each app can have up to 1,000 custom domains, and this limit can be increased by submitting a support ticket.[3](https://help.heroku.com/TV5IYK1Y/how-can-i-create-subdomains-for-all-my-users)
- HTTP/2 Support: Available only on custom domains, not on the default herokuapp.com domain.[4](https://hackernoon.com/custom-domains-for-http2-on-heroku-its-so-easy)

⸻

❌ What Heroku Does NOT Provide

- Domain Registration: Heroku does not sell or register domain names.
- DNS Hosting: You must use an external DNS provider to manage your domain records.[1](https://devcenter.heroku.com/articles/custom-domains)[2](https://help.heroku.com/MTG1BIA7/how-do-i-connect-a-domain-to-my-heroku-app)

⸻

🔒 Security

- DNSSEC is enabled for all Heroku-managed domains.
- SSL/TLS is automatically managed via ACM for custom domains.[1](https://devcenter.heroku.com/articles/custom-domains)

⸻

In short: Heroku supports adding and managing custom domains for your apps, including SSL and HTTP/2, but you need an external registrar and DNS provider. It’s a flexible system, but not a full domain hosting service.

Would you like me to give you a step-by-step guide on how to connect a custom domain to your Heroku app, or compare Heroku’s domain support with other platforms like AWS or Netlify?

