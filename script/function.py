import json

def download_file(a, b, c, d, e, f, g, h, name):
    result = {
        'chest': a,
        'righthand': b,
        'lefthand': c,
        'rightshoulder': d,
        'leftshoulder': e,
        'rightleg': f,
        'leftleg': g,
        'movingrobot': h
    }
    
    with open(f"data/{name}.json", 'w') as outfile:
        json.dump(result, outfile, indent=4)