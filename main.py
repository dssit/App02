# -*- coding: utf-8 -*-
import Draw
import Crawling_Data
import SparkBatch_Data

if __name__ == '__main__':

    print("开始总程序")
    Filename = "rent.csv"
    Crawling_Data.run()
    all_list = SparkBatch_Data.spark_analyse(Filename)
    Draw.draw_bar(all_list)