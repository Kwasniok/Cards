# Dependencies
This project requires [Python 3.6](https://www.python.org/downloads) or greater.


# Installation
## Fast
```
git clone https://github.com/Kwasniok/Cards.git --recursive

```
or
```
git clone https://github.com/Kwasniok/Cards.git --branch <tag/branch> --recursive
```
for a specific [branch](https://github.com/Kwasniok/Cards/branches/all) or [tag](https://github.com/Kwasniok/Cards/tags).

*Note: Replace `<tag/branch>` with the name of the desired tag or branch (e.g. `v0.1`, `master`).*


## Slow
```
git clone https://github.com/Kwasniok/Cards.git
cd Cards
git checkout <tag/branch>
git submodule update --init
cd ..
```

*Note: `git checkout <tag/branch>` is optional.*


# Run
Call
```
cd Cards
python main.py
```
to run the script.

# Update
Pull via
```
cd Cards
git pull --recurse-submodule
```
to keep the project and its submodules in sync.

## Submodules
Update submodules via
```
git submodules update
```
which will update them according to your project's current version.

*Note: Do not use `git submodules update --remote` as it updates them to their latest version available which might be ahead or behind your current projects's version.*



# Tests
## Unit Tests
Run all unit tests via
```
cd Cards
python run_all_unittests.py
```

## Interactive Tests
Run all interactive tests sequentially via
```
cd Cards
python run_all_interactive_tests.py
```
or run a single interactive test via
```
cd Cards
python -m interactive_tests.<test>
```
where `<test>` might be the name of any [test modules](interactive_tests).
*Note: Remeber to strip the file extension `.py` like in `example_test.py` --> `example_test`.*

## Tested with
`Windows 10` and `Python 3.6.6`
