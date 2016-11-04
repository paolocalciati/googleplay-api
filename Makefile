# Sample makefile to show how to use this project

# Complete list of categories. This list can be retrieved with the Googleplay API as well. 
CATEGORIES=ANDROID_WEAR ART_AND_DESIGN AUTO_AND_VEHICLES BEAUTY BOOKS_AND_REFERENCE BUSINESS COMICS COMMUNICATION DATING EDUCATION ENTERTAINMENT EVENTS FINANCE FOOD_AND_DRINK GAME HEALTH_AND_FITNESS HOUSE_AND_HOME LIBRARIES_AND_DEMO LIFESTYLE MAPS_AND_NAVIGATION MEDICAL MUSIC_AND_AUDIO NEWS_AND_MAGAZINES PERSONALIZATION PHOTOGRAPHY PRODUCTIVITY SHOPPING SOCIAL SPORTS TOOLS TRAVEL_AND_LOCAL VIDEO_PLAYERS WEATHER

TODAY=$(shell date +'%d-%m-%Y')

# scripts folder
SCRIPTSFOLDER=$(shell pwd)
# output folder
OUTFOLDER=output
# parameter to retrieve the top N apps
TOP_APPS_NUM=100
# file listing all top N apps of each category
TOP_APPS_EACH_CAT=$(OUTFOLDER)/top_$(TOP_APPS_NUM)_apps_$(TODAY).txt

APPS:=$(shell cat $(TOP_APPS_EACH_CAT))
DOWNLOAD_ALL_APPS:=$(APPS:%=$(OUTFOLDER)/%.apk)
REVIEWS_ALL_APPS:=$(APPS:%=$(OUTFOLDER)/%-reviews.json)
DETAILS_ALL_APPS:=$(APPS:%=$(OUTFOLDER)/%-details.json)

getListTopApps: $(TOP_APPS_EACH_CAT)
downloadTopApps:$(DOWNLOAD_ALL_APPS)
reviewsTopApps:$(REVIEWS_ALL_APPS)
detailsTopApps:$(DETAILS_ALL_APPS)


# Retrieve the list of top N apps for each category and save it to file TOP_APPS_EACH_CAT
$(TOP_APPS_EACH_CAT):
	test -e $(OUTFOLDER) | mkdir -p $(OUTFOLDER)
	for i in $(CATEGORIES); do \
		echo "Category:" $$i; \
		python $(SCRIPTSFOLDER)/list.py $$i apps_topselling_free $(TOP_APPS_NUM) | \
			cut -f2 -d';' | \
			sed '/^Package .*/d' | \
			sed '/^list\?.*/d' >> $@.temp; \
		sleep 3; \
	done
	cat $@.temp | sort | uniq > $@
	rm $@.temp

# Download all the apks that are listed in TOP_APPS_EACH_CAT
$(OUTFOLDER)/%.apk:
	cd $(OUTFOLDER); \
	echo '** Downloading $*.apk'; \
	python $(SCRIPTSFOLDER)/download.py $*
	sleep 3

# Download all the reviews that of the apps that are listed in TOP_APPS_EACH_CAT
$(OUTFOLDER)/%-reviews.json:
	echo '** Downloading the 500 most recent reviews for $*'
	python $(SCRIPTSFOLDER)/reviews.py $* 500 > $@
	sleep 3

# Download the details of the apps that are listed in TOP_APPS_EACH_CAT
$(OUTFOLDER)/%-details.json:
	echo '** Downloading the details (description among others) for $*'
	python $(SCRIPTSFOLDER)/details.py $* > $@
	sleep 3
