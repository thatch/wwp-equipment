EVENTS = 304 604 904 1204 \
         305 605 905 1205 \
         306 606 906 1206 \
         307 607 907 1207 108 \
         308 608 908 1208 \
         309 609 909 1209

WORK_DIR = new


DATA_HTML = $(patsubst %,$(WORK_DIR)/data-%.html,$(EVENTS))
DATA_CSV = $(patsubst %,$(WORK_DIR)/data-%.csv,$(EVENTS))
EQUIP = $(patsubst %,$(WORK_DIR)/equip-%.txt,$(EVENTS))

DATA_LIVE = $(patsubst %,$(WORK_DIR)/data-%.live,$(EVENTS))
DEST_SSH = thatch@timhatch.com:timhatch.com/projects/wwp-equipment/

all: template

fetch: getinfo.py $(EQUIP)
parse: autoparse.py $(DATA_CSV)
template: stuff.php $(DATA_HTML)

#upload: $(DATA_LIVE)
#data-%.live: data-%.html
#	scp $< thatch@timhatch.com:timhatch.com/projects/wwp-equipment/
#	@touch $@

upload: $(DATA_HTML) $(DATA_CSV)
	@echo "====Uploading"
	rsync -av $^ $(DEST_SSH)

test:
	@echo $(DATA_HTML)

.PHONY: all fetch parse template upload test yuval graph upload-graph

upload-graph:
	rsync -av graph/*.png $(DEST_SSH)/graph

graph:
	python grapher4.py "$(EVENTS)" new/*.csv

yuval:
	rm -f yuval.csv
	for f in $(EVENTS); do echo $$f; python get_yuval.py $$f >> yuval.csv; done

data-%.html: data-%.csv
	@echo "====Templating to $@"
	php stuff.php $* $< > $@

data-%.csv: equip-%.txt
	@echo "====Autoparsing to $@"
	python autoparse.py $< > $@

equip-%.txt:
	@echo "====Fetching $@"
	python getinfo.py $(patsubst new/%,%,$*) > $@
