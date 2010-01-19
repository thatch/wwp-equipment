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

DEST_SSH = thatch@timhatch.com:timhatch.com/projects/wwp-equipment/

.PHONY: all fetch parse template upload test graph upload-graph

all: template

fetch: getinfo.py $(EQUIP)
parse: autoparse.py $(DATA_CSV)
template: stuff.php $(DATA_HTML)

upload: $(DATA_HTML) $(DATA_CSV)
	@echo "====Uploading"
	rsync -av $^ $(DEST_SSH)

test:
	@echo $(DATA_HTML)

upload-graph:
	rsync -av graph/*.png $(DEST_SSH)/graph

graph:
	[ ! -d graph ] && mkdir graph || true
	python grapher4.py "$(EVENTS)" $(WORK_DIR)/*.csv

data-%.html: data-%.csv stuff.php
	@echo "====Templating to $@"
	php stuff.php $* $< > $@

data-%.csv: equip-%.txt defs.py
	@echo "====Autoparsing to $@"
	python autoparse.py $< > $@

equip-%.txt:
	@echo "====Fetching $@"
	python getinfo.py $(patsubst $(WORK_DIR)/%,%,$*) > $@
