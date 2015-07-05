# Our Local Stories API

<img src="http://www.abc.net.au/reslib/201408/r1314027_18113770.JPG" width=300></img><br>
[One man's obsession with Lego, ABC Northwest Queensland (2014)](http://www.abc.net.au/local/photos/2014/08/08/4063716.htm)

An self-hosted open-source API for querying the [ABC Local Online Photo Stories 2009-2014 data set](http://data.gov.au/dataset/abc-local-online-photo-stories-2009-2014)

**Note: this is a Govhack project built in a weekend, don't rely on it yet!**

***

## Features

  * Full-text search.
  * Location-based searches.
  * Date-range filtering.

## How to build

### System deps (just Debian-esque for now)

```
> apt-get update
> apt-get install -y postgresql postgresql-contrib
> apt-get install -y postgis postgresql-9.3-postgis-2.1
> apt-get install -y python-virtualenv
> createdb local_explorer
> sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" local_explorer
```

## Python

```
> git clone https://github.com/OurLocal/our-local-stories-api
> cd our-local-stories-api
> # Optional 2 lines below.
> virtualenv ENV
> . ENV/bin/activate
> pip install -r requirements.txt
> python manage.py migration
> python manage.py collectstatic
> python manage.py runserver
```

## Importing Data

See [docs](docs/import-data.md).

## Usage

```
> curl http://127.0.0.1:8000/?search=lego&pretty=1
[
  {
    "date": "08/08/2014", 
    "latitude": -20.7287, 
    "longitude": 139.4897, 
    "primary_image": "http://www.abc.net.au/reslib/201408/r1314027_18113770.JPG", 
    "primary_image_caption": "Several recognisable cartoon characters which Mr Kemp has created from square blocks of Lego. He says while sometimes he follows instructions, he often does his own thing. You do follow some instructions to a point and some you just grab and go 'I dont like that bit so Ill swap that bit with this bit' and before you know it youve got something completely different.", 
    "subjects": "Education:Play and Learning, Human Interest:People,", 
    "title": "One mans obsession with Lego", 
    "url": "http://www.abc.net.au/local/photos/2014/08/08/4063716.htm"
  }, 
  {
    "date": "21/05/2014", 
    "latitude": -30.7458, 
    "longitude": 121.4715, 
    "primary_image": "http://www.abc.net.au/reslib/201405/r1278944_17301720.jpg", 
    "primary_image_caption": "The Lego Travellers at Hellfire Bay in Cape Le Grand National Park, Esperance", 
    "subjects": "Lifestyle and Leisure:Travel and Tourism,", 
    "title": "The tiny travellers helping put Goldfields-Esperance on the map", 
    "url": "http://www.abc.net.au/local/photos/2014/05/21/4009029.htm"
  }
]
```
