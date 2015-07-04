## Data Import 

Author: Lyndon D'arcy (logworthy)

```
/* shell commands to run to clean the data (remove invalid unicode chars) */
iconv -f 'UTF-8' -t 'UTF-32' -c localphotostories20092014csv.csv -o localphotostories20092014csv.tmp
iconv -f 'UTF-32' -t 'UTF-8' -c localphotostories20092014csv.tmp -o localphotostories20092014.csv

/* run the rest of this in postgres */
sudo -u postgres psql pick_story

/* create the staging table */
drop table data_stage;
create table data_stage (
    "Title" text
    ,"URL" text
    ,"Date" text
    ,"Primary image" text
    ,"Primary image caption" text
    ,"Primary image rights information" text
    ,"Subjects" text
    ,"Station" text
    ,"State" text
    ,"Place" text
    ,"Keywords" text
    ,"Latitude" numeric
    ,"Longitude" numeric
    ,"MediaRSS URL" text
    );

COPY data_stage FROM './localphotostories20092014csv.csv' DELIMITER ',' CSV;

/* insert the staged data into the app_story table */
insert into app_story (title, url, date, primary_image, primary_image_caption, primary_image_rights_information, subjects, station, state, place, keywords, location) (
select 
	"Title"
	, "URL"
	, to_date("Date", 'DD/MM/YYYY')
	,"Primary image" 
	,"Primary image caption" 
	,"Primary image rights information" 
	, "Subjects"
	,"Station" 
	,"State" 
	,"Place" 
	,"Keywords"
	, ST_SetSRID(ST_POINT("Latitude", "Longitude"),4326) as location
from data_stage 
where "Latitude" is not null and "Longitude" is not null
);
```
