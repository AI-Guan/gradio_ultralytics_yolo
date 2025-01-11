# -*- coding: utf-8 -*-
# @Author: xguan
# @Software: PyCharm

import gradio as gr

theme = gr.themes.Default(
    primary_hue="rose",
    neutral_hue="slate",
).set(
    border_color_accent_subdued='*border_color_accent',
    block_shadow='none',
    block_shadow_dark='none',
    form_gap_width='0px',
    checkbox_label_background_fill='*button_secondary_background_fill',
    checkbox_label_background_fill_dark='*button_secondary_background_fill',
    checkbox_label_background_fill_hover='*button_secondary_background_fill_hover',
    checkbox_label_background_fill_hover_dark='*button_secondary_background_fill_hover',
    checkbox_label_shadow='none',
    error_background_fill_dark='*background_fill_primary',
    input_background_fill='*neutral_100',
    input_background_fill_dark='*neutral_700',
    input_border_width='0px',
    input_border_width_dark='0px',
    input_shadow='none',
    input_shadow_dark='none',
    input_shadow_focus='*input_shadow',
    input_shadow_focus_dark='*input_shadow',
    stat_background_fill='*primary_300',
    stat_background_fill_dark='*primary_500',
    button_shadow='none',
    button_shadow_active='none',
    button_shadow_hover='none',
    button_transition='background-color 0.2s ease',
    button_primary_background_fill='*primary_200',
    button_primary_background_fill_dark='*primary_700',
    button_primary_background_fill_hover='*button_primary_background_fill',
    button_primary_background_fill_hover_dark='*button_primary_background_fill',
    button_primary_border_color_dark='*primary_600',
    button_secondary_background_fill='*neutral_200',
    button_secondary_background_fill_dark='*neutral_600',
    button_secondary_background_fill_hover='*button_secondary_background_fill',
    button_secondary_background_fill_hover_dark='*button_secondary_background_fill',
    button_cancel_background_fill='*button_secondary_background_fill',
    button_cancel_background_fill_dark='*button_secondary_background_fill',
    button_cancel_background_fill_hover='*button_cancel_background_fill',
    button_cancel_background_fill_hover_dark='*button_cancel_background_fill',
    button_cancel_border_color='*button_secondary_border_color',
    button_cancel_border_color_dark='*button_secondary_border_color',
    button_cancel_text_color='*button_secondary_text_color',
    button_cancel_text_color_dark='*button_secondary_text_color'
)

js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';
    container.style.backgroundImage = 'url("file=head.png")';
    container.style.backgroundSize = "contain";
    container.style.backgroundRepeat = 'no-repeat';

    var text = '在线视频推理';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""
css = """
.confirm {background-color: #d4e7fe !important}
"""