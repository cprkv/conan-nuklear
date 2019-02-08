#include <stdio.h>
#include <nuklear.h>

#if  !defined(NK_INCLUDE_FIXED_TYPES) \
  || !defined(NK_INCLUDE_DEFAULT_ALLOCATOR) \
  || !defined(NK_INCLUDE_STANDARD_IO) \
  || !defined(NK_INCLUDE_STANDARD_VARARGS) \
  || !defined(NK_INCLUDE_VERTEX_BUFFER_OUTPUT) \
  || !defined(NK_INCLUDE_FONT_BAKING) \
  || !defined(NK_INCLUDE_DEFAULT_FONT)
void error_flags_should_be_defined_by_default();
#endif

int main()
{
  return 0;
}