EVENTS = 304 604 904 1204 \
         305 605 905 1205 \
         306 606 906 1206 \
         307 607 907 1207 108 \
         308 608 908 1208

WORK_DIR = new


DATA_HTML = $(patsubst %,$(WORK_DIR)/data-%.html,$(EVENTS))
DATA_CSV = $(patsubst %,$(WORK_DIR)/data-%.csv,$(EVENTS))
EQUIP = $(patsubst %,$(WORK_DIR)/equip-%.txt,$(EVENTS))

DATA_LIVE = $(patsubst %,$(WORK_DIR)/data-%.live,$(EVENTS))

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
	rsync -av $^ thatch@timhatch.com:timhatch.com/projects/wwp-equipment/

test:
	@echo $(DATA_HTML)

.PHONY: all fetch parse template upload test yuval graph upload-graph

upload-graph:
	rsync -av graph/*.png \
	thatch@timhatch.com:timhatch.com/projects/wwp-equipment/graph

graph:
	python grapher3.py new/*.csv
	(cd graph; for f in *.sh; do sh $$f; done)

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
