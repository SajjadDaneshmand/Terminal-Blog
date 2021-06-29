import get_push
import connectin


conn = connectin.db_connection()
cursor = conn.cursor()
# get_push.insert_category('sport')
# get_push.insert_category('art')
# get_push.insert_category('programming')
for i in cursor.execute('select * from post'):
    print(i)

conn.close()