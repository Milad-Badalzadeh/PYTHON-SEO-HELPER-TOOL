import csv
from datetime import date
from client import RestClient

with open("Desktop/words.txt") as file:
    lines = [line.rstrip() for line in file]

today = date.today()


header = ['WORD', 'YEAR', 'MONTH', 'VOLUME', 'AVR_IN_YEAR']

f = open(f'Desktop/KEYWORD_VOLUME {today}.csv', 'a+')

writer = csv.writer(f)

writer.writerow(header)

client = RestClient("texyxy@lyft.live", "6c9fc6b7af0b037b")
post_data = dict()
post_data[len(post_data)] = dict(
    date_from="2020-01-01",
    keywords=lines
)
response = client.post("/v3/keywords_data/google_ads/search_volume/live", post_data)

if response["status_code"] == 20000:
    pass
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

v = response.get('tasks')
h = v[0].get('result')

try:
    for evrywrd in range(len(h)):
        kwrd = (h[evrywrd].get('keyword'))
#        print(f"THE AVRAGE SEARCH VOLUME FOR THE WORD {kwrd} IS {h[evrywrd].get('search_volume')}")
        w = h[evrywrd].get('monthly_searches')
        for dateon in w:
#            print(f"\nTHE VOLUME OF SEARCHES FOR THE WORD {kwrd} IN THE MONTH {dateon.get('month')} OF THE YEAR {dateon.get('year')} IS {dateon.get('search_volume')}\n")
            rrow = [kwrd, dateon.get('year'), dateon.get('month'), dateon.get('search_volume'), h[evrywrd].get('search_volume')]
            writer.writerow(rrow)

except:
    print(f"Err 4002 : \n\"{v[0].get('status_message')}\" \nthis message is deliverd by the API .")

f.close()
print("Done , Thanks for Using ME")