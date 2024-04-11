#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import statistics

data = [12,123,123,435,324,234,234,324,25,23,5,325,325,23,5,235,2,25,235,234,235,23,52,53]

print(statistics.harmonic_mean(data))
# 传入的参数是一个可以被迭代的数据集
# statistics.harmonic_mean()	计算给定数据集的调和平均值。
# statistics.mean()	计算数据集的平均值
# statistics.median()	计算数据集的中位数
# statistics.median_grouped()	计算给定分组数据集的分组中位数
# statistics.median_high()	计算给定数据集的高位中位数
# statistics.median_low()	计算给定数据集的低位中位数。
# statistics.mode()	算数据集的众数（出现频率最高的值）
# statistics.pstdev()	计算给定数据集的样本标准偏差
# statistics.stdev()	计算数据集的标准差
# statistics.pvariance()	计算给定数据集的样本方差
# statistics.variance()	计算数据集的方差
# statistics.quantiles()	计算数据集的分位数，可指定分位数的数量（默认为四分位数）