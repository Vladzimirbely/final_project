def abs_path_from_project(relative_path: str):
    import final_project
    from pathlib import Path

    return (
        Path(final_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
