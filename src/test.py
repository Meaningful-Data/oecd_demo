from pysdmx.io import get_datasets
from pysdmx.api.qb.service import RestService
from pysdmx.api.qb.structure import StructureQuery, StructureFormat, StructureType, StructureReference, StructureDetail
from pysdmx.api.qb.data import DataQuery, DataFormat
from pysdmx.api.qb.util import ApiVersion
from pysdmx.io import get_datasets
from pysdmx.model.dataflow import Role



data_query = "https://sdmx.oecd.org/public/rest/data/OECD.CFE.EDS,DSD_REG_CLIM@DF_AIR_TEMP,/all?startPeriod=2023"
metadata_query = "https://sdmx.oecd.org/public/rest/dataflow/OECD.CFE.EDS/DSD_REG_CLIM@DF_AIR_TEMP/?references=all"

data = get_datasets(
    data=data_query,
    structure=metadata_query)

print(data)





