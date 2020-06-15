import math
import pandas as pd
import numpy as np
import argparse


def RMSE(gt_value, pred_value):
    sum_error = 0
    length = len(gt_value)
    for i in range(length):
        sum_error += (gt_value[i] - pred_value[i]) ** 2
    sum_error = float(sum_error / length)
    sum_error = sum_error ** 0.5 + 1
    sum_error = math.log(sum_error)
    return sum_error


def read_file(file_name):
    label_index_pool = [2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 22, 23, 25, 26, 27, 28, 30, 32, 33, 34]
    f =  open(file_name, 'r', encoding='utf-8-sig')
    lines = f.readlines()
    
    result = []
    for line in lines[362:]:
        line = line.strip().split(',')
        for idx in label_index_pool:
            result.append(float(line[idx + 2]))

    f.close()
    return result


def evaluation_metrics(prediction_file, test_file):
    prediction_labels = read_file(prediction_file)
    gt_labels = read_file(test_file)

    return RMSE(prediction_labels, gt_labels)    


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--prediction_file', type=str, default='prediction.csv')
    args.add_argument('--test_file', type=str, default='data/validate.csv')

    config = args.parse_args()

    print(evaluation_metrics(config.prediction_file, config.test_file))