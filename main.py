import argparse
from engine.engine import EngineTheRun

def parse_arg():
    parser = argparse.ArgumentParser(description='the parser')
    parser.add_argument('--mode', help='t = train, i = inference')
    parser.add_argument('--show',action='store_true', help='Whether to show the image')
    parser.add_argument('--model_path', help='The path of pth file')
    parser.add_argument('--image_path', help='The path of image file or folder')
    parser.add_argument('--backbone', default = 'VGG16', help='The backbone network')
    args = parser.parse_args()
    return args
def main():
    args = parse_arg()
    
    runner = EngineTheRun(args)
    if args.mode == 'train':
        runner.train()
    elif args.mode == 'inference':
        runner.inference()
        return


    

if __name__ == "__main__":
    # print(torch.__version__)
    # print(np.__version__)
    main()