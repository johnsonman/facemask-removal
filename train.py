import argparse
from configs import Config
from trainer import Trainer

def main(args, cfg):
    trainer = Trainer(args, cfg)
    trainer.fit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Training custom model')
    parser.add_argument('--resume', default=None, type=str, help='resume training')
    parser.add_argument('config', default='config', type=str, help='config training')                         
    args = parser.parse_args() 

    config = Config(f'./configs/{args.config}.yaml')
    main(args, config)