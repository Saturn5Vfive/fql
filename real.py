import fql


f = fql.connect("database.fql")
f.setvalue("hello", "world")
f.save()