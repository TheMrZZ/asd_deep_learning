from nibabel import Nifti1Image, Nifti1Pair
from nibabel.filebasedimages import SerializableImage
from nilearn import image as niimage

path = r'./data/Caltech/0051456/session_1/anat_1/Caltech_0051456_brain_seg.nii.gz'
res = Nifti1Image.get_fdata(Nifti1Image.load(path)).shape