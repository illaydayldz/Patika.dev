# Patika.dev INSERTION SORT PROJECT


[22,27,16,2,18,6] => Insertion Sort

1)Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

2) Big-O gösterimini yazınız.

4) Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
5) Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.

6) [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort’a göre ilk 4 adımını yazınız.

INSTERTİON SORT AŞAMALARI
 
[22,27,16,2,18,6]
[2|,27,16,22,18,6]
[2,6|,1,6,22,18,27]
[2,6,16|,18,22,27]
** n , n-1,n-2,n-3 olarak gidiyor.

BIG-0 GÖSTERİMİ

worst Case => O(n²) = n+(n-1)+(n-2)…+1
Average Case => (n²)
Best Case => O(n)

TIME COMPLEXİTY
Worst Case => [27,22,18,16,6,2]
Best Case => [2,6,16,18,22,27]

18 SAYISI’NIN CASE DURUMU

Dizinin son hali [2,6,16,18,22,27]. 18 sayısı bu dizide ortanca deper olduğundan dolayı average case diyebiliriz.

[7,3,5,8,2,9,4,15,6] DİZİSİNİN INSERTION SORT’A GÖRE İLK 4 ADIMI

[2|,3,5,8,7,9,4,15,6]
[2,3|,5,8,7,9,4,15,6]
[2,3,4|,8,7,9,5,15,6]
[2,3,4,5|,7,9,8,15,6]
