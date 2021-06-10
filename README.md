# Trivial economy game

This is a simple text-based economy game. Fun for maybe 15 minutes :)

# Story

My 10 year old nephew likes computer games (well, usually tablet games) and Catan.
Like any teenage kid, he wants to create his own computer games, and in this case I am the role-model programmer.

To guide kids to programming, there are things like [code.org](https://code.org/) and also some paid services out there.
These sites offer pretty graphics, exercises with themes from known games like Minecraft, and even inspiring interviews with the developers of said games.
Pretty good for what they are.

However, all of these games are essentially about moving some sprites on the screen via instructions. They are the same thing as those programmable robots, you can build from plastic bricks.
The kid picks the theme they like (in my nephew's case probably Minecraft), then solves 10 instruction-based/programming-like puzzles, and then there is nothing more to do...

So, let's get back to Catan... I wanted to know, how much programming skill is needed to write a simple economy game:
some game about building/growing things, and buying/selling them.
The idea is to help the kid write the game with 2 types of goods, and then let the kid add countless more things... probably involving feedback loops and exponential wealth :p

Thus I wrote this game. The rules are:
* Use a real programming language, no kids-only drag&drop "programming". I guess JavaScript and Python are suitable options, but I only really know Python.
* No functions.
* No loops except the main loop.
* I used a single class to make stuff less annoying for me, but it can be removed by copy&pasting more things.
* No graphics, only text, uhh... my nephew HATES drawing pictures, I may be able to sell it with that in mind :p

This is what I learned:
* A money-based economy with goods and prices pretty fast results in fractional money. I don't think it's viable to avoid float- and integer-divisions in this kind of game. It may be easier to just teach the kid to accept fractional numbers.
* Entering numbers and the following string->int conversion requires exception handling. I guess I would have to provide an "input_integer()" function and prepare some excuse to make the kid accept it as-it.

# Inspiration

While the story related to my nephew's favorite game Catan, this game is actually inspired by some other games:
* The 1988 DOS game "Armut Und Reichtum" ("povery and wealth") by Karl-Heinz Tisch.
* I believe this game was itself inspired by the 1984 Atari game "Kaiser".
