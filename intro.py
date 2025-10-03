# # Welcome to your Jupyter Book


def foo():
    """Some function.

    .. pyvista-plot::

        >>> import pyvista as pv
        >>> mesh = pv.Sphere()
        >>> mesh.plot()
    """
    pass


import pyvista as pv

mesh = pv.Sphere()
mesh.plot()
