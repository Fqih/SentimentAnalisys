from google_play_scraper import reviews_all, Sort
import csv

scrapreview = reviews_all(
    'com.tokopedia.tkpd',  # ID aplikasi
    lang='id',            
    country='id',               
    sort=Sort.MOST_RELEVANT,   
    count=10100 
)

with open('ReviewTokopedia.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])  
    for i, review in enumerate(scrapreview):
        if i < 10100:
            writer.writerow([review['content']])
        else:
            break

print("Scrapping berhasil disimpan di ReviewTokopedia.csv")
