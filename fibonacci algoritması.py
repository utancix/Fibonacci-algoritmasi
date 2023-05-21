sayi = input("Bir sayı giriniz.")
sayi = int(sayi) #Girişi tam sayıya dönüştür.

def fibonacci(sayi): 
   if  sayi ==1:
    return 0         #return komutu bir fonksiyonun işleyişini sonlandırarak fonksiyonun çağrıldığı yere bir değer döndürmek için kullanılır.
   if  sayi == 2:
    return 1
   if  sayi > 2:
    return fibonacci(sayi-1) + fibonacci(sayi-2)

if sayi <= 0:
    print("Fibonacci algoritmasında negatif veya sıfır sayısı yoktur.")
else:   #"else" yerine "if" yazılırsa "if sayi > 0:" şeklinde yazılmalı. Burada else yazarak yukarıda tanımlanan koşulu içermeyen sayılar denildi.
    print("fibonacci sayısı", fibonacci (sayi))