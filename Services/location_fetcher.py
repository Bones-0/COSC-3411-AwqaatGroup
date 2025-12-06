# Source - https://stackoverflow.com/a
# Posted by Apollo_LFB
# Retrieved 2025-12-06, License - CC BY-SA 3.0

import geocoder
g = geocoder.ip('me')
print(g.latlng)
