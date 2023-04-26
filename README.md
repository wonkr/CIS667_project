# CIS667_project

## collaborators
```
Kyungrok Won (https://github.com/wonkr)
Neda Abdolrahimi (https://github.com/NedaABD)
```

## dependencies
- `random`
- `numpy`
- `torch`
- `matplotlib.pyplot`

If you use `pip`, you can install the dependencies with
```
pip install random
pip install numpy
pip install torch
pip install matplotlib
```

## How to run interactive domain program
`python3 play_checker.py`

## How to evaluate minimax 
`python3 evaluate_minimax_checker.py`

Execution example. 
```
Choose problem size : 
1. 4 
2. 6 
3. 8 
4. 10 
5. 12 
3 <- input
Choos player 0 strategy : 
1. human 
2. baseline AI 
3. minimax 
4. nn 
1 <- input
Choos player 1 strategy : 
1. human 
2. baseline AI 
3. minimax 
4. nn 
3 <- input
['_' 'o' '_' 'o' '_' 'o' '_' 'o']
['o' '_' 'o' '_' 'o' '_' 'o' '_']
['_' 'o' '_' 'o' '_' 'o' '_' 'o']
['■' '_' '_' '_' '■' '_' '_' '_']
['_' '_' '_' '_' '_' '_' '_' '■']
['x' '_' 'x' '_' 'x' '_' 'x' '_']
['_' 'x' '_' 'x' '_' 'x' '_' 'x']
['x' '_' 'x' '_' 'x' '_' 'x' '_']
--- Player0's turn --->
Player 0, choose an action : 
0. (2, 1, 1, 1) 
1. (2, 3, 1, -1) 
2. (2, 5, 1, 1) 
3. (2, 7, 1, -1) 
0 <- input
['_' 'o' '_' 'o' '_' 'o' '_' 'o']
['o' '_' 'o' '_' 'o' '_' 'o' '_']
['_' '_' '_' 'o' '_' 'o' '_' 'o']
['■' '_' 'o' '_' '■' '_' '_' '_']
['_' '_' '_' '_' '_' '_' '_' '■']
['x' '_' 'x' '_' 'x' '_' 'x' '_']
['_' 'x' '_' 'x' '_' 'x' '_' 'x']
['x' '_' 'x' '_' 'x' '_' 'x' '_']
```

The action (2,1,1,1) represents move disk located in the position (2,1) in the board to move (+1, +1). 
The disk position will be (3,2) after the move. The column and the row starts from 0 in the board. 

## How to evaluate neural network
`python3 evaluate_nn_checker.py`

When you run the evaluate_nn_checker.py script, you can choose what configuration setting to use as below.

```
Choose configuration settings for a neural network: 
1. Kyungrok's configuration 
2. Neda's configuration 
```

If you want to run it with Kyungrok's configuration, you can input 1 and put enter.

This script will draw 2 plots. When the first plot (learning curve plot) is up, you need to close the window
to proceed the evaluation tasks. 

## Bibliography
```bib
@book{van1995python, 
  title={The Python Library Reference, release 3.8.2},
  author={Van Rossum, Guido}, 
  year={2020}, 
  publisher={Python Software Foundation} 
}

@ARTICLE{2020NumPy-Array,
  author  = {Harris, Charles R. and Millman, K. Jarrod and
            van der Walt, Stéfan J and Gommers, Ralf and
            Virtanen, Pauli and Cournapeau, David and
            Wieser, Eric and Taylor, Julian and Berg, Sebastian and
            Smith, Nathaniel J. and Kern, Robert and Picus, Matti and
            Hoyer, Stephan and van Kerkwijk, Marten H. and
            Brett, Matthew and Haldane, Allan and
            Fernández del Río, Jaime and Wiebe, Mark and
            Peterson, Pearu and Gérard-Marchant, Pierre and
            Sheppard, Kevin and Reddy, Tyler and Weckesser, Warren and
            Abbasi, Hameer and Gohlke, Christoph and
            Oliphant, Travis E.},
  title   = {Array programming with {NumPy}},
  journal = {Nature},
  year    = {2020},
  volume  = {585},
  pages   = {357–362},
  doi     = {10.1038/s41586-020-2649-2}
}

@incollection{NEURIPS2019_9015,
title = {PyTorch: An Imperative Style, High-Performance Deep Learning Library},
author = {Paszke, Adam and Gross, Sam and Massa, Francisco and Lerer, Adam and Bradbury, James and Chanan, Gregory and Killeen, Trevor and Lin, Zeming and Gimelshein, Natalia and Antiga, Luca and Desmaison, Alban and Kopf, Andreas and Yang, Edward and DeVito, Zachary and Raison, Martin and Tejani, Alykhan and Chilamkurthy, Sasank and Steiner, Benoit and Fang, Lu and Bai, Junjie and Chintala, Soumith},
booktitle = {Advances in Neural Information Processing Systems 32},
pages = {8024--8035},
year = {2019},
publisher = {Curran Associates, Inc.},
url = {http://papers.neurips.cc/paper/9015-pytorch-an-imperative-style-high-performance-deep-learning-library.pdf}
}

@Article{Hunter:2007,
  Author    = {Hunter, J. D.},
  Title     = {Matplotlib: A 2D graphics environment},
  Journal   = {Computing in Science \& Engineering},
  Volume    = {9},
  Number    = {3},
  Pages     = {90--95},
  abstract  = {Matplotlib is a 2D graphics package used for Python for
  application development, interactive scripting, and publication-quality
  image generation across user interfaces and operating systems.},
  publisher = {IEEE COMPUTER SOC},
  doi       = {10.1109/MCSE.2007.55},
  year      = 2007
}

@Techreport{mancala_helpers.py:2022,
  Author    = {Katz, G. }, 
  Title     = {mancala_helpers.py}, 
  Institution = {Syracuse University}
}

@Techreport{mancala_minimax.py:2022,
  Author    = {Katz, G. }, 
  Title     = {ProjectExample.ipynb}, 
  Institution = {Syracuse University}
}

@Techreport{play_mancala.py:2022,
  Author    = {Katz, G. }, 
  Title     = {mancala_minimax.py}, 
  Institution = {Syracuse University}
}
 
```
