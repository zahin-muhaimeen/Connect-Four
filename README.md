# Connect-Four

**Version 1.1.0**

Connect Four python project.

---

## What's New

1. Magic Numbers removed. Replaced with the 
   appropriate constants, such as `BOARD_WIDTH`,
   `BOARD_HEIGHT`, `WINNING_LENGTH`
2. Reformated the code. Removed `reset_check_list()`
   function as I can replicate it with one line.
3. Remade the `choosing()` function so it now has
   boundaries so that the game won't crash. (Keep in
   mind that you have to enter from `0-6`, not `1-7`
   anymore.
4. Made `get_int()` function to make sure that the
   user is providing a numeric str instead of some
   random text.

---

## License & Copyright

This project is unlicensed and open source
