cmake_minimum_required(VERSION 3.2)
project(nuklear)

set(OUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/bin CACHE STRING "Build output directory")
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(
  SOURCES
  ${SOURCE_DIR}/nuklear_buffer.c
  ${SOURCE_DIR}/nuklear_button.c
  ${SOURCE_DIR}/nuklear_chart.c
  ${SOURCE_DIR}/nuklear_color.c
  ${SOURCE_DIR}/nuklear_color_picker.c
  ${SOURCE_DIR}/nuklear_combo.c
  ${SOURCE_DIR}/nuklear_context.c
  ${SOURCE_DIR}/nuklear_contextual.c
  ${SOURCE_DIR}/nuklear_draw.c
  ${SOURCE_DIR}/nuklear_edit.c
  ${SOURCE_DIR}/nuklear_font.c
  ${SOURCE_DIR}/nuklear_group.c
  ${SOURCE_DIR}/nuklear_image.c
  ${SOURCE_DIR}/nuklear_input.c
  ${SOURCE_DIR}/nuklear_layout.c
  ${SOURCE_DIR}/nuklear_list_view.c
  ${SOURCE_DIR}/nuklear_math.c
  ${SOURCE_DIR}/nuklear_menu.c
  ${SOURCE_DIR}/nuklear_page_element.c
  ${SOURCE_DIR}/nuklear_panel.c
  ${SOURCE_DIR}/nuklear_pool.c
  ${SOURCE_DIR}/nuklear_popup.c
  ${SOURCE_DIR}/nuklear_progress.c
  ${SOURCE_DIR}/nuklear_property.c
  ${SOURCE_DIR}/nuklear_scrollbar.c
  ${SOURCE_DIR}/nuklear_selectable.c
  ${SOURCE_DIR}/nuklear_slider.c
  ${SOURCE_DIR}/nuklear_string.c
  ${SOURCE_DIR}/nuklear_style.c
  ${SOURCE_DIR}/nuklear_table.c
  ${SOURCE_DIR}/nuklear_text.c
  ${SOURCE_DIR}/nuklear_text_editor.c
  ${SOURCE_DIR}/nuklear_toggle.c
  ${SOURCE_DIR}/nuklear_tooltip.c
  ${SOURCE_DIR}/nuklear_tree.c
  ${SOURCE_DIR}/nuklear_utf8.c
  ${SOURCE_DIR}/nuklear_util.c
  ${SOURCE_DIR}/nuklear_vertex.c
  ${SOURCE_DIR}/nuklear_widget.c
  ${SOURCE_DIR}/nuklear_window.c
)
add_library(${PROJECT_NAME} ${SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC ${SOURCE_DIR})
set_target_properties(
  ${PROJECT_NAME} PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${OUT_DIR}
  ARCHIVE_OUTPUT_DIRECTORY ${OUT_DIR}
  RUNTIME_OUTPUT_DIRECTORY ${OUT_DIR}
  C_STANDARD 11
  C_STANDARD_REQUIRED TRUE
  C_EXTENSIONS OFF
)
install(
  TARGETS nuklear
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
)
install(
  FILES ${SOURCE_DIR}/nuklear.h
  DESTINATION include
)