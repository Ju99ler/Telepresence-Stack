# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_tp_cmd_sub_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED tp_cmd_sub_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(tp_cmd_sub_FOUND FALSE)
  elseif(NOT tp_cmd_sub_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(tp_cmd_sub_FOUND FALSE)
  endif()
  return()
endif()
set(_tp_cmd_sub_CONFIG_INCLUDED TRUE)

# output package information
if(NOT tp_cmd_sub_FIND_QUIETLY)
  message(STATUS "Found tp_cmd_sub: 0.0.0 (${tp_cmd_sub_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'tp_cmd_sub' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${tp_cmd_sub_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(tp_cmd_sub_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${tp_cmd_sub_DIR}/${_extra}")
endforeach()
