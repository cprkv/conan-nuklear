# Conan nuklear package

## Installation

Add remote to get ckristen packages from bintray:  
`conan remote add ckristen https://api.bintray.com/conan/ckristen/conan`

Add dependency to your project in conanfile:  
`nuklear/2.0.0@ckristen/master`

## Options

You can define options (`True` or `False`) in your conanfile (has value on build process):
```
NK_INCLUDE_FIXED_TYPES           (default: True)
NK_INCLUDE_DEFAULT_ALLOCATOR     (default: True)
NK_INCLUDE_STANDARD_IO           (default: True)
NK_INCLUDE_STANDARD_VARARGS      (default: True)
NK_INCLUDE_VERTEX_BUFFER_OUTPUT  (default: True)
NK_INCLUDE_FONT_BAKING           (default: True)
NK_INCLUDE_DEFAULT_FONT          (default: True)
NK_INCLUDE_COMMAND_USERDATA      (default: False)
NK_BUTTON_TRIGGER_ON_RELEASE     (default: False)
NK_ZERO_COMMAND_MEMORY           (default: False)
NK_UINT_DRAW_INDEX               (default: False)
NK_KEYSTATE_BASED_INPUT          (default: False)
```

Description of options you could find on [official documentation page](https://rawgit.com/vurtun/nuklear/master/doc/nuklear.html#nuklear/usage/flags).

## Additional info

Original authors of nuklear library offers header only library.
I decided to make static library because header library brings unnecessary compilcated define-like interface.
With my package all needed defines come to library through conan Options (see above) and you shouldn't define it yourself.


## ToDo

- Tests on Windows, MacOS