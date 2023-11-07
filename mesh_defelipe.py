# %%
from swc2mesh import Swc2mesh
from os.path import isfile, join, split
import glob
# from joblib import Parallel, delayed


def unit(swcname):
    folder, fname = split(swcname)
    mfolder = folder[:-3] + 'meshes'
    mname = fname.replace('.CNG.swc', '_cell-axon.ply')
    mesh_name = join(mfolder, mname)
    if not isfile(mesh_name):
        mesh_name = mesh_name.replace('_cell-axon.ply', '.ply')
        try:
            mesh = Swc2mesh(swcname, to_origin=False)
            mesh.build(mesh_name, compartment='cell-axon', simplification=True)
        except:
            print(f'Error: {swcname}')
    return None


swcfiles = glob.glob('NeuronSet/defelipe/swc_files/*.CNG.swc')

for f in swcfiles:
    unit(f)
