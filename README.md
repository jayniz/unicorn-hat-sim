# Unicorn HAT (HD) simulator

Simulates an Unicorn HAT HD (and should work for the 8x8 HAT and the 8x4 PHAT as well) using pygame.

## Usage

If you want your code to run on your computer as well as your Pi, you could do something like this:

1. `pip install unicorn-hat-sim` (or `pip2` or `pip3` depending on your setup)
1. Adjust your `import unicornhathd` statement as follows:

```python
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
```

You can choose from `import unicornhathd` (16x16), `import unicornhat` (8x8) and `import unicornphat` (8x4). 

## Demo

(Note that this gif has a low framerate, the simulator runs nice and smooth in real life)

![Demo](https://cl.ly/2s070z1k0L3J/Screen%20Recording%202017-06-26%20at%2011.12%20PM.gif)

## TODO

- [ ] find a python person who shows me how this would be done properly
- [ ] fix/check rotation
- [ ] add a proper LED glow effect so it looks more like a real unicorn HAT
- [ ] publish via pip
