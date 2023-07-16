# UniScape
Convert a string to its unicode representation.

## Current State

- CLI app runs fine
- GUI app doesn't display window contents.
  Output during runtime is missing the following lines normally seen when launching the scripts directly:
  ```
  [...]
  [INFO   ] [Text        ] Provider: sdl2
  [INFO   ] [Clipboard   ] Provider: xclip
  [INFO   ] [CutBuffer   ] cut buffer support enabled
  [...]
  [INFO   ] [GL          ] NPOT texture support is available
  [...]
  ```
