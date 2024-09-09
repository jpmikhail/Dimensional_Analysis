'''
This script is meant to be a general example of setting up and using Dimension
instances.

More complicated Dimension instances can be built up by using the fundamental
dimensions (Mass, Length, Time, etc.) with their associated methods for
combining dimensions. They can also be defined directly by specifying an
appropriate 'values' vector.
'''

import numpy as np
from Dimension import Dimension
    
## Fundamental dimensions
# if more are needed, simply append to the list of labels. However, user should
#   ensure the included dimensions are mutually independent
labels = ['Mass', 'Length', 'Time', 'Temperature', 'Current', \
          'Luminous_Intensity', 'Quantity']
n_dims = len(labels)

labels = {labels[i]: i for i in range(n_dims)}
base_values = np.zeros(n_dims, dtype = np.int64)
Dimensionless = Dimension(base_values)
fundamental_dims = [None for i in range(n_dims)]

for i in range(n_dims):
    values = base_values.copy()
    values[i] = 1
    fundamental_dims[i] = Dimension(values)
    
Mass        = fundamental_dims[labels['Mass']]
Length      = fundamental_dims[labels['Length']]
Time        = fundamental_dims[labels['Time']]
Temperature = fundamental_dims[labels['Temperature']]
Current     = fundamental_dims[labels['Current']]
Quantity    = fundamental_dims[labels['Quantity']]

## Derived dimensions
Velocity = Length/Time
Acceleration = Velocity/Time
Area = Length**2
Volume = Length**3
Force = Mass*Acceleration
Energy = Force*Length
Pressure = Force/Area # also stress or bulk modulus
Compressibility = Pressure**(-1)
Density = Mass/Volume
Number_Density = Volume**(-1)
Frequency = Time**(-1)
Surface_Tension = Force/Length
Wavenumber = Length**(-1)
Charge = Current/Time
Voltage = Energy/Charge
E_Field = Force/Charge
B_Field = Force/Charge/Velocity
Dynamic_Viscosity = Pressure*Time
Kinematic_Viscosity = Dynamic_Viscosity/Density
Thermal_Expansion = Temperature**(-1)

## Physical constants
Planck_const = Energy*Time
# heat capacity, entropy
Boltzmann_const = Energy/Temperature
Ideal_gas_const = Energy/Temperature/Quantity
