import numpy as np
def lisst(data, wavelength, bin_size=1.0):
    # Validate and preprocess input data
    if not isinstance(data, (list, np.ndarray)):
        raise TypeError("Data must be a list or numpy array.")
    if not isinstance(wavelength, (list, np.ndarray)):
        raise TypeError("Wavelength must be a list or numpy array.")
    data = np.asarray(data)
    wavelength = np.asarray(wavelength)

    # Apply binning to the data
    bin_edges = np.arange(wavelength.min(), wavelength.max() + bin_size, bin_size)
    binned_data, _ = np.histogram(wavelength, bins=bin_edges, weights=data)

    return binned_data