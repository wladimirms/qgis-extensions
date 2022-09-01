# QGIS-extensions

Adding TMS XYZ tiles to your own QGIS 3.X project, installing useful QGIS plugins and installing ArcQMS extension to ArcMap 10.X

links:

```shell
<https://qms.nextgis.com/>
<https://qms.nextgis.com/about>
<https://portal.fppd.cgkipd.ru/main>
<https://rosreestr.gov.ru/activity/geodeziya-i-kartografiya/edinaya-elektronnaya-kartograficheskaya-osnova/>
<https://plugins.qgis.org/plugins/>

```

## How to add

### 1. Clone the project or download package from GitLab

```shell
git clone http://gitlab.tsnigri.ru/vmuravev/qgis-extensions
```

### 3. Copy and run plugins-add.py in QGIS 3.X python console to install QGIS3 useful extensions

### 4. Copy and run source-add.py in QGIS 3.X python console and install ArcQMSInstaller.msi

### 5. Open browser and choose XYZ Tiles service in QGIS and enable ArcQMS extension in Toolbars to get QMS services in your ArcMap environment

## Adding WMS/WMTS layers to QGIS project

Use WMS/WMTS to import connections in QGIS browser

Sources:

```shell
ИПД ЦНИГРИ - https://ugibtest.tsnigri.ru/geoserver/NET2/wms?

ГГК ВСЕГЕИ 1:1 000 000 - https://wms.vsegei.ru/VSEGEI_Bedrock_geology/wms?

ГГК ВСЕГЕИ 1:200 000 - https://wms.vsegei.ru/VSEGEI_Bedrock_geology2/wms?

ВСЕГЕИ ГГК Растры - http://wms.vsegei.ru/rasters/wms?

РФГФ - https://rfgf.ru/exploration-map/wms

МГС ВНИИгеосистем - http://ows.mgs.geosys.ru/topo/eqdc100?version=1.3.0

EOX Sentinel - http://a.tiles.maps.eox.at/wms

OneGeology World CGMW 1:50M Geological Units Onshore - http://mapsref.brgm.fr/wxs/1GG/CGMW_Bedrock_and_Structural_Geology

OneGeology World CGMW Imaging - http://mapsref.brgm.fr/wxs/1GG/monde1GG

```

## Adding WFS/OGC API Features to QGIS project

Use WFS/OGC API Features to import connections in QGIS browser

Sources:

```shell
ИПД ЦНИГРИ - http://kastor.tsnigri.ru:8585/geoserver/wfs

USGS Major mineral deposits of the world - https://mrdata.usgs.gov/services/wfs/ofr20051294

OneGeology - http://mapsref.brgm.fr/wxs/1GG/CGMW_Bedrock_and_Structural_Geology

OneGeology ARCTIC GTK 1:1M Mineral Resources - http://13.95.69.121:80/geoserver/erl/ows
```

## Adding ArcGIS REST services to QGIS project

Use ArcGIS REST servers to import connections in QGIS browser

Sources:

```shell
SGM Музей Вернадского - http://83.149.241.4/arcgis/rest/services/Public

ААНИИ POLAR - http://lgtgis.aari.ru/arcgis/rest/services/AARI/polar/MapServer

ESRI ArcGIS Online Imagery - https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer

Росреестр ЕЭКО BaseMap - https://pkk.rosreestr.ru/arcgis/rest/services/BaseMaps/BaseMap/MapServer

Росреестр ЕЭКО Anno - https://pkk.rosreestr.ru/arcgis/rest/services/BaseMaps/Anno/MapServer

ВСЕГЕИ Deposits - http://agssrv1.vsegei.ru/arcgis/rest/services/WEB_P3/WEB_P3_2L/MapServer

ВСЕГЕИ ArcGIS REST - http://agssrv1.vsegei.ru/arcgis/rest/services/

ЯНАО ArcGIS REST - https://karta.yanao.ru/arcgisserver/rest/services

ХМАО ArcGIS REST - http://pubweb.admhmao.ru:6080/arcgis/rest/services

ГИС МЕТЕО-ДВ - http://www.meteo-dv.ru/arcgis/rest/services

DATAPLUS - https://projectserver.dataplus.ru/arcgis105/rest/services

```

## Adding Vector Tiles services to QGIS project

Use Vector Tiles service to import connections in QGIS browser

Sources:

```shell
OpenInfraMap Roads and ways - https://openinframap.org/tiles/{z}/{x}/{y}.pbf

Роcреестр кадастровое деление - https://pkk.rosreestr.ru/arcgis/rest/services/Hosted/caddivsion/VectorTileServer/tile/{z}/{y}/{x}.pbf

```
