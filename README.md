# How develop a maintainable batch job

## Table of Contents

- [About](#about)
- [Generators](#part1)
- [Loaders](#part2)
- [Transformers](#part3)
- [Runners](#part4)
- [Exporters](#part5)

## About <a name = "about"></a>

Process to create a maintainable batch job

Our project is divided into five parts:

## Generators <a name="part1"></a>

Scripts to generate CSV data used in the project; store in the `data` folder. There will be two kinds:
- Cart update
- User visit

## Loaders <a name="part2"></a>

Functions to load a CSV and return a pandas DataFrame.

## Transformers <a name="part3"></a>

Scripts that contain the multiple transformation of data needed for our DataFrame to be used for the project, as well as a main function that can be called in a pipeline way to have a full view of the transformations.

## Runners <a name="part4"></a>

Scripts that will load data, execute the transformation, and export the data to another backend, such as an SQLite DB.

## Exporters <a name="part5"></a>

Functions to export to the SQLite DB in the `data` folder.
