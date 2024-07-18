Title: Deploying a Docker Container to Digital Ocean with sshfs
Date: 2020-02-21 00:00
Modified: 2020-02-25 13:31
Category: Web Apps
Tags: configuration, make, deployment
Slug: digital-ocean
Status: published
Comments: true


In this post I'll talk about the way I set up the directory structure for my data science bootcamp capstone project, and how I mounted my droplet in my local file system in order to deploy my web application. I also used of a couple of makefiles so I didn't have to keep re-typing the same long shell commands in the terminal and I'll explain how that works too.

![Broccoli directory structure]({static}/images/directory-structure.png)

------

Here's the makefile on my local system:

```makefile
mount:
	sshfs broccoli.floatingeye.net:/home/mlehotay/broccoli broccoli

umount:
	sudo umount broccoli

upload:
	rm -rf broccoli/app/

	mkdir broccoli/app
	cp foods.py broccoli/app/
	cp main.py broccoli/app/

	mkdir broccoli/app/static
	mkdir broccoli/app/static/images
	cp -r images/*.jpg broccoli/app/static/images/

	mkdir broccoli/app/templates
	cp templates/index.html broccoli/app/templates/
	cp templates/recommend.html broccoli/app/templates/
	cp templates/survey.html broccoli/app/templates/
	cp templates/thankyou.html broccoli/app/templates/
	cp templates/gtag.html broccoli/app/templates/

	mkdir broccoli/app/data
	mkdir broccoli/app/data/json
	cp data/db.py broccoli/app/data/
	cp data/foods.csv broccoli/app/data/

download:
	cp -pr broccoli/backup/ .

login:
	ssh broccoli.floatingeye.net
```

------

Here's the makefile on the droplet:

```makefile
build:
	docker build -t appimage .
run:
	docker run -d --name appcontainer -p 80:80 appimage
	docker cp backup/broccoli.db appcontainer:/app/data/
stop:
	docker stop appcontainer
cleanup: backup
	docker rmi -f appimage &&\
	docker rm appcontainer

data:
	-mv broccoli.db broccoli.`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 8`.db
	-docker cp appcontainer:/app/data/broccoli.db .
	-docker cp appcontainer:/app/data/json/ .

backup: data
	cp -pr broccoli*.db json/ backup/

clean-data: backup
	rm broccoli*.db
	rm json/*.json
```

------

And here are the commands I run to deploy my app:

```typescript
$ cd sandbox/broccoli
$ make mount
$ make upload
$ make login

$ cd broccoli
$ make stop
$ make cleanup
$ make build
$ make run
$ exit

$ make download
$ make umount
```



### Links

* [GNU Make](https://www.gnu.org/software/make/)
* [How To Use SSHFS to Mount Remote File Systems Over SSH](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)
