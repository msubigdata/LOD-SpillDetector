import json
import random

import geopy
from geopy import distance


def append_area(area):
    d = geopy.distance.geodesic(
        kilometers=geopy.distance.distance((area[0][0], area[0][1]), (area[0][0], area[1][1])).km / 2)
    bg = d.destination(point=d.destination(point=(area[1][0], area[1][1]), bearing=0), bearing=90)
    sm = d.destination(point=d.destination(point=(area[0][0], area[0][1]), bearing=180), bearing=270)
    return [[sm[0], sm[1]], [bg[0], bg[1]]]


def create_markers(label):
    dataset = json.loads(open(f'dataset-{label}.json').read())

    colors = ['green', 'orange', 'yellow', 'red']
    markers = []

    last_file = {'name': None, 'id': 0}
    j = -1

    for i, item in enumerate(dataset):
        if i >= 2000:
            break
        if last_file['name'] == item['filename'].split('-')[1].split('_')[0]:
            markers[last_file['id']]['images'].append({
                'timestamp': item['timestamp'],
                'url': f"api/media/{item['filename']}"
            })
            continue
        else:
            j += 1

        area = [[item['bbox'][1], item['bbox'][0]],
                [item['bbox'][3], item['bbox'][2]]]

        markers.append({
            'spill': bool(random.randint(0, 1)),
            'area': [
                area, append_area(area), append_area(append_area(area))
            ],
            'color': random.choice(colors),
            'images': [
                {
                    'timestamp': item['timestamp'],
                    'url': f"/api/media/{label}/{item['filename']}"
                }
            ]
        })
        last_file['name'] = item['filename'].split('-')[1].split('_')[0]
        last_file['id'] = j

        open(f'markers-{label}.json', 'w').write(json.dumps(markers))


create_markers(2017)
