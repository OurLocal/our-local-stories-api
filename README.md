# Our Local API

**Note: this is a Govhack project built in a weekend, don't rely on it yet! PRs welcome.**

A simple API for querying the ABC Local Online Photo Stories 2009-2014 data set:

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

## Usage

```
> curl http://127.0.0.1:8080?search=Crocodiles
```
