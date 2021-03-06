from setuptools import setup


SETTINGS = dict(
  name = "pycret-santa",
  version = "0.5",
  description = "Package that will help you organizing a Secret Santa party!",
  keywords = ["secret", "santa", "christmas"],
  author = "Renaud Parent",
  author_email = "renaud.parent@gmail.com",
  url = "https://github.com/RenaudParent/pycret-santa",
  download_url = "https://github.com/RenaudParent/pycret-santa/tarball/0.5",
  packages = ["pycret_santa"],
  package_data = {"pycret_santa": ["*.yaml"]},
  install_requires = ["pyyaml"],
  tests_require = ["nose>=1.0", "mock", "mox"],
  test_suite = 'nose.collector',
  entry_points = {
    "console_scripts": [
      "secretsanta = pycret_santa.secret_santa:main",
    ],
  },
)

if __name__ == "__main__":
  setup(**SETTINGS)
