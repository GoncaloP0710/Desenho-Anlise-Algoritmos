# Desenho e Análise de Algoritmos

This repository contains various assignments and projects related to the course "Desenho e Análise de Algoritmos" (Design and Analysis of Algorithms).

## Table of Contents

- [Introduction](#introduction)
- [Assignments](#assignments)
  - [TP_1: Search Algorithms](#tp_1-search-algorithms)
  - [TP_2: Graph Algorithms](#tp_2-graph-algorithms)
- [Virtual Environment Setup](#virtual-environment-setup)

## Introduction

This repository contains Jupyter notebooks and Python scripts that demonstrate various algorithms and data structures covered in the course.

## Assignments

### TP_1: Search Algorithms

- **01. Search (student).ipynb**: Introduction to search algorithms including linear search, binary search, and heuristic search.
- **Maze.ipynb**: Solving maze problems using different search strategies.
- **Maze.py**: Python script for maze solving.

### TP_2: Graph Algorithms

- **02. Graphs (student).ipynb**: Introduction to graph algorithms including traversal, shortest path, and Eulerian paths.
- **temp.dot**: DOT file for graph visualization.
- **temp.png**: PNG image of the graph.


## Virtual Environment Setup

1. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```

2. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. To save the current environment's packages to `requirements.txt`:
    ```sh
    pip freeze > requirements.txt
    ```