kobieta(katarzyna).
kobieta(zofia).
kobieta(anna).
kobieta(maria).
kobieta(wanda).
kobieta(ewa).

mezczyzna(robert).
mezczyzna(wojciech).
mezczyzna(jan).
mezczyzna(krzysztof).
mezczyzna(franciszek).
mezczyzna(bogdan).

malzenstwo(wojciech,zofia).
malzenstwo(jan,maria).
malzenstwo(bogdan,anna).

rodzic(wojciech,katarzyna).
rodzic(zofia,katarzyna).
rodzic(wojciech,robert).
rodzic(zofia,robert).
rodzic(jan,krzysztof).
rodzic(maria,krzysztof).
rodzic(jan,wojciech).
rodzic(maria,wojciech).
rodzic(franciszek,maria).
rodzic(bogdan,zofia).
rodzic(anna,zofia).
rodzic(bogdan,ewa).
rodzic(anna,ewa).
rodzic(wanda,bogdan).

matka(X,Y):-kobieta(X),rodzic(X,Y).
ojciec(X,Y):-mezczyzna(X),rodzic(X,Y).
siostra(X,Y):-kobieta(X),rodzic(Z,X),rodzic(Z,Y).
brat(X,Y):-mezczyzna(X),rodzic(Z,X),rodzic(Z,Y).
babcia(X,Y):-kobieta(X),rodzic(X,Z),rodzic(Z,Y).
dziadek(X,Y):-mezczyzna(X),rodzic(X,Z),rodzic(Z,Y).
syn(X,Y):-mezczyzna(X),rodzic(Y,X).
corka(X,Y):-kobieta(X),rodzic(Y,X).

przodek(X,Y):-rodzic(X,Y).
przodek(X,Y):-rodzic(X,Z),przodek(Z,Y).
potomek(X,Y):-rodzic(Y,X).
potomek(X,Y):-rodzic(Y,Z),przodek(Z,X).

ma_dziecko(X):-rodzic(X,_).
jest_dziadkiem(X):-rodzic(X,Z),rodzic(Z,_).

rodzenstwo(X,Y):-rodzic(Z,X),rodzic(Z,Y).