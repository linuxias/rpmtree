import setuptools

setuptools.setup(
    name='rpmtree',
    version='0.1',
    description="The information and dependability relationships for RPM or ELF files are structured and displayed in a tree form.",
    author="Seungha Son",
    author_email="linuxias@gmail.com",
    license="GNU 3.0+",
    url="https://github.com/linuxias/rpmtree",
    packages=setuptools.find_packages(),
    keywords=["rpm", "tree", "elf", "elftree"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
)
