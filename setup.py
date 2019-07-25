from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    # Extension("AmazonApi",  ["AmazonApi.py"]),
    # Extension("centroidtracker",  ["centroidtracker.py"]),
    # Extension("resize_as",  ["resize_as.py"]),
    Extension("text_detection_video",  ["text_detection_video.py"]),
    # Extension("trackableobject",  ["trackableobject.py"]),
#   ... all your modules that need be compiled ...
]
setup(
    name = 'Text recognition after detection',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)