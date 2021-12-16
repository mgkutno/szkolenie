
Podstawy
Markdown

# H1 
## H2

GIT

git init - inicjalizacja pustego repo

Po utworzeniu polecenia
(git remote add origin <adres>)
(git config --global user.email "email")
(git config --global user.name "name")
(git config --list)

Najczestsze polecenia
git status
git add <nazwa pliku>
git commit -m "message" # tworzenie rewizji
git push origin master  # wysyla zmiany do zdalnego repo

git branch  # sprawdza galaz


git pull origin master  # sciaga zmiany ze zdalnego repo

git clone <adres>

Podstawowe typy
int - liczby całkowite

1
2

10000
100_000_000  # separator pomocniczy

100000000

int()

0

int("100")

100

type("100")

str

type(int("100"))

int

int(2.7)

2

int("2.7")

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
C:\Users\SZB345~1\AppData\Local\Temp/ipykernel_4196/4095753669.py in <module>
----> 1 int("2.7")

ValueError: invalid literal for int() with base 10: '2.7'

float - liczby zmiennoprzecinkowe

float

float(1)

1.0

0.1 + 0.1 + 0.1 == 0.3

False

Operatory

+ dodawanie
- odejmowanie
* mnożenie
/ dzielenie
// dzielenie calkowite
% modulo - reszta z dzielenia
** operator potegowania

10 / 3

3.3333333333333335

10 // 3

3

10 % 3

1

3 ** 2

9

9 ** 0.5

3.0

Zadanie

W sesji interaktywnego środowiska interpretera oblicz następujące wartości:

    pole trójkąta o podstawie 10 i wysokości 5
    pole koła o promieniu 7
    pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5
    objętość kuli o promieniu 7/8

0.5 * 10 * 5

25.0

import math

math.pi * 7 ** 2

153.93804002589985

(3 + 9) * 6.5 / 2

39.0

(4 * math.pi * (7/8) ** 3) / 3

2.806162187972133

Zasady PEP8

https://www.python.org/dev/peps/pep-0008/

flake8

black
bool

False/True

False

False

True

True

Operatory porównania

==
!=
<
<=
>
>=

inne operatory, które zwrócą wartość True/ False, to

in
is

1 * 2 == 6 / 3

True

1 * 2 == 3 / 2

False

Operatory logiczne

and - koniunkcja
or - alternatywa
not - negacja

False or True

True

False and True

False

not False

True

1 * 2 == 3 / 2 or 3 > 2

True

1 * 2 == 3 / 2 and 3 > 2

False

1 == 1.0

True

1 == "1"

False

1 == True

True

1 + True

2

1 is True

<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
<>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
C:\Users\SZB345~1\AppData\Local\Temp/ipykernel_11844/3482963539.py:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
  1 is True

False

id(1)

3035582890224

id(True)

140725254495080

int(False)

0

float(False)

0.0

56.0 ** 10

3.033054890961142e+17

123

123

0b101011

43

0xfff

4095

0o777

511

help(int)

Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

int('222', base=3)

26

complex

complex()

0j

1 + 3j + 2 + 4j

(3+7j)

str - napis

 

"to jest napis"

'to jest napis'

'to jest napis'

'to jest napis'

"to 'jest' napis"

"to 'jest' napis"

'to "jest" napis'

'to "jest" napis'

"to \"jest\" napis"

'to "jest" napis'

"to "jest" napis"

  File "C:\Users\SZB345~1\AppData\Local\Temp/ipykernel_11844/739905611.py", line 1
    "to "jest" napis"
         ^
SyntaxError: invalid syntax

"napis" + "napis1"

'napisnapis1'

'linia 1\n' + 'linia 2' 

'linia 1\nlinia 2'

print('linia 1\n' + 'linia 2')

linia 1
linia 2

'''
linia1
linia2
'''

'\nlinia1\nlinia2\n'

"""
linia1
linia2
"""

'\nlinia1\nlinia2\n'

Zmienne

Typowanie dynamiczne ( w odróżnieniu od statycznego)

a = 1  # komentarz
a = 2.3 # komentowanie blokow ctrl + /
a = "a"

"""
To czasem tez jest uwazane za komentarz
"""

a: str = "New"

mypy - http://mypy-lang.org/

