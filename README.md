# TSS 1.0
## Tile Size Selection 
*Optimization of loop programs is an important topic in program optimization. As a typical technique of loop optimization, loop tiling has been widely studied and applied. The selection of tile size, which is complex and highly dependent on program and hardware, has a great impact on the performance of loops. Traditional approaches based on static analysis and heuristic experience search have high cost of labor and time, and lack generality and portability. Therefore, the neural network method, which is good at representing high-dimensional information, is considered to learn the hidden correlation between tiling size and program performance, which is a result of complex interaction between program and hardware.*

link:http://www.jsjkx.com/CN/10.11896/jsjkx.191200180

CHI Hao-yu, CHEN Chang-bo. Prediction of Loop Tiling Size Based on Neural Network[J]. Computer Science, 2020, 47(8): 62-70.

Related work:https://link.springer.com/chapter/10.1007/978-3-030-52200-1_28#citeas

Abstract：

   Optimization of loop programs is an important topic in program optimization. As a typical technique of loop optimization, loop tiling has been widely studied and applied. The selection of tile size, which is complex and highly dependent on program and hardware, has a great impact on the performance of loops. Traditional approaches based on static analysis and heuristic experience search have high cost of labor and time, and lack generality and portability. Therefore, the neural network method, which is good at representing high-dimensional information, is considered to learn the hidden correlation between tiling size and program performance, which is a result of complex interaction between program and hardware. A new group of features with 29 dimensions are extracted based on size of the problem, structure of the loop, locality of the operations within the loop. The experiments are carried out on hundreds of thousands of lines of six kinds of kernel programs (3D loop, 2D data) with random sizes in the range of 1024 to 2048. Compared with GCC-O2, the sequential model (TSS-T6) achieves an average speedup of 6.64, 98.5% of the average maximum available performance, and an average 9.9% performance improvement compared with Pluto. The parallel model (TSSP-T6-Search) achieves an average speedup of 2.41 compared with the OpenMP default optimization, 91.7% of the average maximum available performance compared with the exhaustive search, and an average 9% performance improvement compared with Pluto default parallel tiling optimization.
   
  循环程序的优化一直是程序优化的重点，循环分块作为一种典型的循环程序优化技术已被广泛的研究和应用。分块大小的选择对循环程序的性能有着重要影响，分块大小选择复杂多变且高度依赖程序和硬件。传统的静态分析和启发式经验搜索的人工和时间成本过高，缺少通用性和可移植性。为此考虑使用有良好高维表示特性的神经网络方法去学习程序与硬件复杂交互过程中分块大小与程序性能的隐含关联。从问题规模、循环结构、循环内操作的局部性等方面抽取出新的一组29维特征，对问题规模为1024至2048范围内随机大小的六类内核程序（3维循环、2维数据）的数十万行示例进行实验。串行模型（TSS-T6）相比GCC-O2默认优化实现了6.64倍的平均加速比，相比穷尽搜索实现了98.5%的平均最大可用性能，和Pluto默认分块优化相比实现了平均9.9%的性能提升。并行模型（TSSP-T6-Search）相比OpenMP默认优化实现了2.41倍的平均加速比，相比穷尽搜索实现了91.7%的平均最大可用性能，同时和Pluto默认分块并行优化相比得到了平均9%的性能提升。 

New Version: https://github.com/CharlieCurry/TSS2.0
