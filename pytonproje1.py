

#https://app.patika.dev/courses/python-temel/proje
# input : [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]

def flatten_list(lisst):
    # Girdi olarak verilen listeyi düzleştirir.
    flat_list =[]
    for i in lisst:

        if isinstance(i,list) or  isinstance(i,tuple):
            #isinstance => i nin türü list ya da tuple mı 
            flat_list.extend(flatten_list(i))
            #extend => tek tek elemanları for ile listeye ekleme yerine
            # extend kullanarak hepsini bir liste içine ekleyebiliriz. 
        else:
            flat_list.append(i)
    return flat_list

deneme_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print('Transformed Flat List', flatten_list(deneme_list)) 


# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverse_list(lisst2):
    lisst2.reverse()
    # listeyi ters çevirir son elemanı başa alır ilk elemanı sona 
    for i in lisst2:
        if isinstance(i,list) or  isinstance(i,tuple):
            i.reverse()
            # listenin elemanlarını ters çevirir.
    
    return lisst2
        
b = reverse_list([[1, 2], [3, 4], [5, 6, 7]])   
