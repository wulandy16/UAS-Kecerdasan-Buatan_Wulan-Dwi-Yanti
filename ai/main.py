#mengimport library
import speech_recognition as srec 
from gtts import gTTS #library yang digunakan ,gTTS (google text to speech)
import os

#membuat variabel
def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
       #diberikan perintah print agar tau apakah python sudah mendengarkan atau belum
        print('Mendengarkan....')
        suara = mendengar.listen(source,phrase_time_limit=5)
        try: 
            #diberikan perintah print agar tau apakah python sudah menerima perintah dari suara kita atau belum
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')# disini ID digunakan untuk kode bahasa Indonesia 
            print(dengar)
        except: 
            pass
        return dengar
#function agar python bisa berbicara dengan bahasa Indonesia
def ngomong(self):
    teks = (self)
    bahasa = 'id'
    namafile = 'ngomong.mp3'
    def reading():
        suara = gTTS(text=teks, lang=bahasa, slow=False)
        suara.save(namafile)
        os.system(f'start {namafile}')
    reading()

def run_michelle():
    Layanan = perintah()
    #print(Layanan)
    ngomong(Layanan)

run_michelle()