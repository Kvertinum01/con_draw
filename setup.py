from setuptools import setup

version = "0.1.1"

setup(
    name="con_draw",
    author="Kvertinum01",
    url="https://github.com/Kvertinum01/con_draw",
    description="Framework for drawing in console",
    version=version,
    packages=["con_draw"],
    install_requires=[
        "Pillow"
    ],
    classifiers=[
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
    python_requires='>=3.7',
)
