# -*- coding: utf-8 -*-
# @Author: wmingdru
# @Software: PyCharm

import gradio as gr
import time

def show_params(source1,source2,model_name,conf,iou,classes,save):
    source = source1 if source1 else source2
    # 原始视频信息
    import cv2
    source_cap = cv2.VideoCapture(source)
    if not source_cap.isOpened():
        print("无法打开视频")
        exit()
    source_width = int(source_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    source_height = int(source_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    source_fps = round(source_cap.get(cv2.CAP_PROP_FPS))
    source_cap.release()
    all_params = {"模型":model_name,"置信度":conf,"IoU":iou,"目标类别":classes,"原视频":{"位置":source,"宽度":source_width,"高度":source_height,"fps":source_fps}}
    all_params2 = {"模型":model_name,"置信度":conf,"IoU":iou,"目标类别":classes,"原视频":{"位置":source,"宽度":source_width,"高度":source_height,"fps":source_fps},"结果视频":"./runs/detect/predict"}

    return all_params if not save else all_params2

def video_inference(model:str,source1:str,source2:str,conf:float,iou:float,classes:int,save:bool=False):
    """
    :param model: 模型名称
    :param source1: 本地视频文件
    :param source2: 视频流的URL
    :param conf: 置信度
    :param iou: IOU
    :param classes: 选择检测的类别
    :param save: 是否自动将结果视频保存
    :return:
    """
    gr.Info(message="ℹ️ℹ️加载模型中，请耐心等待...", duration=5)
    from ultralytics import YOLO
    import cv2
    print(locals())
    model = YOLO(model)
    #注:两种形式的视频，在前端我们选择了一种，则另一种为空;classes要放在列表中
    source = source1 if source1 else source2
    results = model(source=source,conf=conf,iou=iou,classes=[].append(classes),save=save,stream=True)
    processed_count = 0
    start_time = time.perf_counter()

    for result in results:
        result = result.plot()#将boxes打印画在原图上
        #如果原图比较大，这里将其缩放为原来的1/2，以便于观看
        if max(result.shape) > 700:
            new_size = (result.shape[1] // 2, result.shape[0] // 2)
            result = cv2.resize(result, new_size, interpolation=cv2.INTER_LINEAR)
        result = result[:, :, ::-1]#注意把推理结果的BGR图片转为RGB

        processed_count += 1
        consumption = round(time.perf_counter() - start_time,1)
        yield gr.Button(value="已处理{}帧，耗时{}秒".format(processed_count,consumption),visible=True),result