nazwy zmiennych piszemy malymi literami moga to byc litery cyfry i znak podkreslenia

Dobre nazwy
nazwa_zmiennej
_nazwa_zmiennej
ser_1


zle nazwy:

bledy:
1nazwa
nazwa.1

zla praktyka:
nazwaZmiennej
NazwaZmiennej

zmienna = "napis"
x = zmienna

x == zmienna

True

x is zmienna

True

id(x)

3035680511792

id(zmienna)

3035680511792

zmienna2 = "napis dluższy"
x = zmienna2

zmienna2 == x

True

zmienna2 is x

True

zmienna3 = "napis"
id(zmienna3)

3035680511792

zmienna4 = "napis dluższy"

zmienna2 == zmienna4

True

zmienna2 is zmienna4

False

id(zmienna2)

3035681112560

id(zmienna4)

3035681113120

a = 1
b = 1

a is b

True

a = 10000001
b = 10000001

a is b

False

Funkcja print

help(print)

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

print()

print(1, 2, 3, 4)

1 2 3 4

print(1, 2, "3", 4)

1 2 3 4

print(str(1))

1

print(10)
print(20)

10
20

print(10, end="-")
print(20)

10-20

print(1, 2, 3, 4, sep=":")

1:2:3:4

print(end="-", 1)  # kolejnosc ma znaczenie

  File "C:\Users\SZB345~1\AppData\Local\Temp/ipykernel_11844/1238163101.py", line 1
    print(end="-", 1)
                    ^
SyntaxError: positional argument follows keyword argument

input

x = input()

10

x

'10'

input("Wciśnij jakiś klawisz")

Wciśnij jakiś klawisz

''

# x to napis
# typowanie silne - python nie robi za nas konwersji
x + 1

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
C:\Users\SZB345~1\AppData\Local\Temp/ipykernel_11844/1824700092.py in <module>
      1 # x to napis
      2 
----> 3 x + 1

TypeError: can only concatenate str (not "int") to str

int(x) + 1

11

x + str(1)

'101'

help(input)

Help on method raw_input in module ipykernel.kernelbase:

raw_input(prompt='') method of ipykernel.ipkernel.IPythonKernel instance
    Forward raw_input to frontends
    
    Raises
    ------
    StdinNotImplementedError if active frontend doesn't support stdin.

Zadanie 01

Korzystając z przypisywania wartości do zmiennych napisz program obliczający pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5.
Zadanie 02

Napisz program wyliczający kwotę należną za zakupiony towar na podstawie ceny za kilogram oraz liczby zakupionych kilogramów. Do przechowywania informacji o cenie oraz liczbie kilogramów użyj zmiennych. Wypisz wszystkie informacj na konsolę. Przykładowy komunikat programu:

