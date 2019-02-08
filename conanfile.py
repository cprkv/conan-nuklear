import os
from conans import ConanFile, CMake, tools


class ConanPackage(ConanFile):
  name = "nuklear"
  version = "1.0.0"
  license = "MIT License"
  url = "https://github.com/veyroter/conan-nuklear"
  description = "conan nuklear package"
  homepage = "https://github.com/vurtun/nuklear"
  settings = "os", "compiler", "build_type", "arch"
  generators = "cmake"
  exports_sources = "nuklear-master%s*" % os.sep
  default_on_features = [
      "NK_INCLUDE_FIXED_TYPES",
      "NK_INCLUDE_DEFAULT_ALLOCATOR",
      "NK_INCLUDE_STANDARD_IO",
      "NK_INCLUDE_STANDARD_VARARGS",
      "NK_INCLUDE_VERTEX_BUFFER_OUTPUT",
      "NK_INCLUDE_FONT_BAKING",
      "NK_INCLUDE_DEFAULT_FONT",
  ]
  default_off_features = [
      "NK_INCLUDE_COMMAND_USERDATA",
      "NK_BUTTON_TRIGGER_ON_RELEASE",
      "NK_ZERO_COMMAND_MEMORY",
      "NK_UINT_DRAW_INDEX",
      "NK_KEYSTATE_BASED_INPUT",
  ]
  options = {feature: [True, False]
             for feature in default_on_features + default_off_features}
  default_options = ['%s=True' % feature for feature in default_on_features]
  default_options += ['%s=False' % feature for feature in default_off_features]
  default_options = tuple(default_options)

  def configure(self):
    pass

  def build(self):
    print("self.dir_bld(): %s" % self.dir_bld())
    print("self.dir_src(): %s" % self.dir_src())

    incstr = "/* added by conan package options */"
    defstr = ""
    for feature in self.default_on_features + self.default_off_features:
      if getattr(self.options, feature):
        defstr += "%s #define %s 1\n" % (incstr, feature)
        if feature == "NK_INCLUDE_STANDARD_VARARGS":
          defstr += "%s #include <stdarg.h>\n" % incstr

    print("total flags: \n%s" % defstr)
    tools.replace_in_file(
        "%s%ssrc%snuklear.h" % (self.dir_src(), os.sep, os.sep),
        "#define NK_NUKLEAR_H_",
        "#define NK_NUKLEAR_H_\n\n%s\n\n" % defstr
    )

    cmake = CMake(self)
    tools.mkdir(self.dir_bld())
    cmake.configure(source_folder=self.dir_src(),
                    cache_build_folder=self.dir_bld())
    cmake.build(build_dir=self.dir_bld())

  def package(self):
    cmake = CMake(self)
    cmake.configure(source_folder=self.dir_src(),
                    cache_build_folder=self.dir_bld())
    cmake.install()

  def package_info(self):
    self.cpp_info.libs = tools.collect_libs(self)

  def dir_src(self):
    try:
      return self.src_full_path
    except:
      self.src_full_path = "%s%snuklear-master" % (self.source_folder, os.sep)
      return self.src_full_path

  def dir_bld(self):
    try:
      return self.build_full_path
    except:
      self.build_full_path = "%s%sbuild" % (self.dir_src(), os.sep)
      return self.build_full_path
