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
    
## Fundamental Dimensions
'''
If more are needed, simply append to the list of labels. However, user should
ensure the included dimensions are mutually independent.
'''
labels = ['Mass', 'Length', 'Time', 'Temperature', 'E_Current', \
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
# note: E_ prefix used as shorthand for "Electric_"
E_Current   = fundamental_dims[labels['E_Current']]
'''
note that Quantity can be set equal to Dimensionless if it is not needed
for disambiguation
'''
Quantity    = fundamental_dims[labels['Quantity']]

## Derived Dimensions
### derived from Fundamental Dimensions
Velocity               = Length/Time
Area                   = Length**2
Volume                 = Length**3
Frequency              = Time**(-1)
Wavenumber             = Length**(-1)
Charge                 = E_Current*Time
Thermal_Expansion      = Temperature**(-1)

### derived from other Derived Dimensions
Acceleration           = Velocity/Time
Force                  = Mass*Acceleration
Energy                 = Force*Length
Power                  = Energy/Time
Pressure               = Force/Area # == stress, bulk modulus
Compressibility        = Pressure**(-1)
Density                = Mass/Volume
Number_Density         = Quantity/Volume
Surface_Tension        = Force/Length

Voltage                = Energy/Charge
E_Resistance           = Voltage/E_Current
E_Conductance          = E_Resistance**(-1)
Capacitance            = Charge/Voltage
E_Field                = Force/Charge
B_Field                = Force/Charge/Velocity
Magnetic_Permeability  = Force/E_Current**2
H_Field                = B_field/Magnetic_Permeability
E_Inductance           = Energy/E_Current**2
Permittivity           = Capacitance/Length

Dynamic_Viscosity      = Pressure*Time
Kinematic_Viscosity    = Dynamic_Viscosity/Density

## Physical Constants
Planck_const           = Energy*Time
Boltzmann_const        = Energy/Temperature # == heat capacity, entropy
Avogadro_const         = Quantity**(-1)
Ideal_gas_const        = Energy/Temperature/Quantity
Gravitational_const    = Force*Area/Mass**2
Coulomb_const          = Force*Area/Charge**2
Stefan_Boltzmann_const = Power/Area/Temperature**4
Cosmological_const     = Area**(-1)