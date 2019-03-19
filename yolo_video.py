import os
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import json

def detect_img(yolo):
    test_path = './datas/test/jinnan2_round1_test_a_20190306/'
    for _,__,files in os.walk(test_path):
        break
    iii = 0
    json_file = {}
    all_pic_info = []
    for file_name in files[:2]:
        '''
        放入一张图片测试，生成数据集是否正常
        
        iii += 1
        if iii==2:
            break
        '''
        img = test_path + file_name
        print(img)
        try:
            image = Image.open(img.strip())
        except:
            print('Open Error! Try again!')
            continue
        else:
            
            r_image,infos = yolo.detect_image(image)
            '''
            此段程序为生成提交json结果代码
            '''
            
            dics = []
            
            if(len(infos) == 0):
                dics = []
            for info in infos:
                '''
                #跳过置信度<0.4的
                if info[5] <0.4:
                    continue
                '''
                dic = {"xmin": info[0], "xmax": info[1], "ymin": info[3], "ymax": info[2], "label": info[4], "confidence": round(info[5],1)}
                dics.append(dic)
            
            pic_info = {"filename": file_name, "rects": dics}
            
            all_pic_info.append(pic_info)
            
            
            #r_image.save('./output/test.jpg')
            #r_image.show()
    json_file = {"results":all_pic_info}
    
    f = open('submit.json','w',encoding='utf-8')
    #json_output = json.dumps(json_file)
    
    json_output = str(json_file)
    
    
    #将转化之后的单引号变为双引号
    str_to_write = ""
    for char in json_output:
        if char == "\'":
            str_to_write = str_to_write + chr(34)
        else:
            str_to_write = str_to_write + char
            
            
    
    #把json_file写入文件
    
    #print(json_file)
    f.write(str_to_write)
    
    f.close()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=True, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
