import os

import jinja2
import TileStache

application = None

infile = 'tilestache.cfg'
outfile = 'tilestache-cfg-rendered.cfg'

try:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('/nepal-tiles/'))
    template = env.get_template(infile)
    rendered = template.render(os.environ)
except Exception as e:
    print("Error rendering template: " + e.message)
    with open(infile, 'rb') as f:
        rendered = f.read()

with open(outfile, 'wb') as f:
    f.write(rendered)


application = TileStache.WSGITileServer(outfile)
