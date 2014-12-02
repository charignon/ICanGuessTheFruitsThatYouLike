##Purpose 
A quick hack around neural networks to study correlation between chemical composition and tastiness of fruits.

In other words, with this program you can state what fruit you like and dislike and this program guesses what other fruits you might like or not dislike like using a Neural Network.

I used this data: https://fr.wikipedia.org/wiki/Composition_nutritionnelle_des_fruits

- You should edit the fruit list to match what you like and don't like.
- The program takes a sample of the fruits to test the training.
- You can also modify the training parameter easily.

Example output (on a bad terminal that does not handle utf-8 -_-) :
```bash
['Amande s\xc3\xa8che', 'Abricot sucr\xc3\xa9 en conserve', 'Banane fra\xc3\xaeche', 'Banane s\xc3\xa9ch\xc3\xa9e', 'Cassis frais', 'Pistachefra\xc3\xaeche', 'Poire', 'Cerise en conserve', 'Grenadefra\xc3\xaeche', 'Orange']
Feed-forward neural network: 
inputs:    19 
hiddens:    2 
outputs:    1 
connections and biases:   43

Testing results for 10 testing cases:
OUTPUT 1 (node nr 22):
Targets vs. outputs:
   1      1.000000      0.818081
   2      0.000000      0.080944
   3      1.000000      1.111447
   4      1.000000      1.214286
   5      1.000000     -0.214286
   6      1.000000      0.818081
   7      1.000000      1.214285
   8      0.000000      0.268257
   9      0.000000      0.054516
  10      0.000000      0.056672
Regression line parameters:
slope         =  0.711885
intercept     =  0.115097
r-value       =  0.669524
p-value       =  0.034204
slope stderr  =  0.279232
estim. stderr =  0.432584
```
Here the interpretation is that all the predictions were right except one, number 5.
Based on what I told the program: I don't like fresh blackcurrant and it thinks I should like it based on what it learnt about me :)
I will make sure to try blackcurrant again, I might be mistaken!

## Setup on Mac OS

```bash
git clone git@github.com:charignon/ICanGuessTheFruitsThatYouLike.git
cd ICanGuessTheFruitsThatYouLike
Install homebrew http://brew.sh/
brew install gcc
sudo easy_install networkx
sudo easy_install ffnet
python main.py
```
