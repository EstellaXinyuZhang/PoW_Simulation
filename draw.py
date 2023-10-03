import matplotlib.pyplot as plt
import numpy as np


diff = [0.1, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
'''
fork_polar_2_7 = [0, 0, 0, 3, 6, 8, 13, 14, 20]
fork_uni = [0, 0, 1, 2, 3, 2, 3, 6, 6]
fork_polar_5_8 = [0, 0, 2, 4, 10, 14, 16, 9, 22]
'''
fork_uni = [0, 3/196, 5/363, 15/362, 27/720, 45/950, 84/1094, 100/1275, 98/1436]
fork_polar_2_7 = [9/62, 32/183, 57/313, 71/491, 84/644, 126/757, 137/942, 172/1068, 214/1224]
fork_polar_5_8 = [5/49, 15/170, 37/344, 51/498, 98/685, 101/886, 136/1068, 161/1176, 206/1449]
plt.plot(diff, fork_uni, label='Uniform')
plt.plot(diff, fork_polar_2_7, label='Polar (2:0.7)')
plt.plot(diff, fork_polar_5_8, label='Polar (5:0.8)')
plt.yticks(size=15)
plt.xticks(size=15)
plt.xlabel('The Number of Blocks Mined Per Minute', fontsize=17)
plt.ylabel('Stale Blocks Ratio', fontsize=17)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('diff.png')
plt.show()



den = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
'''
fork_den_polar_2_7 = [2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]
fork_den_uni = [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
fork_den_polar_5_8 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
'''
fork_den_uni = [3, 0, 1, 0, 0, 2, 0, 2, 0, 2, 0]
fork_den_polar_2_7 = [12, 4, 9, 3, 7, 8, 9, 9, 6, 7, 10]
fork_den_polar_5_8 = [6, 5, 11, 4, 6, 5, 12, 10, 10, 13, 3]
plt.plot(den, fork_den_uni, label='Uniform')
plt.plot(den, fork_den_polar_2_7, label='Polar (2:0.7)')
plt.plot(den, fork_den_polar_5_8, label='Polar (5:0.8)')
plt.yticks(size=12)
plt.xticks(size=12)
plt.xlabel('Edge Density of the Peer Network', fontsize=15)
plt.ylabel('The Number of Forks', fontsize=15)
plt.legend(fontsize=13)
plt.savefig('den_diff(0.1).png')
plt.show()


den = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
'''
fork_den_uni = [2, 1, 1, 0, 1, 2, 2, 0, 1, 0, 0]
fork_den_polar_2_7 = [3, 5, 0, 4, 5, 6, 7, 4, 2, 2, 3]
fork_den_polar_5_8 = [4, 2, 5, 2, 2, 7, 1, 2, 2, 2, 5]
'''
fork_den_uni = [30, 12, 8, 5, 8, 7, 11, 9, 5, 5, 6]
fork_den_polar_2_7 = [45, 71, 45, 54, 49, 32, 52, 51, 43, 41, 43]
fork_den_polar_5_8 = [41, 48, 52, 47, 38, 33, 38, 46, 29, 34, 44]
plt.plot(den, fork_den_uni, label='Uniform')
plt.plot(den, fork_den_polar_2_7, label='Polar (2:0.7)')
plt.plot(den, fork_den_polar_5_8, label='Polar (5:0.8)')
plt.xlabel('Edge Density of the Peer Network', fontsize=15)
plt.ylabel('The Number of Forks', fontsize=15)
plt.yticks(size=12)
plt.xticks(size=12)
plt.legend(fontsize=13)
plt.savefig('den_diff(0.5).png')
plt.show()


den = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
'''
fork_den_uni = [7, 5, 2, 2, 0, 4, 4, 2, 2, 0, 2]
fork_den_polar_2_7 = [8, 11, 5, 5, 8, 9, 6, 7, 8, 4, 6]
fork_den_polar_5_8 = [7, 6, 10, 6, 4, 12, 2, 7, 8, 5, 6]
'''
fork_den_uni = [79, 29, 23, 22, 30, 23, 19, 26, 16, 16, 16]
fork_den_polar_2_7 = [101, 79, 87, 83, 83, 88, 91, 85, 94, 92, 98]
fork_den_polar_5_8 = [87, 76, 84, 80, 72, 76, 82, 66, 78, 102, 87]
plt.plot(den, fork_den_uni, label='Uniform')
plt.plot(den, fork_den_polar_2_7, label='Polar (2:0.7)')
plt.plot(den, fork_den_polar_5_8, label='Polar (5:0.8)')
plt.xlabel('Edge Density of the Peer Network', fontsize=15)
plt.ylabel('The Number of Forks', fontsize=15)
plt.yticks(size=12)
plt.xticks(size=12)
plt.legend(loc="center right", fontsize=13)
plt.savefig('den_diff(1).png')
plt.show()



fork_01 = [1-3/64, 1-0, 1-1/71, 1-0, 1-0, 1-2/77, 1-0, 1-2/74, 1-0, 1-2/68, 1-0]
fork_05 = [1-30/389, 1-12/380, 1-8/357, 1-5/354, 1-8/340, 1-7/376, 1-11/383, 1-9/347, 1-5/376, 1-5/370, 1-6/313]
fork_1 = [1-79/746, 1-29/699, 1-23/702, 1-22/675, 1-30/791, 1-23/715, 1-19/723, 1-26/732, 1-16/764, 1-16/783, 1-16/756]
plt.plot(den, fork_01, label='0.1 block/min')
plt.plot(den, fork_05, label='0.5 block/min')
plt.plot(den, fork_1, label='1 block/min')
plt.xlabel('Edge Density of the Peer Network', fontsize=15)
plt.ylabel('Valid block ratio', fontsize=15)
plt.yticks(size=12)
plt.xticks(size=12)
plt.legend(fontsize=13)
plt.savefig('diff_den.png')
plt.show()


# 1 block/min
small_den_values = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
uni = [678/749, 672/715, 661/695, 676/707, 697/736, 674/714, 686/718, 689/720, 712/748]
polar_2 = [524/631, 533/643, 508/584, 505/620, 523/614, 529/638, 578/674, 535/619, 518/628]
polar_5 = [609/708, 647/757, 650/745, 649/744, 641/727, 632/726, 614/687, 609/693, 608/693]
plt.plot(small_den_values, uni, label='Uniform')
plt.plot(small_den_values, polar_2, label='Polar (2:0.7)')
plt.plot(small_den_values, polar_5, label='Polar (5:0.8)')
plt.xlabel('Edge Density of the Peer Network', fontsize=17)
plt.ylabel('Valid block ratio', fontsize=17)
plt.yticks(size=15)
plt.xticks(size=15)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('dist_den_small.png')
plt.show()


uni_01 = [79/83, 73/75, 58/59, 84/85, 70/72, 62/66, 67/69, 76/76, 67/69]
uni_05 = [349/371, 345/364, 355/362, 328/338, 326/334, 376/381, 368/378, 345/354, 349/364]
plt.plot(small_den_values, uni_01, label='0.1 block/min')
plt.plot(small_den_values, uni_05, label='0.5 block/min')
plt.plot(small_den_values, uni, label='1 block/min')
plt.xlabel('Edge Density of the Peer Network', fontsize=17)
plt.ylabel('Valid block ratio', fontsize=17)
plt.yticks(size=15)
plt.xticks(size=15)
plt.legend(fontsize=15)
plt.tight_layout()
plt.savefig('diff_den_small.png')
plt.show()


plt.figure()
fork_15 = [976/1064,906/1063,812/1063,730/1062]
fork_01 = [80/83,79/83,79/83,76/83]
fork_1 = [685/731,654/730,606/730, 557/728]
l = [500,1000,2000,3000]
plt.plot(l,fork_01, label='0.1 block/min')
plt.plot(l,fork_1, label='1 block/min')
plt.plot(l,fork_15, label='1.5 block/min')
plt.legend(fontsize=15)
plt.xlabel('Latency (ms)',size=17)
plt.ylabel('Valid Block Ratio',size=17)
plt.yticks(size=15)
plt.xticks(size=15)
plt.tight_layout()
plt.savefig('latency1.png')
plt.show()


plt.figure()
fork_15 = [826/965,818/963,793/956,774/951]
fork_01 = [53/62,53/62,53/62,53/62]
fork_1 = [552/644,548/643,539/640,524/640]
l = [500,1000,2000,3000]
plt.plot(l,fork_01, label='0.1 block/min')
plt.plot(l,fork_1, label='1 block/min')
plt.plot(l,fork_15, label='1.5 block/min')
plt.legend(fontsize=15)
plt.xlabel('Latency (ms)', size=17)
plt.ylabel('Valid Block Ratio', size=17)
plt.yticks(size=15)
plt.xticks(size=15)
plt.tight_layout()
plt.savefig('latency2.png')
plt.show()


