import cdsapi
import subprocess
import os
import sys

data_dir = os.path.dirname(sys.argv[0])

c = cdsapi.Client()
c.retrieve(
    'cams-global-reanalysis-eac4',
    {
        'format': 'netcdf',
        'variable': [
            'total_aerosol_optical_depth_1240nm', 'total_aerosol_optical_depth_469nm', 'total_aerosol_optical_depth_550nm',
            'total_aerosol_optical_depth_670nm', 'total_aerosol_optical_depth_865nm', 'total_column_carbon_monoxide',
            'total_column_ethane', 'total_column_formaldehyde', 'total_column_hydrogen_peroxide',
            'total_column_hydroxyl_radical', 'total_column_isoprene', 'total_column_methane',
            'total_column_nitric_acid', 'total_column_nitrogen_dioxide', 'total_column_nitrogen_monoxide',
            'total_column_ozone', 'total_column_peroxyacetyl_nitrate', 'total_column_propane',
            'total_column_sulphur_dioxide', 'total_column_water_vapour',
        ],
        'date': '2021-01-01/2021-01-31',
        'time': '00:00',
        'area': [
            47, 7, 36,
            18,
        ],
    },
    f'{data_dir}/italiaecmwf.nc')

# shapefile_url = "https://www.eea.europa.eu/data-and-maps/data/eea-reference-grids-2/gis-files/italy-shapefile/at_download/file"
# subprocess.run(f"wget {shapefile_url} -O {data_dir}/italy_shapefile.zip && unzip {data_dir}/italy_shapefile.zip -d {data_dir}/italy_shapefile && rm {data_dir}/italy_shapefile.zip", shell=True, check=True)