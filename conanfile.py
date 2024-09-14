from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout


class SimpleAmqpClientConan(ConanFile):
    name = "simpleamqpclient"
    version = "2.5.1"
    license = "Your License"
    author = "Your Name <your.email@example.com>"
    url = "https://github.com/your/repo"
    description = "A simple AMQP client library"
    topics = ("amqp", "rabbitmq", "messaging")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    exports_sources = "src/*", "include/*", "CMakeLists.txt", "libSimpleAmqpClient.pc.in"

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["SimpleAmqpClient"]


# import os
# import shutil
# from conan import ConanFile
# from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps
# from conan.tools.files import copy


# class SimpleAmqpClientConan(ConanFile):
#     name = "simpleamqpclient"
#     version = "2.5.1"
#     license = "MIT"
#     url = "https://github.com/alanxz/SimpleAmqpClient"
#     description = "SimpleAmqpClient is an easy-to-use C++ wrapper around the rabbitmq-c C library."
#     settings = "os", "compiler", "build_type", "arch"

#     options = {"shared": [True, False], "fPIC": [True, False]}
#     default_options = {"shared": True, "fPIC": True}
#     exports_sources = "CMakeLists.txt", "src/*", "cmake/*", "libSimpleAmqpClient.pc.in"

#     requires = [
#         "rabbitmq-c/0.14.0@magic/stable",
#         "boost/1.85.0",
#     ]

#     # def requirements(self):
#     #     """
#     #     Define additional requirements with overrides if necessary.
#     #     """
#     #     pass

#     # def imports(self):
#     #     """
#     #     Handle the import of files from dependencies.
#     #     """
#     #     self.copy("*", dst="bin", src="bin")
#     #     self.copy("*", dst="lib", src="lib")
#     #     self.copy("*", dst="include", src="src/SimpleAmqpClient")

#     def config_options(self):
#         if self.settings.os == "Windows":
#             del self.options.fPIC

#     def configure(self):
#         if self.options.shared:
#             del self.options.fPIC

#     def generate(self):
#         """
#         Generate the necessary build files.
#         """
#         tc = CMakeToolchain(self)
#         tc.generate()
#         deps = CMakeDeps(self)
#         deps.generate()

#     def build(self):
#         """
#         Build the project using CMake.
#         """
#         cmake = CMake(self)

#         # Build shared library
#         cmake.configure(variables={"BUILD_SHARED_LIBS": "ON"})
#         cmake.build()
#         cmake.install()

#         # Clean up build directory
#         cmake.configure(variables={"BUILD_SHARED_LIBS": "OFF"})
#         cmake.build()
#         cmake.install()

#     # def package(self):
#     #     """
#     #     Package the built artifacts.
#     #     """
#     #     cmake = CMake(self)
#     #     cmake.install()

#     def package(self):
#         include_dir = os.path.join(self.package_folder, "include")
#         lib_dir = os.path.join(self.package_folder, "lib")
#         bin_dir = os.path.join(self.package_folder, "bin")

#         # Copy include files
#         shutil.copytree("include", include_dir, dirs_exist_ok=True)

#         # Copy library files
#         # print(f"build_folder = {self.build_folder}")
#         for root, _, files in os.walk(self.build_folder):
#             for file in files:
#                 if file.endswith((".lib", ".dll", ".so", ".dylib", ".a")):
#                     shutil.copy(os.path.join(root, file), lib_dir)

#     def package_info(self):
#         """
#         Provide package information.
#         """
#         self.cpp_info.libs = ["SimpleAmqpClient"]
