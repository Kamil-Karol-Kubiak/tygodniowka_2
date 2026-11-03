# Task 1.2
    Pamiętam ze spotkania

## Task 1.3 Questions to investigate:
1. What exaactly is lost in 'int(fraction)'?
    Traci się część liczby po przecinku, ponieważ 'int()' skraca liczbę do postaci liczby całkowitej (bez zaokrąglania)
2. Why does 'int(text\_decimal)' fail while 'float(text\_decimal)' works?
    Ponieważ 'int()' potrzebuje w stringu liczby całkowitej do poprawnego działania, a tu dostał liczbę zmiennoprzecinkową
3. What is the diffetence between 'str(whole)' and 'whole'?
    'str(whole)' interpretuje 'whole' jako tekst, natomiast 'whole' jako liczbę
4. Whie is 'bool("0")' True, even though 'bool(0)' is False?
    Ponieważ "0" jest tekstem, a tekst w 'bool()' przyjmuje wartość True
5. Does a covnersion change the original variable, or return new value?
    Nie zmienia oryginalnej wartości, chociaż, że napiszemy np. 'wartosc = str(wartosc)'
6. Which conversions are reversible and which are not?
    odwracalne - z int na float, ze str na float lub int i odwrotnie
    nieodwracalne - z float na int, z czegokolwiek na bool (chociaż, że np. int był równy 0 lub 1), 
7. What does 'round()' do differently from 'int()'?
    'round()' zaokrągla liczbę do najbliższej liczby całkowitej, czyli do .4(9) w dół, a od .5 w górę, natomiast 'int()' usuwa wszystko po przecinku
8. What happens when you convert a string containing spaces, such as " 42 "?
    Program ignoruje spacje

## Task 2.1 Research 
#pamiętam z lekcji dlatego bez linków
1. Możemy skorzystać z %
2. print używa spacji do oddzielania
3. cos = raz dwa trzy; print("Coś tam %s" % cos)
4. liczba = 123; print("Liczba: %d" % liczba)
5. print("Liczba: %d, coś tam: %s" % (liczba, cos))
6. Działa jak 'int()'
7. Dizałą jak 'str()'
8. Trzeba użyć dwóch znaków procent, print("%liczba%%" % liczba)
9. %.2f - float, a liczba po kropce oznacza ilośc cyfr po przecinku
10. Wyświetla się error z odpowiednim opisem

## Task 2.2 Questions to investigate
1. What is the difference between %s and %d?
    %s interpretuje wartość jako tekst, a %d jako liczbę całkowitą
2. What does %d do with the value 12.5?
    Działa jak int() i usuwa wszystko po przecinku
3. Who adds the space in 'print("Name:", name)?
    Spacja dodaje się automatycznie jako oddzielenie między zmiennymi
4. When is % dormatting clearer than several print()?
    Gdy mamy zmienne, które mogą się zmienić i jest ich dużo
5. How do you print literal % character?
    Trzeba użyć dwóch % -> %%
6. What happens when a template cantains two placeholders but only one value?
    Wyświetla się error z odpowiednim opisem

## Task 3.1 Research
1. 'list = ["x", "y", "z"]'
2. print(list)
3. len(list)
4. list.append("a")
5. list.insert(1, "b")
6. 'list.remove("z")'
7. ostatni = lista.pop(); print(ostatni)
8. print(lista.count("a"))
9. lista.sort(); print(lista)
