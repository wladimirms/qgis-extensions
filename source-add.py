"""
This script should be run from the Python consol inside QGIS.
It adds online sources to the QGIS Browser.
Each source should contain a list with the folowing items (string type):
[sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]
You can add or remove sources from the sources section of the code.
Script by Klas Karlsson
Sources from https://qms.nextgis.com/
Some services require you to supply your own API key for the services to work.
Licence GPL-3
Regarding the terms of use for these background maps YOU will need to verify that you
follow the individual EULA that comes with the different services,
Most likely they will restrict how you can use the data.
Example:
For Esri basemaps you will need a valid ArcGIS online subscription to use the maps.
"""


# Sources
sources = []
sources.append(["connections-xyz","Google Maps","","","","https://mt1.google.com/vt/lyrs=m&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D","","19","0"])
sources.append(["connections-xyz","Google Satellite", "", "", "", "https://mt1.google.com/vt/lyrs=s&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Terrain", "", "", "", "https://mt1.google.com/vt/lyrs=t&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Terrain Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=p&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Google Satellite Hybrid", "", "", "", "https://mt1.google.com/vt/lyrs=y&x=%7Bx%7D&y=%7By%7D&z=%7Bz%7D", "", "19", "0"])
sources.append(["connections-xyz","Stamen Terrain", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/terrain/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Toner", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/toner/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Toner Light", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/toner-lite/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Stamen Watercolor", "", "", "Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL", "http://tile.stamen.com/watercolor/%7Bz%7D/%7Bx%7D/%7By%7D.jpg", "", "18", "0"])
sources.append(["connections-xyz","Wikimedia Map", "", "", "OpenStreetMap contributors, under ODbL", "https://maps.wikimedia.org/osm-intl/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "1"])
sources.append(["connections-xyz","Wikimedia Hike Bike Map", "", "", "OpenStreetMap contributors, under ODbL", "http://tiles.wmflabs.org/hikebike/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "1"])
sources.append(["connections-xyz","Esri Boundaries Places", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","Esri Gray (dark)", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["connections-xyz","Esri Gray (light)", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "16", "0"])
sources.append(["connections-xyz","Esri National Geographic", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "12", "0"])
sources.append(["connections-xyz","Esri Ocean", "", "", "Requires ArcGIS Onlinesubscription", "https://services.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "10", "0"])
sources.append(["connections-xyz","Esri Satellite", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["connections-xyz","Esri Standard", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "17", "0"])
sources.append(["connections-xyz","Esri Terrain", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Terrain_Base/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "13", "0"])
sources.append(["connections-xyz","Esri Transportation", "", "", "Requires ArcGIS Onlinesubscription", "https://server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","Esri Topo World", "", "", "Requires ArcGIS Onlinesubscription", "http://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D", "", "20", "0"])
sources.append(["connections-xyz","OpenStreetMap Standard", "", "", "OpenStreetMap contributors, under ODbL", "http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap H.O.T.", "", "", "OpenStreetMap contributors, under ODbL", "http://tile.openstreetmap.fr/hot/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap Monochrome", "", "", "OpenStreetMap contributors, under ODbL", "http://tiles.wmflabs.org/bw-mapnik/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap TF Landscapes", "", "", "", "https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=539e6b26b9b144e68f9d6c9fa4c75d5e", "", "19", "0"])
sources.append(["connections-xyz","OpenStreetMap Node Density", "", "", "", "https://tyrasd.github.io/osm-node-density/2014/tiles/density/{z}/{x}/{y}.png", "", "19", "0"])
sources.append(["connections-xyz","OpenTopoMap", "", "", "Kartendaten: © OpenStreetMap-Mitwirkende, SRTM | Kartendarstellung: © OpenTopoMap (CC-BY-SA)", "https://tile.opentopomap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "17", "1"])
sources.append(["connections-xyz","OpenTopoMap Russia", "", "", "", "https://tile-a.opentopomap.ru/{z}/{x}/{y}.png", "", "19", "0"])
sources.append(["connections-xyz","Strava All", "", "", "OpenStreetMap contributors, under ODbL", "https://heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "15", "0"])
sources.append(["connections-xyz","Strava Run", "", "", "OpenStreetMap contributors, under ODbL", "https://heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19", "", "15", "0"])
sources.append(["connections-xyz","Open Weather Map Temperature", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/temp_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID={your_API_key}", "", "19", "0"])
sources.append(["connections-xyz","Open Weather Map Clouds", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/clouds_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID={your_API_key}", "", "19", "0"])
sources.append(["connections-xyz","Open Weather Map Wind Speed", "", "", "Map tiles by OpenWeatherMap, under CC BY-SA 4.0", "http://tile.openweathermap.org/map/wind_new/%7Bz%7D/%7Bx%7D/%7By%7D.png?APPID={your_API_key}", "", "19", "0"])
sources.append(["connections-xyz","CartoDb Dark Matter", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/dark_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","CartoDb Positron", "", "", "Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.", "http://basemaps.cartocdn.com/light_all/%7Bz%7D/%7Bx%7D/%7By%7D.png", "", "20", "0"])
sources.append(["connections-xyz","Bing VirtualEarth", "", "", "", "http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1", "", "19", "1"])
sources.append(["connections-xyz","Yandex Satellite", "", "", "", "https://core-sat.maps.yandex.net/tiles?l=sat&v=3.1025.0&x={x}&y={y}&z={z}&scale=1&lang=ru_RU", "", "19", "0"])
sources.append(["connections-xyz","Yandex Satellite renew", "", "", "", "https://core-sat.maps.yandex.net/tiles?l=sat&v=3.1016.0&x={x}&y={y}&z={z}&scale=1&lang=ru_RU", "", "19", "0"])
sources.append(["connections-xyz","Yandex Maps 4x", "", "", "", "https://core-renderer-tiles.maps.yandex.net/tiles?l=map&x={x}&y={y}&z={z}&scale=4&lang=ru_RU", "", "19", "1"])
sources.append(["connections-xyz","Mapbox Satellite", "", "", "", "https://{switch:a,b,c,d}.tiles.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}.jpg?access_token=pk.eyJ1Ijoib3BlbnN0cmVldG1hcCIsImEiOiJja2w5YWt5bnYwNjZmMnFwZjhtbHk1MnA1In0.eq2aumBK6JuRoIuBMm6Gew", "", "19", "0"])
sources.append(["connections-xyz","Mapbox Hybrid", "", "", "", "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA", "", "19", "0"])
sources.append(["connections-xyz","ЕЭКО ЦГКИПД", "", "", "", "https://ngw.fppd.cgkipd.ru/tile/56/{z}/{x}/{y}.png", "", "19", "0"])
sources.append(["connections-xyz","ЕЭКО Росреестр Basemap", "", "", "", "https://pkk.rosreestr.ru/arcgis/rest/services/BaseMaps/BaseMap/MapServer/tile/{z}/{y}/{x}", "", "19", "0"])
sources.append(["connections-xyz","ЕЭКО Росреестр Anno", "", "", "", "https://pkk.rosreestr.ru/arcgis/rest/services/BaseMaps/Anno/MapServer/tile/{z}/{y}/{x}", "", "19", "0"])
sources.append(["connections-xyz","Генштаб Топо", "", "", "", "http://maps.marshruty.ru/ml.ashx?al=1&i=1&x={x}&y={y}&z={z}", "", "19", "0"])
sources.append(["connections-xyz","Relief (cz)", "", "", "", "http://{switch:m1,m2,m3,m4}.mapserver.mapy.cz/turist-m/{z}-{x}-{y}", "", "19", "0"])
sources.append(["connections-xyz","ArcticDEM", "", "", "", "http://elevation2.arcgis.com/arcgis/services/Polar/ArcticDEM/ImageServer/WMSServer", "", "19", "0"])
sources.append(["connections-xyz","USGS Topographic", "", "", "", "http://caltopo.s3.amazonaws.com/topo/{z}/{x}/{y}.png", "", "16", "0"])
sources.append(["connections-xyz","ООПТ ААНИИ", "", "", "", "http://lgtgis.aari.ru/arcgis/services/MCPA/PAWMS_lite/MapServer/WMSServer", "", "19", "0"])
sources.append(["connections-xyz","Лесопокрытая площадь", "", "", "", "http://earthengine.google.org/static/hansen_2013/tree_alpha/{z}/{x}/{y}.png", "", "19", "0"])
sources.append(["connections-xyz","Autonavi Satellite (Chineese)", "", "", "", "https://webst01.is.autonavi.com/appmaptile?style=6&x={x}&y={y}&z={z}", "", "19", "0"])
sources.append(["connections-xyz","Landsat Mosaic 2019 Composite", "", "", "", "https://storage.googleapis.com/earthenginepartners-hansen/tiles/gfc_v1.7/last_543/{z}/{x}/{y}.jpg", "", "19", "0"])
sources.append(["connections-xyz","Here Hybrid", "", "", "", "http://1.aerial.maps.cit.api.here.com/maptile/2.1/maptile/newest/hybrid.day/{z}/{x}/{y}/256/png8?app_id=eAdkWGYRoc4RfxVo0Z4B&app_code=TrLJuXVK62IQk0vuXFzaig&lg=eng", "", "19", "0"])
sources.append(["connections-xyz","OpenRailwayMap", "", "", "", "https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png", "", "19", "0"])
sources.append(["connections-xyz","Разграфка топокарт 1:200К", "", "", "", "http://trolleway.nextgis.com/api/resource/1028/wms", "", "19", "0"])
sources.append(["connections-xyz","Сканэкс Космоснимки", "", "", "", "http://maps.kosmosnimki.ru/TileService.ashx?Request=gettile&LayerName=04C9E7CE82C34172910ACDBF8F1DF49A&apikey=U96GP973UH&crs=epsg:3857&z={z}&x={x}&y={y}", "", "19", "0"])
sources.append(["connections-xyz","USGS Tectonic Plates", "", "", "", "http://earthquake.usgs.gov/basemap/tiles/plates/{z}/{x}/{y}.png", "", "19", "0"])


# Add sources to browser
for source in sources:
   connectionType = source[0]
   connectionName = source[1]
   QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
   QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
   QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
   QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
   QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
   QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
   QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

# Update GUI
iface.reloadConnections()