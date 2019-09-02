from conans import ConanFile, CMake, tools
import os


class CppcheckinstallerConan(ConanFile):
    name = "cppcheck_installer"
    version = "1.89"
    license = "GPL 3.0"
    author = "Torfinn Berset <torfinn@bloomlife.com>"
    url = "https://github.com/torfinnberset/conan-cppcheck-installer"
    description = "Cppcheck is a static code analysis tool for the C and C++ programming languages"
    topics = ("static analyzer", "lint", "code quality", "tool")
    settings = "os_build", "arch_build"

    def source(self):
        tools.get(F"https://github.com/danmar/cppcheck/archive/{self.version}.tar.gz")              
        
    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=F"cppcheck-{self.version}", defs={"CMAKE_INSTALL_PREFIX": self.package_folder})
        cmake.install()

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
