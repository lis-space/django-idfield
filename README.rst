Installation
============

Install it with pip (or easy_install)::

    pip install django-idfield

Usage
=====

You can use IDField for primary keys or to generate SMS/Email codes::

    from idfield import IDField
    
    class MyModel(models.Model):
        id = IDField(max_length=10, readable=False, primary_key=True, editable=False) # lzfgxcm3u4, etc
        code = IDField(max_length=4, readable=True) # GKUP, etc

Notes
=====

* IDField is not a completely unique ID. The larger value of ``max_length`` makes less collisions possible.
* IDField always generate a value, if value is not set.
* If ``readable=True``, value will be generated from caps letters and numbers, which do not look alike.
