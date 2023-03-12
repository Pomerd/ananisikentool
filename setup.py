from distutils.core import setup

setup(
    name="Panel Sikici",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.6",
    description="Düşük bant genişliğine sahip DoS aracı. Python'da Slowloris yeniden yazma.",
    author="Pomerd",
    url="https://discord.gg/axid",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
