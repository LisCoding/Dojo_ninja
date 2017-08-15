In [70]: for ninja in Dojo.objects.last().ninjas.all():
    ...:     print(ninja.first_name, ninja.last_name, ninja.id)
    ...:
(u'Jhonx', u'Pozo', 7)
(u'Ali', u'Pozo', 8)
(u'Tami', u'Pozo', 9)

In [71]: for ninja in Dojo.objects.last().ninjas.all():
    ...:     print(ninja.first_name, ninja.last_name, ninja.id.dojo)
    ...:

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-71-ca986f1fedc7> in <module>()
      1 for ninja in Dojo.objects.last().ninjas.all():
----> 2     print(ninja.first_name, ninja.last_name, ninja.id.dojo)
      3
      4
      5

AttributeError: 'int' object has no attribute 'dojo'

In [72]: for ninja in Dojo.objects.last().ninjas.all():
    ...:     print(ninja.first_name, ninja.last_name, ninja.dojo)
    ...:
    ...:
    ...:
    ...:
    ...:
(u'Jhonx', u'Pozo', <Dojo: Dojo object>)
(u'Ali', u'Pozo', <Dojo: Dojo object>)
(u'Tami', u'Pozo', <Dojo: Dojo object>)

In [73]: for ninja in Dojo.objects.last().ninjas.all():
    ...:     print(ninja.first_name, ninja.last_name, ninja.dojo.id)
.:
    ...:
(u'Jhonx', u'Pozo', 6)
(u'Ali', u'Pozo', 6)
(u'Tami', u'Pozo', 6)

In [74]: for ninja in Dojo.objects.get(id=5).ninjas.all():
    ...:     print(ninja.first_name, ninja.last_name, ninja.dojo.id)

    ...:
(u'MArix', u'Sergo', 5)
(u'Grantx', u'tevi', 5)
(u'Maicpx', u'Orego', 5)

In [75]: for ninja in Dojo.objects.get(id=5).ninjas.first():
    ...:     print(ninja.first_name, ninja.last_name, ninja.dojo.id)
    ...:
    ...:
    ...:
    ...:
    ...:
    ...:
    ...:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-75-049ffbeec769> in <module>()
----> 1 for ninja in Dojo.objects.get(id=5).ninjas.first():
      2     print(ninja.first_name, ninja.last_name, ninja.dojo.id)
      3
      4
      5

TypeError: 'Ninja' object is not iterable

In [76]:  Dojo.objects.get(id=5).ninjas.first():
    ...:     print(ninja.first_name, ninja.last_name, ninja.dojo.id)
    ...:
    ...:
    ...:
    ...:
    ...:
    ...:
    ...:
  File "<ipython-input-76-6bb5b572d7b5>", line 1
    Dojo.objects.get(id=5).ninjas.first():
                                         ^
SyntaxError: invalid syntax


In [77]: c =  Dojo.objects.get(id=5).ninjas.first()
    ...: c.id
    ...: c.name
    ...: c.first_name
#joining tables and getting specific values:

In [79]: d =  Dojo.objects.get(id=5).ninjas.first()

In [80]: d.id
Out[80]: 4

In [81]: d.dojo
Out[81]: <Dojo: Dojo object>

In [82]: d.dojo.id
Out[82]: 5

In [83]: d.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-83-3930d96f0cd0> in <module>()
----> 1 d.name

AttributeError: 'Ninja' object has no attribute 'name'

In [84]: d.dojo.name
Out[84]: u'CodingDojo Seattle'

In [85]: d.dojo.city
Out[85]: u'Seattle'

In [86]:
Update tables:
SyntaxError: invalid syntax
(djangoEnv) ~/Desktop/django/dojo_ninjas/mai$ python manage.py makemigrations
You are trying to add a non-nullable field 'desc' to dojo without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: Quit
Please select a valid option: 2
(djangoEnv) ~/Desktop/django/dojo_ninjas/mai$ python manage.py makemigrations
Migrations for 'ninja_dojo_app':
  apps/ninja_dojo_app/migrations/0002_auto_20170815_2247.py:
    - Add field desc to dojo
    - Alter field state on dojo
(djangoEnv) ~/Desktop/django/dojo_ninjas/mai$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, ninja_dojo_app, sessions
Running migrations:
  Rendering model states... DONE
  Applying ninja_dojo_app.0002_auto_20170815_2247... OK
(djangoEnv) ~/Desktop/django/dojo_ninjas/mai$ 
