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

## Task 3.2 Questions to investigate
1. What is the difference between 'append()' and 'insert()'?
    'append()' dodaje pozycję do listy na końcu listy, a 'insert()' na wybranej pozycji
2. What happens if you try to remove a value that is not on the list?
    Wyskoczy błąd z informacją o tym, że element nie znajduje się na liście
3. Can a list contain values of different types?
    Tak
4. What is the difference between tasks and seconr_list after the last step?
    Listy nie różnią się
5. Does 'sort()' return a new list, or does it change the original one?
    Zmienia ona oryginalną listę

## Task 4.1 Research
1. krotka = ("a", "b", "c")
2. krotka = ("a",)
3. print(krotka[0])
4. len(krotka)
5. Nie da się zmienić elementów krotki, ponieważ jest niemodalna
6. Nie da się dodać elementów do krotki, ponieważ jest niemodalna
7. x, y, z = krotka
8. list(krotka), tuple(lista)

## Taks 4.2 Questions to investigate
1. What makes a tuple immutable?
    Krotka jest niemutowalna, ponieważ jest to "lista" dla stałych wartości
2. Why would you choose a tuple instead of a list?
    Gdybym potrzebował przechować jakieś stałe wartości, których nie powinno się nadpisywać
3. Why does '(5,)' contain one element, while '(5)' does not?
    Ponieważ '(5,)' mówi o krotce, a zwykłe '(5)' mówi o jednej zmiennej i to jest tak samo jakbyśmy przypisali wartość '5' bez nawiasów
4. Can a tuple contain a list? If so, can you change that list?
    Krotka może posiadać w sobie listę i można ją modyfikować
5. What happens when you pass a tuple to a 'len()'?
    Wyświetla się liczba elementów krotki

## Task 5.1 Research
1. print(krotka[0])
2. print(krotka[2])
3. print(krotka[-1])
4. print(krotka[-2])
5. print(krotka[len(krotka) - 1])
6. Element się nie wyświetli, bo indeksowanie zaczyna się od 0, a długość się liczy od 1
7. a = 1; print(krotka[a])
8. tekst = "Python"; print(tekst[0]); Zwróci: "P"

## Task 5.2 Questions to investigate
1. Why does Python start counting at 0?
    Ponieważ komputer liczy odległości od początku danych od 0 i tak przyjęło się w językach programowania m. in. C, C++ i JS
2. What is the last valid index for a sequence with n elements?
    n - 1
3. What is the name of the error coused by an index that is too large?
    IndexError: tuple index out of range
4. What is the difference between 'colors[1]' and 'colors[-1]'?
    'colors[1]' to druga pozycja od początku krotki, a 'colors[-1]' to ostatnia
5. Can you use an expression such as 'i + 1' as an index?
    Tak
6. Does indexing work the same way for strings and tuples?
    Tak, w stringu kolejnymi indeksami są kolejne znaki 

## Task 6.1 Research
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
