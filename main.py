from jd_scraper_hospital import*
from jd_scraper_police import *
from city_calc import *
from video_recorder import *

cityy = city()
print(cityy)

contact_hospital(cityy)
contact_police(cityy)

# start_AVrecording()
# time.sleep(60)
# stop_AVrecording()
# file_manager()