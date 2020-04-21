[<< Back](https://cntt-n.github.io/CNTT/)
# Handling of figures

## Table of Contents

* [1 Usage of figures](#1)

<a name="1"></a>
## 1 Usage of figures

- Figures used in the document should be in Portable Network Graphic (`png`) or in Scalable Vector Graphics (`svg`) format
- Figures must be stored in the `figures` folder of the document where the figures are used (e.g.: `doc/ref_model/figures/`or `'doc/ref_arch/openstack/figures`)
- File name of the figures shold contain the Work Stream and the chapter number where the figure is used as a prefix (e.g.: `ra2-ch02-topic-of-the-figure`)
- Every `png` figure used in the documents should have an editable version commited to the repository in PowerPoint (`ppt(x)`) or in `svg` format (in case of `svg` format consider using the file directly from the `figures` folder instead of rendering it into `png`)
- Editable versions should be stored in the `artefacts` folder of the document where the figures are used (e.g.: `doc/ref_model/artefacts` or `'doc/ref_arch/openstack/artefacts`)
- Each figure's aditable version should be stored in a separate file with the same file name, but different extension, as the figure itself