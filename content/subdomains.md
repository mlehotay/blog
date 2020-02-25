Title: DNS Subdomains
Date: 2020-02-21 00:00
Modified: 2020-02-24 21:23
Category: Web Apps
Tags: DNS, configuration
Slug: subdomains
Status: published

Today we're going to set up some DNS resource records for the web apps I built in my data science bootcamp. There are three of them; one is hosted on Digital Ocean and the other two are on Heroku.

* Broccoli Recommender is running at [142.93.153.10](http://142.93.153.10/)
* PokePredictor is running at [pokepredictor.herokuapp.com](http://pokepredictor.herokuapp.com/)
* Abalone Calculator is running at [mollusc.herokuapp.com](http://mollusc.herokuapp.com/)

I suppose I could buy domain names for each one and and give them names like broccoli.com or my-cool-app.xyz but I don't want to pay for three new domain names. I already have a domain (floatingeye.net) and we can give these web apps addresses that are subdomains of the domain that I already own.

Setting this up on Digital Ocean is a bit easier than on Heroku so let's do the Broccoli Recommender first.

Start by logging into Digital Ocean and clicking on the project in the sidebar. The name of our droplet is displayed along with the IP address where it is running. We need that IP address.

Digital Ocean has DNS tools to manage your domain but we're not going to use them. I'm already using Nearly Free Speech's DNS hosting service and I don't want to switch. The steps should be pretty similar for any DNS hosting provider.

Now I'll logging into my web hosting account and find the DNS Management page.

![DNS Management tools]({static}/images/nfs-dns.png)

Since the address we have at Digital Ocean is an IP address we'll need add an A record to the DNS table. If the address was a hostname we would add a CNAME record. (We'll do that for Heroku next.)

![DNS Resource Record entry]({static}/images/nfs-dns-record.png)

![Broccoli DNS Resource Record]({static}/images/broccoli-dns.png)

And that's it! Broccoli Recommender is now accessible at [http://broccoli.floatingeye.net](http://broccoli.floatingeye.net)!

[more coming soon]