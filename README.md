# Our Local API

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

See [docs](https://github.com/OurLocal/our-local-stories-api/docs/import-data.md).

## Usage

```
> curl http://127.0.0.1:8080?search=Crocodiles
[{
  'title': 'Mittagong Greeny Flat shows eco-living made easy',
  'url': 'http://www.abc.net.au/local/photos/2014/05/26/4012255.htm',
  'date': '26/05/2014',
  'primary_image': 'http://www.abc.net.au/reslib/201405/r1280295_17329764.jpg',
  'subjects': ['blah', 'something', 'another'],
  'latitude': -34.4516,
  'longitude': 150.4445
  },{
   'title': 'Yadda',
   'url': 'http://www.abc.net.au/local/photos/2014/05/26/4012255.htm',
   'date': '26/05/2014',
   'primary_image': 'http://www.abc.net.au/reslib/201405/r1280295_17329764.jpg',
   'subjects': ['blah', 'something', 'another'],
   'latitude': -54.4516,
   'longitude': 160.4445
}]
```
