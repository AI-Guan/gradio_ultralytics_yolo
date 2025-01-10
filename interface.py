# -*- coding: utf-8 -*-
# @Author: wmingdru
# @Software: PyCharm

import gradio as gr
from style import js,css,theme
from action_function import show_params,video_inference

gr.set_static_paths(["head.png"]) #使用到的静态文件要添加到列表中



with gr.Blocks(theme=theme,fill_width=True,title="gradio and YOLO",js=js,css=css) as video_processing:
    #gr.Markdown("""# 在线视频推理""")
    with gr.Row():
        with gr.Column():
            with gr.Tab("选择视频"):
                # 选择不同的视频源将会显示不同的组件
                source_radio = gr.Radio(["视频文件或webcam", "URL"], label="选择视频源")
                input_video = gr.File(label="视频文件",visible=False)
                with gr.Row():
                    url_input = gr.Textbox(label="输入URL地址", visible=False,
                                           placeholder="RTSP,RTMP,TCP或视频流的IP地址",
                                           interactive=True,scale=15)
                    # confirm_btn = gr.Button("确定",elem_classes="confirm",visible=False,scale=1,min_width=100)


                # 返回组件参见https://www.gradio.app/guides/blocks-and-event-listeners#updating-component-configurations
                @source_radio.select(inputs=source_radio, outputs=[input_video, url_input])
                def show_or_hidden(selected):
                    if selected == "视频文件或webcam":
                        return gr.File(visible=True), gr.Textbox(visible=False)
                    else:
                        return gr.File(visible=False), gr.Textbox(visible=True)

            with gr.Tab("选择模型"):
                model_name = gr.Dropdown(["yolo11n", "yolo11s", "yolo11m", "yolo11l"], label="模型列表",
                                         value="yolo11n",
                                         interactive=True)

            with gr.Accordion(label="参数设置",open=False):
                with gr.Row():
                    conf = gr.Slider(0, 1, value=0.5, label="置信度大小",interactive=True)
                    iou = gr.Slider(0, 1, value=0.7, label="IoU阈值")
                with gr.Row():
                    classes = gr.Number(0, label="目标类别")
                    save = gr.Radio([True, False], value=False, label="将推理结果视频自动保存在服务端")

            start_btn = gr.Button("开始",variant="primary")

        with gr.Column():
            output_image = gr.Image(label="推理结果")
            process_info = gr.Button(variant="secondary",visible=False)
            params = gr.JSON(label="参数值展示")

    start_btn.click(fn=show_params, inputs=[input_video,url_input,model_name,conf,iou,classes,save],
                    outputs=[params], api_name="detector").then(fn=video_inference, inputs=[model_name,input_video,url_input,conf,iou,classes,save],outputs=[process_info,output_image])

if __name__ == "__main__":
    video_processing.launch(server_port=9993)
