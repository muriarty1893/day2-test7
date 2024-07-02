from elasticsearch import Elasticsearch
import io
##setup connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=('elastic', 'suVlWmYRKKFk6RYs_TrU'))
print(es.ping())

with io.open("C:\Users\Murat Eker\Desktop\tabel.txt","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
print(data)
"""data=data.split("\n")
for index in data:
    response=es.indices.create(index=index)
    print(response)"""