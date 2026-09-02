from setuptools import setup
from setuptools.dist import Distribution

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        """Tag the wheel as platform-specific (so Windows and Linux builds
        get distinct filenames) but not tied to a specific CPython ABI/
        version, since the bundled library is loaded via ctypes at runtime
        rather than compiled as a Python extension module."""

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

        def get_tag(self):
            _python, _abi, plat = _bdist_wheel.get_tag(self)
            return "py3", "none", plat

    cmdclass = {"bdist_wheel": bdist_wheel}
except ImportError:
    cmdclass = {}


class BinaryDistribution(Distribution):
    """Bundles a platform-specific compiled library (mavs.dll/libmavs.so) via
    package-data rather than an extension module. Without this, setuptools
    tags the wheel "py3-none-any", so the Windows and Linux builds would
    produce identically-named wheel files."""

    def has_ext_modules(self):
        return True


setup(distclass=BinaryDistribution, cmdclass=cmdclass)
