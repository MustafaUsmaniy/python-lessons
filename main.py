# 01:02 - dars 
# KIRISH. VS Codeni Pythonga настроить. Ekranga ma'lumot chiqarish
# print("Hello World!")

# 03 - dars
# ARIFMETIK AMALLAR. SINTAKSIS.
# Matnni bir nechta qatorga chiqarish uchun ("""...""") yoki(\n)

# 04-dars O'zgaruvchilar
# O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
#     O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
#     O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
#     O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki   chiziq (_) qatnashishi mumkin
#     O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
#     O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)

# 05-dars
# MATNLAR BILAN ISHLASH
# f - string usuli
# ism = 'Ahad'
# familiya = 'Qayum'

# print(f"{ism} {familiya}")

# Maxsus belgilar
# \t - bo'sh joy tashash
# \n - qator tashash

# Strgin Metodlari
# .upper() - matnni yuqori(bosh) harfda chiqaradi
# .lower() - matnni pastki(kichik) harfda chiqaradi 
# .title() - matnni boshliq harfda chiqaradi
# Misol Uchun
# ims = 'AHAD'
# fams = 'QAYUM'

# ism_sharif = f"{ims} {fams}"

# print(ism_sharif.title())

# .capitalize() - matnni birinchi harfini katta qilib beradi
# Misol Uchun
# a = 'ahad'  
# b = 'qayum'

# c = f"{a} {b}"

# print(c.capitalize())

# lstrip() - matnning chap tomonidagi ortiqcha bo'sh joylarni olib tashsh
# rstrip() - matnning o'ng tomonidagi ortiqcha bo'sh joylarni olib tashsh
# strip() - matnning chap tomonidan va o'ng tomonidan ortiqcha bo'sh joylarni olib tashsh

#Foydalanuvchidan ma'lumot qabul qilish
# name = input("Ismingizni kiriting: ")
# print(f"Ismingiz: {name}")

# 06 - dars
# SONLAR BILAN ISHLASH
# int() - kiritilgan matnni int tipiga almashtiradi 
# float() - kiritilgan matnni float tipiga almashtiradi
# str() - kiritilgan matnni string tipiga almashtiradi
# bool() - kiritilgan matnni bool tipiga almashtiradi
# // - sonni butun qiymatini chiqaradi

# 07 - dars
# LISTLAR(RO'YHATLAR)
# [] - ro'yhatlar mana shu belgi belgi yordamida yaratiladi 
# Ro'yhat metodlari
# .append() - ro'yhat oxiriga element qo'shadi
# .insert() - ro'yhatni istalgan yeriga element qo'shadi. Misol: ro'yhat_nomi.insert(index raqam, "Yangi element nomi")
# .remove() - ro'yhatdan elementni olib tashadi
# a = ['olma', 'anor', 'behi', 'shaftoli']
# a.remove('anor')
# print(a)
# .del() - ro'yhatdan elementni o'chirib tashlaydi
# .pop() - ro'yhatdan elementni sug'urib olish

# 08 - dars
# Listlar uchun metodlar(Davomi)
# .sort() - ro'yhatni alifbo tartibida tartiblaydi
# a = ['olma', 'anor', 'behi', 'shaftoli', 'apple']
# a.sort()
# print(a)

# .reverse() - ro'yhatni teskari tartibda chiqarib beradi
# a = ['olma', 'anor', 'behi', 'shaftoli', 'apple']
# a.reverse()
# print(a)
# .sort(reverse=True) - ro'yhatni alifboga teskari tartibda chiqarib beradi 
# a = ['olma', 'anor', 'behi', 'shaftoli', 'apple']
# a.sort(reverse=True)
# print(a)

# .sorted() - ro'yhatga tegmagan holda ro'yhta ichidagi elementlarni alifbo tartibida chiqaradi
# Misol:
# sonlar = [15, 25, 22, 33, 12, 8, 10, 1, 5, 2, -5, -8]
# print(sorted(sonlar))

# .len() - ro'yhat uzunligini chiqaradi
# .range() - ma'lum bir oralig'dagi sonlarni chiqaradi
# Misol:
# print(list(range(0, 11)))

# QADAM
# Misol:
# print(list(range(1, 20, 2)))

# MAX, MIN VA SUM FUNKSIYALARI
# Misol:
# Maximum 
# sonlar = [15, 25, 22, 33, 12, 8, 10, 1, 5, 2, -5, -8]

# print(max(sonlar))

# Minimum
# sonlar = [15, 25, 22, 33, 12, 8, 10, 1, 5, 2, -5, -8]

# print(min(sonlar))

# Summa
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(sonlar))

# RO'YHATNI KESISH
# Ro'yhatni biror bir oralig'ini kesib olish uchun uning indeksidan(tartib raqamidan) foydalaniladi. Misol:
# a = ['olma', 'anor', 'behi', 'shaftoli', 'apple']
# print(a[0:3])
# print(a[:3]) - bu ro'yhat boshidan 3 indeksgacha olib beradi
# print(a[1:]) - bu 1 indeksdan ro'yhat ohirigacha olib beradi

# RO'YHATDAN NUSXA OLISH
# .append() - ro'yhat oxiriga element qo'shadi
# Ro'yhatdan nusxa olish: Misol:

# cars = ['bmw', 'audi', 'toyota', 'subaru', 'nissan']

# my_cars = cars[:] - bu yerda my_cars cars degan ro'yhatdan nusxa olib beradi

# TUPLES - o'zgarmas ro'yhatlar
# O'zgarmas ro'yhatlar () ichida yaratilinadi va unga o'zgartit=rish kiritib bo'lmaydi.
# Misol:
# toys = ('ball', 'doll', 'car', 'truck', 'train')
# print(toys)



# 09 - dars
# FOR LOOP
# Misol:
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# sonlar = list(range(1, 11))

# print(sonlar)

# 10 - dars
# IF...ELSE 
# Operators:
    # and - va operatori
    # or - yoki operatori
    # == - tengmi operatori
    # != - teng emasmi operatori
    # < - kichich operatori
    # > - katta operatori
    # <= - kichich yoki teng operatori
    # >= - katta yoki teng operatori
# Misol:
# a = 10
# if a == 10:
#     print("A 10ga teng bo'ldi")
# else:
#     print("A 10ga teng bo'lmadi")
# Misol:
# yosh = int(input("Yoshini kiriting: "))
# if 2022-yosh > 18:
#     print("Kirishingiz mumkin!")
# else:
#     print("Afususki kirishingiz mumkin emas :(")