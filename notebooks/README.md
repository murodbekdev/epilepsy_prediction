# X1 to X16 ustunlar

###### Bu bizda miyyaning turli joylaridan olingan elektrod kanallaridir.

> Masalan:

| 84 | 117 | 120 |
| -- | --- | --- |
| 4  | 7   | 18  |
| 84 | 117 | 120 |


Oddiy qilib aytganda:

* EEG apparati odamning boshiga bir nechta elektrodlar qo'yadi.
* Har bir elektrod miyaning ma'lum bir qismidagi elektr faollikni o'lchaydi.
* Har bir elektroddan kelgan signal datasetda alohida ustun sifatida saqlanadi.

| X1   | X2   | X3   | ... | X16 | y |
| ---- | ---- | ---- | --- | --- | - |
| -131 | -140 | -125 | ... | -20 | 0 |




Bu yerda:

* **X1** → 1-elektrod signali
* **X2** → 2-elektrod signali
* ...
* **X16** → 16-elektrod signali
* **y** → klass (0,1,2,3)


### EEGdagi "kanal" nima?

EEGda kanal deganda ikki nuqta orasidagi elektr farqi tushuniladi.

Electrode A --------\ 
                      > EEG channel
Electrode B --------/

X1:

 50 |        /\ 
 20 |   /\  /  \
  0 |__/  \/    \__
-20 |
-50 |
      time →
      Bu vaqt bo'yicha miyaning elektr faolligi.