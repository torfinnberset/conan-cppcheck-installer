import os

from conans import ConanFile, CMake, tools
from six import StringIO


class CppcheckinstallerTestConan(ConanFile):
    def build(self):
        pass
    
    def test(self):
        output = StringIO()
        cppcheck_path = os.path.join(self.deps_cpp_info["cppcheck_installer"].rootpath, "bin", "cppcheck")
        self.run("{} --version".format(cppcheck_path), output=output, run_environment=True)
        self.output.info("Installed: %s" % str(output.getvalue()))
        ver = str(self.requires["cppcheck_installer"].ref.version)

        value = str(output.getvalue())
        cppcheck_version = value.split('\n')[0]
        self.output.info("Expected value: {}".format(ver))
        self.output.info("Detected value: {}".format(cppcheck_version))
        assert (ver in cppcheck_version)

   