Cena za kg: 10.0  (# print)
Waga: 2.5         (# input)
Należność: 25.0

nazwa_1 = "Cheddarxxxxxxx"
cena_1 = 12.5

nazwa_2 = "Gouda"
cena_2 = 9.23

template = "Ser: {:^50} - cena {:6.2f}"

print(template.format(nazwa_1, cena_1))
print(template.format(nazwa_2, cena_2))

Ser:                   Cheddarxxxxxxx                   - cena  12.50
Ser:                       Gouda                        - cena   9.23

t1 =  f"Ser: {nazwa_1:^50} - cena {cena_1:6.2f}"

t1

'Ser:                   Cheddarxxxxxxx                   - cena  12.50'

"Ser %s %.2f" % (nazwa_1, cena_1)

'Ser Cheddarxxxxxxx:10 12.50'

Zadanie 03

Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej przez użytkownika liczby kilometrów, ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości. Przykładowe komunikat programu:

 Miasto A: Warszawa
 Miasto B: Gdańsk
 Dystans Warszawa‐Gdańsk: 420
 Cena paliwa: 4.55
 Spalanie na 100 km: 5.5
 Koszt przejazdu Warszawa‐Gdańsk to 105 PLN

Wyrażenie warunkowe

    najprostsze uzycie

    if warunek:

    <blok kodu>

    else

if warunek:
   <blok kodu>
else:
   <blok kodu>

x = 12

if x > 10: 
    print("Większy niż 10")
    print(x)
else:
    print("else")
    if x % 2 == 0:
        print("parzysty")
    
print("Cos tam dalej sie dzieje")

Większy niż 10
12
Cos tam dalej sie dzieje

x = 12

if x > 10: 
    print("Większy niż 10")
    print(x)
elif x % 2 == 0:
    print("Parzysty")
elif x % 3 == 0:
    print("podzielne przez 3")
else:
    print("else")

    
print("Cos tam dalej sie dzieje")

Większy niż 10
12
Cos tam dalej sie dzieje

x = 12

if x > 10: 
    print("Większy niż 10")
    print(x)
    
if x % 2 == 0:
    print("Parzysty")


if x % 3 == 0:
    print("podzielne przez 3")
else:
    print("else")

    
print("Cos tam dalej sie dzieje")

Większy niż 10
12
Parzysty
podzielne przez 3
Cos tam dalej sie dzieje

1 > 0 or 1 / 0

True

1 < 0 and 1 / 0

False

Zadanie 04

Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia. Przykładowy komunikat programu:

Podaj rok urodzenia: 1980
Jesteś pełnoletni!

Podaj rok urodzenia: 2012
Nie jeste pełnoletni!

import datetime

t = datetime.datetime.now()

t

datetime.datetime(2021, 12, 15, 12, 52, 11, 527911)

dir(t)

['__add__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__radd__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rsub__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 'astimezone',
 'combine',
 'ctime',
 'date',
 'day',
 'dst',
 'fold',
 'fromisocalendar',
 'fromisoformat',
 'fromordinal',
 'fromtimestamp',
 'hour',
 'isocalendar',
 'isoformat',
 'isoweekday',
 'max',
 'microsecond',
 'min',
 'minute',
 'month',
 'now',
 'replace',
 'resolution',
 'second',
 'strftime',
 'strptime',
 'time',
 'timestamp',
 'timetuple',
 'timetz',
 'today',
 'toordinal',
 'tzinfo',
 'tzname',
 'utcfromtimestamp',
 'utcnow',
 'utcoffset',
 'utctimetuple',
 'weekday',
 'year']

t.weekday()

2

Zadanie 05

Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100 wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...) lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi. Przykładowy komunikat programu:

 Podaj pozycję gracza X: 95
 Podaj pozycję gracza Y: 95
 Gracz znajduje się w prawym górnym rogu.

image.png

x = 2

5 < x < 15

False

pętla while

while <warunek>:
    <blok kodu>


while <warunek>:
    <blok kodu>
else:
    <blok kodu>

x = 10

while x > 0:
    print(x)
    x = x - 1 # x -= 1

10
9
8
7
6
5
4
3
2
1

x = 10

while x > 0:
    if x % 2 != 0:
        x -= 1
        continue
    print(x)
    x -= 1
else:
    print("Pętla skończona")

10
8
6
4
2
Pętla skończona

x = 10

while x > 0:
    if x == 4:
        break
    print(x)
    x -= 1
else:
    print("Pętla skończona skończona bez użycua break")

10
9
8
7
6
5

suma = 0
while True:
    polecenie = input("Podaj liczbe lub k by zakonczyc")
    if polecenie == "k": break
    suma += int(polecenie)

print(suma)
    
        

Podaj liczbe lub k by zakonczyc1
Podaj liczbe lub k by zakonczyc2
Podaj liczbe lub k by zakonczyc3
Podaj liczbe lub k by zakonczyc4
Podaj liczbe lub k by zakonczyc5
Podaj liczbe lub k by zakonczyc6
Podaj liczbe lub k by zakonczyck
21

Zadanie 06

Napisz program obliczający kwadrat 100 pierwszych liczba całkowitych i wypisujący wyniki na konsolę.
Zadanie 07

Napisz program obliczający średnią wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.
Zadanie 08

Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika. Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą. Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.
Zadanie 09 (opcjonalnie)

Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10. Użytkownik może wprowadzać komendy zmieniające położenie postaci. Po każdym ruchu użytkownik powinien otrzymywać informację o tym czy zmierza dobrym kierunku. Wyjcie poza planszę oznacza koniec gry. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.

Dodatkowo: po wykonaniu większej liczby kroków niż minimalna wartość x 2, umieść skarb w nowym miejscu z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku

import random 

los = random.randint(1, 5)

 


