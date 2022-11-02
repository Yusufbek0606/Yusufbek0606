
from deep_translator import GoogleTranslator

#text=str(input("Matinni kiriting:"))
#translated = GoogleTranslator(source='en', target='uz').translate(text=text)

#print(translated)

#import wikipedia
#wikipedia.set_lang("en")
#translated = GoogleTranslator(source='en',target='uz').translate(text=str(input("Matinni kiriting:")))

#text=str(input("Matinni kiriting:"))
#txt = wikipedia.summary(text)

#print(txt,translated)


from deep_translator  import GoogleTranslator 
import wikipedia
lang = "ru"
to_lang = "uz"
print("Tilni tanglang : \n1. O'zbekcha \n2.Ruscha\n3.Ingilizcha\n")
lang_number = int(input())
lang = "auto"
if lang_number == 1:
    lang = 'uz'
    print("Siz Uzbek tilini tanladiz")
elif lang_number == 2:
    lang = "ru"
    print("Siz Rus tilini tanladiz")
elif lang_number == 3:
    lang = "en"
    print("Siz Ingliz tilini tanladiz")
else:
    print("Siz tanglagan til raqami mavjud emas !!!")
    exit(0)
wikipedia.set_lang(lang)  # tilni o'rnatish
text = str(input("Matnni kiritng : "))
txt = wikipedia.summary(text)
print(txt)
print("="*30)
translated = GoogleTranslator(source=lang, target=to_lang).translate(text=txt)
print(translated)
print("*"*30)

fo = open("tarjima.txt", "w", encoding='UTF-8')
fo.write(txt)
fo.close()
    

fo = open("tarjima.txt", "r", encoding='utf-8')
natija = fo.read()
fo.close()

print(natija)