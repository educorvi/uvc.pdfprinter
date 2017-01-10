======================
uvc pdf printer
======================

UVC PDF Printer

Contents
========

.. contents::

Install
=======
- Add the following to the eggs of the zeoserver_base section of your base.cfg:

::
    
    [zeoserver_base]
    
    eggs =
        ...
        eea.pdf
        eea.converter
        eea.downloads
        plone.app.async

- Add the following environment variables to the zeoserver_base section of your base.cfg: 

::
    
    [zeoserver_base]
    
    environment-vars =
        ...
        WKHTMLTOPDF_PATH ${wkhtmltopdf:location}/wkhtmltopdf
        EEADOWNLOADS_NAME ${buildout:media-downloads-name}
        EEADOWNLOADS_PATH ${buildout:media-downloads-path}
        EEACONVERTER_TEMP ${buildout:media-downloads-temp}

- Add the following sections to your base.cfg:

::

    [media-downloads]
    recipe = ore.recipe.fs:mkdir
    path = ${buildout:media-downloads-path}
    mode = 0700
    createpath = true

    [media-downloads-temp]
    recipe = ore.recipe.fs:mkdir
    path = ${buildout:media-downloads-temp}
    mode = 0700
    createpath = true

    [wkhtmltopdf]
    recipe = hexagonit.recipe.download
    url = http://eggrepo.apps.eea.europa.eu/pypi/wkhtmltopdf/wkhtmltopdf-0.12.1.tgz

- Add the following parts to the buildout section of your buildout.cfg:

::

    [buildout]

    parts = 
    	...
    	client3
    	media-downloads
    	media-downloads-temp
    	wkhtmltopdf

- Add the following variables to the buildout section of your buildout.cfg:

::

    [buildout]
    media-downloads-name = downloads
    media-downloads-path = ${buildout:directory}/var/downloads/pdf
    media-downloads-temp = ${buildout:directory}/var/downloads/tmp

- On the client1 section of your buildout add the following to your zcml:

::

    [client1]
    
    zcml =
    	...
    	plone.app.async-single_db_instance

- On the client2 section of your buildout add the following:

::

    [client2]
  
    zcml =
    	...
    	plone.app.async-single_db_instance

- Add the client3 section to your buildout:

::

    [client3]
    <= client_base
    recipe = plone.recipe.zope2instance
    zeo-address = ${zeoserver:zeo-address}
    http-address = 9082
    zcml =
    	${buildout:zcml}
      	plone.app.async-single_db_worker

- Install the following packages on your server machine:

========================  ========================  ===============================
Debian/Ubuntu             CentOS 7                  dependency for
========================  ========================  ===============================
libjpeg-dev               libjpeg-turbo-devel       Pillow
libjpeg62                 libjpeg-turbo             wkhtmltopdf	
libpng12-0                libpng12                  wkhtmltopdf
libjpef62-dev             libjpef62-dev             wkhtmltopdf
========================  ========================  ===============================

- Add uvc.pdfprinter to your eggs section in your buildout and re-run buildout.

  You can download a sample buildout from
  https://github.com/educorvi/uvc.pdfprinter/tree/master/buildouts/plone4

- Install uvc.pdfprinter within Site Setup > Add-ons
