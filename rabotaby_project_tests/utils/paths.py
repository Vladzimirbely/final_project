def abs_path_from_project(relative_path: str):
    import rabotaby_project_tests
    from pathlib import Path

    return (
        Path(rabotaby_project_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
