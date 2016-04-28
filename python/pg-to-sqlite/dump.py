import sys
import psycopg2
import sqlite3


# sqlite ref:
# http://zetcode.com/db/sqlitepythontutorial/
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

sqliteConnection = sqlite3.connect("olai.db")
sqliteCursor = sqliteConnection.cursor()
# ref: http://hakanu.net/sql/2015/08/25/sqlite-unicode-string-problem/
sqliteConnection.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')

try:
  pgConnectString = "host='localhost' dbname='jjude' user='jjude' password=''"
  pgConnection=psycopg2.connect(pgConnectString)
except:
  print "can't connect to pg. check if your db is running"
  sys.exit(1)


pgCursor = pgConnection.cursor()
try:
  pgCursor.execute("select entry.id, title, subtitle, slug, tags, excerpt, content_md, publish_at, is_post, site.alias from entry, site where entry.site_id = site.id")
except:
  print "I can't SELECT from entry"

rows = pgCursor.fetchall()

for row in rows:
    sqliteCursor.execute("INSERT INTO ENTRY (id, title, subtitle, slug, tags, excerpt, content_md, publish_at, is_post, site) \
                          VALUES (:id, :title, :subtitle, :slug, :tags, :excerpt, :content, :publish_at, :is_post, :site)", \
                          {"id": row[0], "title": row[1], "subtitle": row[2], "slug": row[3], "tags": row[4], \
                          "excerpt": row[5], "content": row[6], "publish_at": row[7], "is_post": row[8], "site": row[9]})
    sqliteConnection.commit()

sqliteConnection.close()
pgConnection.close()