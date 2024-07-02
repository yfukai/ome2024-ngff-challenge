# %% 

import zarr
import s3fs

# Create a S3FileSystem object
s3 = s3fs.S3FileSystem(anon=False, skip_instance_cache=True)

# Define the Zarr store URL
zarr_url = "s3://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0001A/2551.zarr"

# Open the Zarr store using the S3FileSystem
store = s3.get_mapper(zarr_url)
store = zarr.storage.FSStore("https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0076A/10501752.zarr")
# Open the Zarr group
root = zarr.open(store=store, mode='r')

# List the content of the root store
print(root.info)
print(root.tree())
print(root["0"])


# %%
