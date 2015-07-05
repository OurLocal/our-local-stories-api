import json
import datetime
import pprint

from django.http import HttpResponse
from django.shortcuts import render_to_response
from app.models import Story
from datetime import datetime as dt
from django.core.exceptions import SuspiciousOperation
from django.contrib.gis.geos import Point, Polygon



RESULTS_HARD_LIMIT = 100


def api(request):

    """
    Handle the follow params:

    ?search=Something+yadda
    &start=2009-01-01-2014-12-30&end=2014-12-30
    &point=??
    &box=??
    
    Code mostly written by Lyndon D'arcy
    (imported from https://github.com/logworthy/govhack2015).
    """

    search = request.GET.get('search', None)
    limit = request.GET.get('limit', '10')

    # date/window to limit stories
    date = request.GET.get('date', '2014-12-30')
    window = request.GET.get('window', None)

    # start/end to limit stories
    start = request.GET.get('start', '2009-01-01')
    end = request.GET.get('end', '2014-12-30')

    # point to geo stories
    # should be lon, lat
    point = request.GET.get('point', None)
    box = request.GET.get('box', None)

    # check types for key numeric querystring parameters
    try:
        start_date = dt.strptime(start, '%Y-%m-%d')
        end_date = dt.strptime(end, '%Y-%m-%d')
        date_date = dt.strptime(date, '%Y-%m-%d')
        if window != None:
            window_int = int(window)
        limit_int = min(int(limit), RESULTS_HARD_LIMIT)

        # check that point is a legit point
        point_point = None
        if point != None:
            point_point = Point([float(x) for x in point.split(',')])
        
        # check that box is two legit points
        box_poly = None
        if box != None:
            box1, box2 = box.split(':')
            x1, y1 = box1.split(',')
            x2, y2 = box2.split(',')
            box_poly = Polygon.from_bbox((x1,y1,x2,y2))

        # if both exist check that point is within box
        if point_point != None and box_poly != None:
            assert(box_poly.prepared.contains(point_point))

    except Exception as e:
        raise SuspiciousOperation(
            'Query string does not conform. Exception: {}'.format(e))

    # base query
    if search != None:
        base_query = Story.objects.search(search)
    else:
        base_query = Story.objects.all()

    # window limits
    window_query = base_query
    if window != None:
        window_start = date_date - datetime.timedelta(days=window_int)
        window_end = date_date + datetime.timedelta(days=window_int)
        window_query = base_query.filter(date__gte=window_start, date__lte=window_end)

    # date limits
    date_query = window_query.filter(date__gte=start_date, date__lte=end_date)

    # geo limits
    geo_query = date_query
    if box_poly != None:
        geo_query = date_query.filter(location__contained=box_poly)

    # sort and limit
    # closest in time to date_date
    # closest in space to point_point
    # most relevant
    story_list = geo_query.order_by('-date')[:limit_int]

    # convert to dict
    story_dicts = [{
        'id': s.id,
        'title': s.title
        , 'url': s.url
        , 'date': s.date.strftime('%d/%m/%Y')
        , 'primary_image': s.primary_image
        , 'primary_image_caption': s.primary_image_caption
        , 'subjects': s.subjects
        , 'latitude': s.location.coords[0]
        , 'longitude': s.location.coords[1] 
    } for s in story_list]

    if request.GET.get('pretty'):
        output = json.dumps(story_dicts, sort_keys=True, indent=2)
    else:
        output = json.dumps(story_dicts)

    response = HttpResponse(output, content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'
    return response
