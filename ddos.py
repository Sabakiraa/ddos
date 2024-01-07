import requests
import threading

def istek_gonder(url, thread_sayisi):
    session = requests.Session()
    # Manuel olarak çerez ekleme
    session.cookies.set("cookie_name", "cookie_value")

    def istek_yap():
        response = session.get(url)
        print(f"Istek durumu: {response.status_code}")

    threads = []
    for _ in range(thread_sayisi):
        thread = threading.Thread(target=istek_yap)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    girilen_url = input("Istek göndermek istediğiniz web sitesinin URL'sini girin (örn. http://example.com:8080): ")
    girilen_thread_sayisi = int(input("Kaç thread kullanmak istersiniz? "))
    istek_gonder(girilen_url, girilen_thread_sayisi)
