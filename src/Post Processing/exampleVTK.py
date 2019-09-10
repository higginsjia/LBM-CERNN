from dataSave import *

# Get the macroscopics in the folder
macr = getEachMacr3D()
info = getSimInfo()

# Add velocity norm as a macroscopic
macr['nmVel'] = np.ndarray(dtype=float, shape=(info['NX'], info['NY'], info['NZ']))
for x in range(0, info['NX']):
    for y in range(0, info['NY']):
        for z in range(0, info['NZ']):
            macr['nmVel'][x, y, z] = np.linalg.norm([macr['ux'][x, y, z], \
                        macr['uy'][x, y, z], macr['uz'][x, y, z]])

# Save macroscopics to VTK format
saveVTK3D(macr, "000macr")

# Save average uz(y, x=0.5, z=[0, 1]) to csv
uz = macr['uz']
uz = [np.average(uz[info['NX']//2, y, :]) for y in range(0, info['NY'])] # uz <= uz[x=NX/2, y=NY/2, z]
saveMacrLineCsv("000uz.csv", uz)

