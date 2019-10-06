if __name__ == "__main__":
    import pkgutil
    import importlib

    motherpackage_name = "interactive_tests"
    motherpackage = __import__(motherpackage_name)

    for module_finder, module_name, is_pkg in pkgutil.walk_packages(
        path=motherpackage.__path__
    ):
        if not is_pkg:
            module = importlib.import_module(
                "." + module_name, package=motherpackage_name
            )
            module.main()
