kondycja(marek).
kondycja(adam).
kondycja(jan).
biega(marek).
biega(jan).
plywa(adam).
plywa(jan).


sportowiec(X):-biega(X);plywa(X).
zawody(X):-sportowiec(X),kondycja(X).
pilkarz(X):-biega(X),kondycja(X).
plywak(X):-plywa(X),kondycja(X).

zawody(X)
pilkarz(X),plywak(X)
kondycja(X)