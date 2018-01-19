"""
Example module using c extension.
"""
import platform_wheel_extension  # pylint: disable=E0401

def use_extension(some_float=1.234):
    """Use the extension"""
    return platform_wheel_extension.sqrtf(some_float)
