Recipes of code in reStructuredText
======================================

This is a template with some pieces of code/text in rst_ directives.

.. _rst: https://docutils.sourceforge.io/rst.html
.. _UDL: https://www.udl.cat/

Using links
-----------------
The text below contains links that look like "(quickref__)".  These
are relative links that point to the `Quick reStructuredText`_ user
reference.  If these links don't work, please refer to the `master
quick reference`_ document.

__
.. _Quick reStructuredText: quickref.html
.. _master quick reference:
   https://docutils.sourceforge.io/docs/user/rst/quickref.html

.. _AK_ACQS - Azure Kinect Acquisition System: https://github.com/GRAP-UdL-AT/ak_acquisition_system
.. _AK_SM_RECORDER - Azure Kinect Standalone Mode: https://github.com/GRAP-UdL-AT/ak_sm_recorder
.. _AK_FRAEX - Azure Kinect Frame Extractor: https://github.com/GRAP-UdL-AT/ak_frame_extractor


Using simple text
-------------------
This is a text in bold **Write the docs**.

This is italic text *Write the docs*.


Tables
----------

.. list-table::
   :widths: 20 50
   :header-rows: 1

   * - Package
     - Description
   * - `AK_ACQS - Azure Kinect Acquisition System`_
     - AK_ACQS is a software solution for data acquisition in fruit orchards using a sensor system boarded on a terrestrial vehicle. It allows the coordination of computers and sensors through the sending of remote commands via a GUI. At the same time, it adds an abstraction layer on library stack of each sensor, facilitating its integration. This software solution is supported by a local area network (LAN), which connects computers and sensors from different manufacturers ( cameras of different technologies, GNSS receiver) for in-field fruit yield testing.
   * - `AK_SM_RECORDER - Azure Kinect Standalone Mode`_
     - A simple GUI recorder based on Python to manage Azure Kinect camera devices in a standalone mode. ( https://pypi.org/project/ak-sm-recorder/ )
   * - `AK_FRAEX - Azure Kinect Frame Extractor`_
     - AK_FRAEX is a desktop tool created for post-processing tasks after field acquisition. It enables the extraction of information from videos recorded in MKV format with the Azure Kinect camera. Through a GUI, the user can configure initial parameters to extract frames and automatically create the necessary metadata for a set of images. ( https://pypi.org/project/ak-frame-extractor/ )







.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - First Name
     - Last Name
     - Residence
   * - Elizabeth
     - Bennett
     - Longbourne
   * - Fitzwilliam
     - Darcy
     - Pemberley


.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====



.. table:: Truth table for "not"
   :widths: auto

   ======================================  =========
    COLUMN 01                              COLUMN 02
   ======================================  =========
    A value here                           Single row here.
    .. math:: e^{i\pi} + 1 = 0             Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
   ======================================  =========


Math symbols
--------------

Defining an equation after this line.

.. math:: e^{i\pi} + 1 = 0
   :label: euler

Euler's identity, equation :math:numref:`euler`, was elected one of the
most beautiful mathematical formulas.



Managing images
-----------------
This is the name of an image IMG_20180617_123230.jpg
An image.

.. image:: recipes_restructuredtext_img/IMG_20180617_123230.jpg
  :width: 400
  :align: center
  :alt: Alternative text

A figure with caption.

.. figure:: recipes_restructuredtext_img/IMG_20180617_123230.jpg
  :alt: Alternative text for figure
  :width: 400
  :align: center

  This is the caption


Managing code blocks
--------------------

Python code ahead.

.. code:: python

  def my_function():
      "just a test"
      print 8/2


Bash code ahead.

.. code-block:: bash

    #!/bin/bash
    echo "---- SCRIPT INFORMATION ---";
    MY_VARIABLE=1;
    echo "Enter value ->; read $MY_VARIABLE;
    echo "Some text here -> "$MY_VARIABLE;


Calling MATLAB code.

.. code-block:: matlab

    IRGBPath=fullfile(datasetImagesPath, imageName);
    IMaskPath=fullfile(datasetMasksPath, imageMaskName);
    IRGB=imread(IRGBPath);
    IMask=imread(IMaskPath);
    DepthChannel=transformed_depth;  % get channel from transformed depth matrix

