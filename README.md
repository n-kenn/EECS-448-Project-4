# EECS-448-Project-4

A worms clone written in pygame.

Runs with python 2.7 and pygame 1.9.3

To play, clone the repository and run the wizards script using

<code>python wizards.py</code>

To run the test suite, you need to have pytest.
How to install pytest:

<code>pip install pytest </code>

Make sure your pip is for python 2.7. You can also follow the instructions here: [https://docs.pytest.org/en/latest/getting-started.html](https://docs.pytest.org/en/latest/getting-started.html)


### List of Known Bugs

- Some collisions can get players stuck in the ground.
- It is possible to kill yourself and the remaining team after they have won. This crashes the game.
- Animations can get stuck if the player fires fast enough, and while moving fast enough in a certain direction.
- Any mouse button can be used to fire a projectile. While not harmful in any way to the codebase, this is an unintended side effect of the verbage used in the code.

Authors:

Josh Oertel

oertelj@yahoo.com

Tom Brooks

t090b057@ku.edu

Noah Kenn

nkenn@ku.edu
