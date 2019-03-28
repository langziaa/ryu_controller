# -*- coding: UTF-8 -*-
# light
from __future__ import division
# python2 the  / and the  // future need to import this 
 

if __name__ == '__main__':
    time_array=[]
    flow_mode = []
    check_result=[]
    self_jude=[]
    with open('detected.log', 'r') as f:
        for one in f.readlines():
            # print(one)
            data = one.split()
            # print(data[7])
            flow_mode.append(int(float(data[7])))
            check_result.append(int(float(data[8])))
            time_array.append(float(data[10]))
            self_jude.append(data[9])
    #print(flow_mode)
    #print(check_result)
    #print(time_array)
    #print(self_jude)

    # 误报率，正常流量中却报为错误
    normal_error = 0
    total_normal = 0
    for i in range(len(flow_mode)):
        if flow_mode[i] == 0:
            total_normal +=1
            if check_result[i] ==1:
                normal_error +=1
    # print(normal_error)
    # print(total_normal)

    normal_error_rate = normal_error/total_normal *100
    print("误报率为：" + str(normal_error_rate) + '%')



    # 识别率 ，异常流量正确被检测
    attack_right=0
    total_attack=0
    for i in range(len(flow_mode)):
        if flow_mode[i] == 1:
            total_attack +=1
            if check_result[i] == 1 :
                attack_right += 1
    
    #print(attack_right)
    #print(total_attack)
    attack_reg_rate = float(attack_right/total_attack) *100
    #print(attack_reg_rate)
    print("识别率" + str(attack_reg_rate) + "%")



    # 统计总体准确率  正确识别占据所有流量的统计
    i = 0
    for item in self_jude:
        if item == "correct":
            i +=1
    rate = i / len(self_jude) *100
    print("总体正确率" + str(rate) + "%")

    # 统计平均耗时
    total_cost = 0
    for item in time_array:
        total_cost +=item
    average_time = total_cost/len(time_array) *1000
    print("平均耗时为" + str(average_time) +" ms")